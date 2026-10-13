#!/usr/bin/env python3
"""Modèle économique et financier de La Saffranerie (bibliothèque standard uniquement).

    python3 saffranerie.py                 # lit hypotheses.json, écrit sorties/*.md et ../numbers.json
    python3 saffranerie.py --hyp autre.json

Chaque chiffre vient de hypotheses.json (étiquettes C/V/E/H). Le modèle :
  1. coûte chaque produit (matières, safran au prix de cession, crème, emballage, pertes, carte) ;
  2. construit un ticket moyen pondéré à partir d'un mix d'unités pour 100 tickets ;
  3. calcule charges fixes, personnel par planning, point mort, capacité ;
  4. simule la première année mois par mois (rampe, saison, TVA, trésorerie) ;
  5. décompose le financement minimum, compare les scénarios et fait les sensibilités ;
  6. écrit numbers.json pour l'outil unit_economics.py du skill founder-cfo.
"""

import argparse
import copy
import datetime
import json
import math
import os

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIES = os.path.join(ICI, "sorties")
CATS = ["boissons", "gourmandises", "formules", "safran", "pots"]
NOM_CAT = {"boissons": "Boissons", "gourmandises": "Gourmandises", "formules": "Formules",
           "safran": "Safran", "pots": "Crème en pots et coffrets"}


# ── formats ─────────────────────────────────────────────────────────────────────
def e(x, dec=0):
    """Montant en euros, format français."""
    if x is None or (isinstance(x, float) and math.isinf(x)):
        return "—"
    s = ("{:,.%df}" % dec).format(abs(x)).replace(",", " ").replace(".", ",")
    return ("−" if x < 0 else "") + s + " €"


def n(x, dec=0):
    if x is None or (isinstance(x, float) and math.isinf(x)):
        return "—"
    s = ("{:,.%df}" % dec).format(abs(x)).replace(",", " ").replace(".", ",")
    return ("−" if x < 0 else "") + s


def pc(x, dec=0):
    return ("{:.%df}" % dec).format(x * 100).replace(".", ",") + " %"


# ── produits ────────────────────────────────────────────────────────────────────
def creme_cout_kg(H, mode=None):
    c = H["creme"]
    mode = mode or c["mode_retenu"]
    ing = sum(f["part"] * f["cout_kg"] for f in c["formule_hypothese"])
    ing += c["safran_g_par_kg"] * H["safran"]["prix_cession_g"]
    m = c["modes"][mode]
    base = ing + m.get("main_oeuvre_kg", 0) + m.get("facon_kg", 0)
    return base / (1 - m["perte"])


def produit(p, H):
    ck = creme_cout_kg(H)
    ht_sp = p["prix_ttc"] / (1 + p["tva_sp"])
    ht_emp = p["prix_ttc"] / (1 + p["tva_emp"])
    ht = p["part_sp"] * ht_sp + (1 - p["part_sp"]) * ht_emp
    saf = p["safran_g"] * H["safran"]["prix_cession_g"]
    cre = p["creme_g"] / 1000.0 * ck
    mat = p["matieres"] + saf + cre
    emb = p["part_sp"] * p["emb_sp"] + (1 - p["part_sp"]) * p["emb_emp"]
    perte = mat * p["perte"]
    cb = p["prix_ttc"] * H["taux_cb"]
    var = mat + emb + perte + cb
    safran_g_total = p["safran_g"] + p["creme_g"] / 1000.0 * H["creme"]["safran_g_par_kg"]
    return {"id": p["id"], "nom": p["nom"], "cat": p["cat"], "statut": p["statut"], "ttc": p["prix_ttc"],
            "ht": ht, "tva": p["prix_ttc"] - ht, "mat": p["matieres"], "saf": saf, "cre": cre, "emb": emb,
            "perte": perte, "cb": cb, "var": var, "marge": ht - var, "marge_pct": (ht - var) / ht,
            "cout_matiere_pct": (mat + emb + perte) / ht, "safran_g": safran_g_total,
            "temps_s": p["temps_s"], "note": p.get("note", "")}


def table_produits(H):
    return {p["id"]: produit(p, H) for p in H["produits"]}


# ── mix et ticket ───────────────────────────────────────────────────────────────
def mix_mois(H, mois_cal, scen):
    mx = H["mix_pour_100_tickets"]
    sc = H["scenarios"][scen]
    u = dict(mx["permanent"])
    if mois_cal in mx["mois_saison"]:
        for k, v in mx["saison"].items():
            u[k] = u.get(k, 0) + v
    cat = {p["id"]: p["cat"] for p in H["produits"]}
    boost = mx.get("boost_cadeaux", {}).get(str(mois_cal), 1.0)
    for k in list(u):
        if cat[k] in ("safran", "pots"):
            u[k] = u[k] * sc.get("retail_mult", 1.0) * boost
    return u


def ticket(H, units, P=None):
    P = P or table_produits(H)
    t = {"ttc": 0.0, "ht": 0.0, "var": 0.0, "mat_emb_perte": 0.0, "cb": 0.0, "safran_g": 0.0, "items": 0.0,
         "temps_s": H["capacite"]["secondes_encaissement_ticket"], "cat_ht": {c: 0.0 for c in CATS},
         "cat_units": {c: 0.0 for c in CATS}}
    for k, q in units.items():
        r = P[k]
        f = q / 100.0
        t["ttc"] += f * r["ttc"]
        t["ht"] += f * r["ht"]
        t["var"] += f * r["var"]
        t["cb"] += f * r["cb"]
        t["mat_emb_perte"] += f * (r["var"] - r["cb"])
        t["safran_g"] += f * r["safran_g"]
        t["items"] += f
        t["temps_s"] += f * r["temps_s"]
        t["cat_ht"][r["cat"]] += f * r["ht"]
        t["cat_units"][r["cat"]] += f
    t["contrib"] = t["ht"] - t["var"]
    t["contrib_pct"] = t["contrib"] / t["ht"]
    return t


def ticket_annuel(H, scen):
    """Ticket moyen pondéré par les volumes mensuels (saisonnalité) sur 12 mois calendaires."""
    P = table_produits(H)
    w = H["saisonnalite_calendaire"]
    acc = None
    tot = 0.0
    for m in range(1, 13):
        t = ticket(H, mix_mois(H, m, scen), P)
        wt = w[str(m)]
        tot += wt
        if acc is None:
            acc = {k: (v * wt if not isinstance(v, dict) else {c: x * wt for c, x in v.items()}) for k, v in t.items()}
        else:
            for k, v in t.items():
                if isinstance(v, dict):
                    for c, x in v.items():
                        acc[k][c] += x * wt
                else:
                    acc[k] += v * wt
    for k, v in acc.items():
        if isinstance(v, dict):
            for c in v:
                v[c] /= tot
        else:
            acc[k] = v / tot
    acc["contrib_pct"] = acc["contrib"] / acc["ht"]
    return acc


# ── personnel et charges fixes ──────────────────────────────────────────────────
def cout_salarie(H, kind, heures):
    S = H["personnel"]
    if kind == "ft":
        return S["cout_ft"] + S["mutuelle_medecine_par_salarie"]
    if kind == "resp":
        return S["cout_resp"] + S["mutuelle_medecine_par_salarie"]
    if kind == "pt":
        brut = heures * 52 / 12 * S["taux_horaire_pt"]
        return brut * S["ratio_cout_pt"] + S["mutuelle_medecine_par_salarie"] / 2
    raise ValueError(kind)


def personnel(H, planning=None):
    S = H["personnel"]
    pl = S["plannings"][planning or S["planning_retenu"]]
    lignes = [(lab, cout_salarie(H, k, h), h) for lab, k, h in pl["salaries"]]
    base = sum(c for _, c, _ in lignes)
    prov = base * pl["provision"]
    fond_h = sum(h for _, h in pl["fondateurs"])
    fond_val = fond_h * 52 / 12 * S["cout_horaire_fondateur_valorise"]
    return {"label": pl["label"], "lignes": lignes, "base": base, "provision": prov, "total": base + prov,
            "fondateurs": pl["fondateurs"], "fond_h": fond_h, "fond_valorisation": fond_val,
            "heures_salaries": pl["heures_couvertes_salaries"]}


def charges_fixes(H, planning=None, marketing=None, cle="central", annee1=True):
    lignes = [(c["label"], c[cle], c["tva"], c["statut"]) for c in H["charges_fixes"]]
    pers = personnel(H, planning)
    mk = H["marketing"]
    mens = marketing if marketing is not None else mk["B_mensuel"]
    hors_pers = sum(l[1] for l in lignes)
    return {"lignes": lignes, "hors_personnel": hors_pers, "personnel": pers, "marketing": mens,
            "total": hors_pers + pers["total"] + mens}


# ── point mort et capacité ──────────────────────────────────────────────────────
def point_mort(H, scen="central", planning=None, marketing=None, valoriser=False, t=None):
    t = t or ticket_annuel(H, scen)
    cf = charges_fixes(H, planning, marketing)
    fixe = cf["total"] + (cf["personnel"]["fond_valorisation"] if valoriser else 0.0)
    jours = H["calendrier"]["jours_par_mois"]
    tj = fixe / (t["contrib"] * jours) if t["contrib"] > 0 else math.inf
    ho = H["horaires"]
    h_jour = ho["heures_ouverture_semaine"] / 7.0
    return {"fixe": fixe, "tickets_jour": tj, "ca_ht_mois": tj * jours * t["ht"], "ca_ht_jour": tj * t["ht"],
            "ca_ttc_jour": tj * t["ttc"], "ca_ttc_mois": tj * jours * t["ttc"], "par_heure": tj / h_jour,
            "pointe": tj * ho["part_ventes_heure_pointe"],
            "cat_jour": {c: tj * t["cat_units"][c] for c in CATS}, "ticket": t}


def capacite(H, t):
    C = H["capacite"]
    ho = H["horaires"]
    s = t["temps_s"]
    un = 3600 * C["utilisation"] / s
    deux = un * C["facteur_deux_personnes"]
    h_jour = ho["heures_ouverture_semaine"] / 7.0
    renfort_jour = ho["renfort_poste2_semaine"] / 7.0
    jour = (h_jour - renfort_jour) * un + renfort_jour * deux
    return {"sec_ticket": s, "une_personne_h": un, "deux_personnes_h": deux, "jour": jour}


# ── simulation mensuelle ────────────────────────────────────────────────────────
def mois_cal(H, i):
    d = datetime.date.fromisoformat(H["calendrier"]["ouverture_hypothetique"])
    m = (d.month - 1 + i) % 12 + 1
    y = d.year + (d.month - 1 + i) // 12
    return y, m


NOMS_MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]


def simulation(H, scen="central", planning=None, marketing_mensuel=None, lancement=None, valoriser=False,
               volume_mult=1.0, invest_cle="ht", sans_signature=False, mois=24):
    P = table_produits(H)
    sc = H["scenarios"][scen]
    cf = charges_fixes(H, planning, marketing_mensuel)
    pers = cf["personnel"]
    jours = H["calendrier"]["jours_par_mois"]
    rampe = H["montee_en_puissance"]
    saison = H["saisonnalite_calendaire"]
    delai = H["tva"]["delai_remboursement_credit_mois"]
    # investissements (index de mois relatif : −3..0)
    inv = copy.deepcopy(H["investissement"])
    if lancement is not None:
        for it in inv:
            if it["label"].startswith("Communication de lancement"):
                it[invest_cle if invest_cle in it else "ht"] = lancement
                it["ht"] = lancement
    debut = min(it["mois"] for it in inv)
    T = list(range(debut, mois))
    flux = {t: {"encaissements": 0.0, "decaissements": 0.0, "tva_nette": 0.0, "invest_ttc": 0.0, "invest_tva": 0.0}
            for t in T}
    depot = 0.0
    immob = []
    charges_pre = 0.0
    stock = 0.0
    for it in inv:
        v = it[invest_cle] if invest_cle in it else it["ht"]
        tva = v * it["tva"]
        flux[it["mois"]]["invest_ttc"] += v + tva
        flux[it["mois"]]["invest_tva"] += tva
        if it["nature"] == "depot":
            depot += v
        elif it["nature"] in ("immobilisation",):
            immob.append((v, it.get("amort_ans", 5)))
        elif it["nature"] == "immobilisation_non_amortie":
            pass
        elif it["nature"] == "stock":
            stock += v
        else:
            charges_pre += v
    amort_mois = sum(v / a / 12.0 for v, a in immob)
    fixe_tva = sum(l[1] * l[2] for l in cf["lignes"])
    rows = []
    credit_tva = 0.0
    remb = {}
    cum = 0.0
    cum_min = 0.0
    t_min = debut
    cum_op = 0.0
    cum_op_min = 0.0
    for t in T:
        f = flux[t]
        row = {"t": t, "tickets_jour": 0.0, "ca_ht": 0.0, "ca_ttc": 0.0, "var": 0.0, "contrib": 0.0, "fixe": 0.0,
               "ebitda": 0.0, "amort": 0.0, "resultat": 0.0, "safran_g": 0.0}
        tva_collectee = 0.0
        tva_deduc = f["invest_tva"]
        dec = f["invest_ttc"]
        enc = 0.0
        if t >= 0:
            y, mc = mois_cal(H, t)
            units = mix_mois(H, mc, scen)
            if sans_signature:
                units = {k: v for k, v in units.items() if k != "signature"}
            tk = ticket(H, units, P)
            tj = sc["tickets_jour_croisiere"] * (rampe[t] if t < len(rampe) else 1.0) * saison[str(mc)] * volume_mult
            nb = tj * jours
            row.update({"y": y, "m": mc, "tickets_jour": tj, "ticket_ttc": tk["ttc"], "ca_ht": nb * tk["ht"],
                        "ca_ttc": nb * tk["ttc"], "var": nb * tk["var"], "contrib": nb * tk["contrib"],
                        "safran_g": nb * tk["safran_g"]})
            fixe = cf["total"] + (pers["fond_valorisation"] if valoriser else 0.0)
            row["fixe"] = fixe
            row["ebitda"] = row["contrib"] - fixe
            row["amort"] = amort_mois
            row["resultat"] = row["ebitda"] - amort_mois
            tva_collectee = row["ca_ttc"] - row["ca_ht"]
            var_hors_cb = nb * (tk["var"] - tk["cb"])
            tva_var = var_hors_cb * 0.10
            tva_deduc += tva_var + fixe_tva + cf["marketing"] * 0.20
            enc = row["ca_ttc"]
            dec += var_hors_cb + tva_var + nb * tk["cb"] + cf["hors_personnel"] + fixe_tva + pers["total"] + \
                cf["marketing"] * 1.20
            if valoriser:
                dec += pers["fond_valorisation"]
            cum_op += enc - (var_hors_cb + tva_var + nb * tk["cb"] + cf["hors_personnel"] + fixe_tva + pers["total"]
                             + cf["marketing"] * 1.20 + (pers["fond_valorisation"] if valoriser else 0))
        # TVA : solde du mois payé (ou crédit remboursé) plus tard
        solde = tva_collectee - tva_deduc
        row["tva_solde"] = solde
        if solde >= 0:
            imput = min(credit_tva, solde)
            credit_tva -= imput
            paye = solde - imput
            if t + 1 in flux:
                flux[t + 1]["tva_nette"] -= paye
        else:
            credit_tva += -solde
        # demande de remboursement du crédit chaque mois, reçue après le délai
        if credit_tva > 0 and t >= 0:
            remb[t + delai] = remb.get(t + delai, 0.0) + credit_tva
            credit_tva = 0.0
        tva_cash = f["tva_nette"] + remb.get(t, 0.0)
        net = enc - dec + tva_cash
        cum += net
        if cum < cum_min:
            cum_min = cum
            t_min = t
        cum_op_min = min(cum_op_min, cum_op)
        row.update({"enc": enc, "dec": dec, "tva_cash": tva_cash, "net": net, "cum": cum, "cum_op": cum_op})
        rows.append(row)
    op = [r for r in rows if 0 <= r["t"] < 12]
    op2 = [r for r in rows if 12 <= r["t"] < 24]
    cles = ("ca_ht", "ca_ttc", "var", "contrib", "fixe", "ebitda", "amort", "resultat", "safran_g")
    an = {k: sum(r[k] for r in op) for k in cles}
    an2 = {k: sum(r[k] for r in op2) for k in cles}
    derniers = [r["cum"] for r in rows[-3:]]
    stabilise = not (rows[-1]["cum"] <= min(r["cum"] for r in rows) + 1e-6 and derniers[-1] < derniers[0])
    return {"rows": rows, "annee": an, "annee2": an2, "stabilise": stabilise, "cum_fin": rows[-1]["cum"],
            "besoin_max": -cum_min, "mois_besoin_max": t_min,
            "deficit_exploitation_max": -cum_op_min, "depot": depot, "immob": sum(v for v, _ in immob),
            "charges_pre": charges_pre, "stock": stock, "amort_mois": amort_mois, "cf": cf,
            "invest_ht": sum((it[invest_cle] if invest_cle in it else it["ht"]) for it in inv),
            "invest_ttc": sum(flux[t]["invest_ttc"] for t in T),
            "credit_restant": credit_tva + sum(v for k, v in remb.items() if k >= mois)}


def financement(H, sim, reserve_taux=None):
    """Décomposition du besoin au mois le plus bas, sans double compte."""
    inv = H["investissement"]
    taux = H["reserve_aleas"]["taux"] if reserve_taux is None else reserve_taux
    pre_ht = sum(it["ht"] for it in inv if it["nature"] != "stock")
    stock_ht = sum(it["ht"] for it in inv if it["nature"] == "stock")
    base_reserve = sum(it["ht"] for it in inv if it["nature"] not in ("depot", "stock"))
    reserve = base_reserve * taux
    tmin = sim["mois_besoin_max"]
    tva_avancee = 0.0
    rows = sim["rows"]
    # TVA payée sur investissements et non encore récupérée au mois le plus bas
    inv_tva_payee = sum(r_tva for r_tva in [it["ht"] * it["tva"] for it in inv])
    recup = sum(r["tva_cash"] for r in rows if r["t"] <= tmin and r["tva_cash"] > 0)
    tva_avancee = max(0.0, inv_tva_payee - recup)
    besoin = sim["besoin_max"]
    exploitation = besoin - pre_ht - stock_ht - tva_avancee
    return {"pre_ht": pre_ht, "stock": stock_ht, "tva_avancee": tva_avancee, "exploitation": exploitation,
            "reserve": reserve, "total": besoin + reserve, "besoin_sim": besoin, "mois": tmin}


# ── rapports ────────────────────────────────────────────────────────────────────
def rapport_produits(H):
    P = table_produits(H)
    L = ["# Coût et marge par produit — La Saffranerie", "",
         "Généré par `founder/modele/saffranerie.py` à partir de `founder/modele/hypotheses.json` (%s)." % H["version"],
         "Prix TTC proposés ; HT calculé avec la TVA sur place / à emporter et la part consommée sur place ; "
         "safran au prix de cession (%s/g) ; crème au coût %s (%s/kg, mode « %s »). Pertes = %% des matières. "
         "Carte bancaire = %s du TTC." % (e(H["safran"]["prix_cession_g"], 2), "complet", e(creme_cout_kg(H), 2),
                                         H["creme"]["mode_retenu"], pc(H["taux_cb"], 1)), "",
         "Statuts : ouverture, saison (avril–septembre), ouverture_si_test (signature : seulement si le test de faisabilité est concluant), report (après preuve de demande et faisabilité de la cuisson), retire (non recommandé).", "",
         "| produit | statut | prix TTC | HT moyen | matières | safran | crème | emballage | pertes | carte | coût variable | marge € | marge % |",
         "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for c in CATS:
        for r in P.values():
            if r["cat"] != c:
                continue
            L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                r["nom"], r["statut"], e(r["ttc"], 2), e(r["ht"], 2), e(r["mat"], 2), e(r["saf"], 2), e(r["cre"], 2),
                e(r["emb"], 2), e(r["perte"], 2), e(r["cb"], 2), e(r["var"], 2), e(r["marge"], 2), pc(r["marge_pct"])))
    L += ["", "Coût de la crème au safran selon le mode de production (€/kg, hors pot) :", ""]
    for mode in H["creme"]["modes"]:
        L.append("- %s : %s/kg (%s)" % (mode, e(creme_cout_kg(H, mode), 2), H["creme"]["modes"][mode]["source"]))
    return "\n".join(L) + "\n"


def rapport_cfo(H):
    L = []
    P = table_produits(H)
    t = ticket_annuel(H, "central")
    pm = point_mort(H, "central", t=t)
    cap = capacite(H, t)
    L += ["# Modèle financier détaillé — La Saffranerie", "",
          "Version des hypothèses : **%s**. Généré par `founder/modele/saffranerie.py`. Montants HT sauf mention. "
          "Ouverture **hypothétique** le %s." % (H["version"], H["calendrier"]["ouverture_hypothetique"]), ""]
    # 1. ticket moyen
    L += ["## 1. Ticket moyen pondéré (scénario central, moyenne annuelle pondérée par la saison)", "",
          "| catégorie | unités pour 100 tickets | CA HT par ticket | part du CA HT |", "| --- | ---: | ---: | ---: |"]
    for c in CATS:
        L.append("| %s | %s | %s | %s |" % (NOM_CAT[c], n(t["cat_units"][c] * 100, 1), e(t["cat_ht"][c], 2),
                                          pc(t["cat_ht"][c] / t["ht"])))
    L += ["| **Total** | **%s articles** | **%s** | 100 %% |" % (n(t["items"] * 100, 0), e(t["ht"], 2)), "",
          "- Ticket moyen : **%s TTC**, %s HT, coût variable %s (dont carte %s), **contribution %s par ticket (%s du HT)**." % (
              e(t["ttc"], 2), e(t["ht"], 2), e(t["var"], 2), e(t["cb"], 2), e(t["contrib"], 2), pc(t["contrib_pct"])),
          "- Safran consommé : %s g par ticket en moyenne." % n(t["safran_g"], 3), ""]
    # 2. charges fixes
    cf = pm["ticket"] and charges_fixes(H)
    L += ["## 2. Charges fixes mensuelles (central, planning « %s »)" % H["personnel"]["planning_retenu"], "",
          "| poste | € HT / mois | statut |", "| --- | ---: | --- |"]
    for lab, v, _, st in cf["lignes"]:
        L.append("| %s | %s | %s |" % (lab, e(v), st))
    for lab, v, h in cf["personnel"]["lignes"]:
        L.append("| Personnel : %s | %s | indispensable |" % (lab, e(v)))
    L.append("| Provision absences, congés, dimanches et fériés | %s | indispensable |" % e(cf["personnel"]["provision"]))
    L.append("| Communication mensuelle (budget B) | %s | indispensable |" % e(cf["marketing"]))
    L += ["| **Total charges fixes décaissées** | **%s** | |" % e(cf["total"]), "",
          "- Travail des fondateurs non rémunéré dans ce planning : %s h/semaine, valorisé à %s/mois au coût d'un responsable de boutique." % (
              n(cf["personnel"]["fond_h"]), e(cf["personnel"]["fond_valorisation"])),
          "- CFE non comptée en année 1 (exonération l'année de création, à confirmer) ; amortissements hors charges fixes décaissées.", ""]
    # 3. point mort
    pmv = point_mort(H, "central", valoriser=True, t=t)
    pms = point_mort(H, "central", t=ticket_annuel_avec_signature(H))
    L += ["## 3. Point mort (scénario central)", "",
          "| | sans valoriser les fondateurs | en valorisant le travail des fondateurs | avec la boisson signature (si test réussi) |",
          "| --- | ---: | ---: | ---: |",
          "| Charges fixes / mois | %s | %s | %s |" % (e(pm["fixe"]), e(pmv["fixe"]), e(pms["fixe"])),
          "| CA HT / mois | %s | %s | %s |" % (e(pm["ca_ht_mois"]), e(pmv["ca_ht_mois"]), e(pms["ca_ht_mois"])),
          "| CA TTC / mois (équivalent) | %s | %s | %s |" % (e(pm["ca_ttc_mois"]), e(pmv["ca_ttc_mois"]), e(pms["ca_ttc_mois"])),
          "| CA TTC / jour | %s | %s | %s |" % (e(pm["ca_ttc_jour"]), e(pmv["ca_ttc_jour"]), e(pms["ca_ttc_jour"])),
          "| **Tickets / jour** | **%s** | **%s** | **%s** |" % (n(math.ceil(pm["tickets_jour"])), n(math.ceil(pmv["tickets_jour"])), n(math.ceil(pms["tickets_jour"]))),
          "| Tickets / heure d'ouverture (moyenne) | %s | %s | %s |" % (n(pm["par_heure"], 1), n(pmv["par_heure"], 1), n(pms["par_heure"], 1)),
          "| Tickets à l'heure de pointe (%s du jour) | %s | %s | %s |" % (pc(H["horaires"]["part_ventes_heure_pointe"]), n(pm["pointe"], 1), n(pmv["pointe"], 1), n(pms["pointe"], 1)),
          ""]
    L += ["Produits vendus par jour au point mort (sans valorisation) :", ""]
    for c in CATS:
        L.append("- %s : %s" % (NOM_CAT[c], n(pm["cat_jour"][c], 1)))
    L += ["", "## 4. Capacité de service", "",
          "- Temps de service moyen par ticket (préparation + conseil + encaissement) : %s s." % n(cap["sec_ticket"]),
          "- Une personne seule : **%s tickets/heure** au rythme soutenable (%s d'utilisation) ; deux personnes : **%s tickets/heure**." % (
              n(cap["une_personne_h"], 1), pc(H["capacite"]["utilisation"]), n(cap["deux_personnes_h"], 1)),
          "- Capacité journalière avec le planning retenu (renfort %s h/semaine) : **≈ %s tickets/jour**." % (
              n(H["horaires"]["renfort_poste2_semaine"]), n(cap["jour"])),
          "- Point mort à l'heure de pointe : %s tickets, contre %s pour une personne seule : %s." % (
              n(pm["pointe"], 1), n(cap["une_personne_h"], 1),
              "**une personne seule ne suffit pas aux pointes**" if pm["pointe"] > cap["une_personne_h"] else "une personne seule suffit en théorie, sans marge pour le conseil safran"), ""]
    # 5. scénarios
    L += ["## 5. Trois scénarios — première année (planning retenu, communication B)", "",
          "| | prudent | central | favorable |", "| --- | ---: | ---: | ---: |"]
    sims = {s: simulation(H, s) for s in ("prudent", "central", "favorable")}
    simv = {s: simulation(H, s, valoriser=True) for s in ("prudent", "central", "favorable")}
    fins = {s: financement(H, sims[s]) for s in sims}

    def row(lab, f):
        L.append("| %s | %s |" % (lab, " | ".join(f(s) for s in ("prudent", "central", "favorable"))))
    row("Tickets/jour en croisière (hypothèse)", lambda s: n(H["scenarios"][s]["tickets_jour_croisiere"]))
    row("Tickets/jour moyens sur l'année 1", lambda s: n(sum(r["tickets_jour"] for r in sims[s]["rows"] if 0 <= r["t"] < 12) / 12))
    row("Ticket moyen TTC (annuel)", lambda s: e(ticket_annuel(H, s)["ttc"], 2))
    row("CA HT année 1", lambda s: e(sims[s]["annee"]["ca_ht"]))
    row("Marge sur coûts variables", lambda s: e(sims[s]["annee"]["contrib"]))
    row("Charges fixes décaissées", lambda s: e(sims[s]["annee"]["fixe"]))
    row("**EBE année 1 (fondateurs non payés)**", lambda s: "**%s**" % e(sims[s]["annee"]["ebitda"]))
    row("Amortissements", lambda s: e(sims[s]["annee"]["amort"]))
    row("Résultat d'exploitation", lambda s: e(sims[s]["annee"]["resultat"]))
    row("**EBE en valorisant le travail des fondateurs**", lambda s: "**%s**" % e(simv[s]["annee"]["ebitda"]))
    row("Point mort tickets/jour (fondateurs non payés)", lambda s: n(math.ceil(point_mort(H, s)["tickets_jour"])))
    row("Point mort tickets/jour (fondateurs valorisés)", lambda s: n(math.ceil(point_mort(H, s, valoriser=True)["tickets_jour"])))
    row("EBE année 2 (croisière, fondateurs non payés)", lambda s: e(sims[s]["annee2"]["ebitda"]))
    row("EBE année 2 en valorisant les fondateurs", lambda s: e(simv[s]["annee2"]["ebitda"]))
    row("Besoin de trésorerie maximal sur 24 mois (hors réserve)", lambda s: e(sims[s]["besoin_max"]) + ("" if sims[s]["stabilise"] else " **et toujours en baisse au mois 24**"))
    row("Mois du creux", lambda s: mois_label(H, sims[s]["mois_besoin_max"]))
    row("**Financement minimum avec réserve**", lambda s: "**%s**" % e(fins[s]["total"]))
    L.append("")
    # 6. mois par mois central
    L += ["## 6. Première année mois par mois — scénario central", "",
          "| mois | tickets/j | ticket TTC | CA HT | marge s/ coûts var. | charges fixes | EBE | résultat | TVA (flux) | flux de trésorerie | trésorerie cumulée |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for r in [x for x in sims["central"]["rows"] if x["t"] < 12]:
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            mois_label(H, r["t"]), n(r["tickets_jour"]), e(r.get("ticket_ttc", 0), 2) if r["t"] >= 0 else "—",
            e(r["ca_ht"]), e(r["contrib"]), e(r["fixe"]), e(r["ebitda"]), e(r["resultat"]), e(r["tva_cash"]),
            e(r["net"]), e(r["cum"])))
    L += ["", "Les mois avant l'ouverture portent les investissements TTC ; la TVA récupérable revient avec un délai de %s mois (hypothèse)." % H["tva"]["delai_remboursement_credit_mois"], ""]
    # 7. financement
    f = fins["central"]
    sim = sims["central"]
    L += ["## 7. Financement minimum — scénario central", "",
          "| bloc | montant | contenu |", "| --- | ---: | --- |",
          "| 1. Dépenses et engagements avant ouverture (HT) | %s | dépôt de garantie %s (récupérable en fin de bail), honoraires, travaux, équipements, loyers pendant travaux, marque, crème, lancement |" % (e(f["pre_ht"]), e(sim["depot"])),
          "| 2. Stock initial et TVA avancée non encore remboursée au creux | %s | stock %s + TVA avancée %s |" % (e(f["stock"] + f["tva_avancee"]), e(f["stock"]), e(f["tva_avancee"])),
          "| 3. Pertes d'exploitation cumulées jusqu'au creux (montée en puissance) | %s | %s |" % (e(f["exploitation"]), "creux en " + mois_label(H, f["mois"])),
          "| = Besoin maximal simulé | %s | |" % e(f["besoin_sim"]),
          "| 4. Réserve pour aléas (%s des investissements hors dépôt et stock) | %s | travaux et équipements dans un local non visité |" % (pc(H["reserve_aleas"]["taux"]), e(f["reserve"])),
          "| **Total à mobiliser** | **%s** | |" % e(f["total"]), ""]
    # 8. sensibilités
    L += ["## 8. Sensibilités (scénario central, une variable à la fois)", "",
          "| variable | point mort tickets/j | EBE année 1 | besoin + réserve |", "| --- | ---: | ---: | ---: |"]
    for lab, Hx, kw in sensibilites(H):
        s2 = simulation(Hx, "central", **kw)
        f2 = financement(Hx, s2)
        pm2 = point_mort(Hx, "central", planning=kw.get("planning"), marketing=kw.get("marketing_mensuel"),
                         valoriser=kw.get("valoriser", False),
                         t=ticket_annuel_sans_signature(Hx) if kw.get("sans_signature") else None)
        L.append("| %s | %s | %s | %s |" % (lab, n(math.ceil(pm2["tickets_jour"])), e(s2["annee"]["ebitda"]), e(f2["total"])))
    L.append("")
    # 9. groupe
    sim = sims["central"]
    g = sim["annee"]["safran_g"]
    oc = g * (H["safran"]["prix_cession_g"] - H["safran"]["cout_achat_oc_g"])
    L += ["## 9. Vue groupe (Olympus Croci + filiale), sans double compte", "",
          "- Safran consommé ou vendu par la boutique en année 1 (central) : **%s g** (%s kg)." % (n(g), n(g / 1000, 2)),
          "- Marge d'Olympus Croci sur ce safran au prix de cession de %s/g (coût %s/g) : **%s**. Elle s'ajoute à l'EBE de la boutique (%s) pour la vue consolidée : %s." % (
              e(H["safran"]["prix_cession_g"], 2), e(H["safran"]["cout_achat_oc_g"], 2), e(oc),
              e(sim["annee"]["ebitda"]), e(sim["annee"]["ebitda"] + oc)),
          "- Le capital apporté par Olympus Croci est compté une seule fois, comme ressource de la filiale. La marge interne ne crée pas de trésorerie pour le groupe : elle déplace la marge d'une société à l'autre.", ""]
    return "\n".join(L) + "\n", sims, fins


def ticket_annuel_sans_signature(H):
    Hx = copy.deepcopy(H)
    Hx["mix_pour_100_tickets"]["permanent"].pop("signature", None)
    return ticket_annuel(Hx, "central")


def avec_signature(h):
    h["mix_pour_100_tickets"]["permanent"]["signature"] = 8
    h["mix_pour_100_tickets"]["permanent"]["latte_safran"] = max(0, h["mix_pour_100_tickets"]["permanent"]["latte_safran"] - 4)


def ticket_annuel_avec_signature(H):
    Hx = copy.deepcopy(H)
    avec_signature(Hx)
    return ticket_annuel(Hx, "central")


def mois_label(H, t):
    y, m = mois_cal(H, t)
    return "%s %d" % (NOMS_MOIS[m - 1], y)


def sensibilites(H):
    out = []

    def var(lab, fn, **kw):
        Hx = copy.deepcopy(H)
        fn(Hx)
        out.append((lab, Hx, kw))
    var("Base centrale", lambda h: None)
    var("Prix de tous les produits −10 %", lambda h: [p.__setitem__("prix_ttc", p["prix_ttc"] * 0.9) for p in h["produits"]])
    var("Prix de tous les produits +10 %", lambda h: [p.__setitem__("prix_ttc", p["prix_ttc"] * 1.1) for p in h["produits"]])
    var("Volume −20 %", lambda h: None, volume_mult=0.8)
    var("Volume +20 %", lambda h: None, volume_mult=1.2)
    var("Coût de la crème +30 %", lambda h: [f.__setitem__("cout_kg", f["cout_kg"] * 1.3) for f in h["creme"]["formule_hypothese"]] or h["creme"]["modes"]["faconnier"].__setitem__("facon_kg", h["creme"]["modes"]["faconnier"]["facon_kg"] * 1.3))
    var("Crème produite en interne", lambda h: h["creme"].__setitem__("mode_retenu", "interne"))
    var("Pertes doublées", lambda h: [p.__setitem__("perte", p["perte"] * 2) for p in h["produits"]])
    var("Safran cédé à 6 €/g", lambda h: h["safran"].__setitem__("prix_cession_g", 6.0))
    var("Safran cédé à 12 €/g", lambda h: h["safran"].__setitem__("prix_cession_g", 12.0))
    var("Avec la boisson signature (si test réussi)", avec_signature)
    var("Planning S1 (intention : 1 salarié + fondateurs) — NON TENABLE, voir ops", lambda h: None, planning="S1_intention")
    var("Planning S3 (exploitation autonome)", lambda h: None, planning="S3_autonome")
    var("Fondateurs valorisés (S2)", lambda h: None, valoriser=True)
    var("Loyer −25 % (autre local, ≈ 5 000 €)", lambda h: h["charges_fixes"][0].__setitem__("central", 5000.0))
    var("Loyer +12,5 % (7 500 €, comme les annonces voisines)", lambda h: h["charges_fixes"][0].__setitem__("central", 7500.0))
    var("Charges fixes hors personnel au maximum de fourchette", lambda h: [c.__setitem__("central", c["max"]) for c in h["charges_fixes"]])
    var("Communication 3B (mensuel ×3, lancement ×3)", lambda h: None, marketing_mensuel=H["marketing"]["B_mensuel"] * 3, lancement=H["marketing"]["B_lancement"] * 3)
    var("Communication 10B (mensuel ×10, lancement ×10)", lambda h: None, marketing_mensuel=H["marketing"]["B_mensuel"] * 10, lancement=H["marketing"]["B_lancement"] * 10)
    var("Droit au bail 50 000 €", lambda h: [i.__setitem__("ht", 50000) for i in h["investissement"] if i["label"].startswith("Droit au bail")])
    var("Droit au bail 100 000 €", lambda h: [i.__setitem__("ht", 100000) for i in h["investissement"] if i["label"].startswith("Droit au bail")])
    var("Travaux au maximum (95 000 €)", lambda h: [i.__setitem__("ht", i["max"]) for i in h["investissement"] if i["label"].startswith("Travaux")])
    var("Pas d'agence (honoraires 0 €)", lambda h: [i.__setitem__("ht", 0) for i in h["investissement"] if i["label"].startswith("Honoraires")])
    var("Franchise de loyer pendant les travaux", lambda h: [i.__setitem__("ht", 0) for i in h["investissement"] if i["label"].startswith("Loyer et charges pendant")])
    return out


def numbers_json(H):
    """Entrée pour unit_economics.py (skill founder-cfo) : unité = ticket, scénario central, planning retenu."""
    t = ticket_annuel(H, "central")
    cf = charges_fixes(H)
    sim = simulation(H, "central")
    cap = capacite(H, t)
    variable = [{"label": "Matières, safran (prix de cession) et crème", "cost": round(t["mat_emb_perte"] * 0.80, 4)},
                {"label": "Emballages et pertes", "cost": round(t["mat_emb_perte"] * 0.20, 4)},
                {"label": "Commissions carte", "cost": round(t["cb"], 4)}]
    # répartition matières/emballages+pertes calculée précisément
    P = table_produits(H)
    mat = embp = 0.0
    w = H["saisonnalite_calendaire"]
    tot = sum(w.values())
    for m in range(1, 13):
        u = mix_mois(H, m, "central")
        for k, q in u.items():
            r = P[k]
            mat += w[str(m)] / tot * q / 100 * (r["mat"] + r["saf"] + r["cre"])
            embp += w[str(m)] / tot * q / 100 * (r["emb"] + r["perte"])
    variable = [{"label": "Matières, safran (prix de cession) et crème", "cost": round(mat, 4)},
                {"label": "Emballages et pertes", "cost": round(embp, 4)},
                {"label": "Commissions carte", "cost": round(t["cb"], 4)}]
    fixed = [{"label": lab, "cost": round(v, 2)} for lab, v, _, _ in cf["lignes"]]
    fixed += [{"label": "Personnel (%s)" % H["personnel"]["planning_retenu"], "cost": round(cf["personnel"]["total"], 2)},
              {"label": "Communication mensuelle (B)", "cost": round(cf["marketing"], 2)}]
    startup = [{"label": it["label"], "cost": it["ht"]} for it in H["investissement"] if it["ht"]]
    ramp = [round(r["tickets_jour"], 1) for r in sim["rows"] if r["t"] >= 0]
    return {"business": "La Saffranerie (rue du Dragon) — unité = ticket moyen, montants HT en euros",
            "unit": "ticket", "price": round(t["ht"], 4), "variable": variable, "fixed_monthly": fixed,
            "startup": startup, "days_per_month": H["calendrier"]["jours_par_mois"],
            "capacity_per_day": int(cap["jour"]), "plan_per_day": H["scenarios"]["central"]["tickets_jour_croisiere"],
            "ramp_per_day": ramp,
            "_note": "Généré par founder/modele/saffranerie.py (%s). L'outil compte les montants en '$' : ce sont des euros HT. "
                     "Les montants de 'startup' sont HT ; le dépôt de garantie est récupérable." % H["version"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hyp", default=os.path.join(ICI, "hypotheses.json"))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    H = json.load(open(a.hyp, encoding="utf-8"))
    os.makedirs(SORTIES, exist_ok=True)
    open(os.path.join(SORTIES, "produits.md"), "w", encoding="utf-8").write(rapport_produits(H))
    txt, sims, fins = rapport_cfo(H)
    open(os.path.join(SORTIES, "cfo-modele.md"), "w", encoding="utf-8").write(txt)
    nj = numbers_json(H)
    json.dump(nj, open(os.path.join(ICI, "..", "numbers.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    t = ticket_annuel(H, "central")
    pm = point_mort(H, "central", t=t)
    res = {"ticket_ttc": t["ttc"], "ticket_ht": t["ht"], "contrib": t["contrib"], "contrib_pct": t["contrib_pct"],
           "point_mort_tickets": pm["tickets_jour"], "fixe": pm["fixe"],
           "point_mort_valorise": point_mort(H, "central", valoriser=True, t=t)["tickets_jour"],
           "capacite_jour": capacite(H, t)["jour"],
           "scenarios": {s: {"ebitda": sims[s]["annee"]["ebitda"], "ca_ht": sims[s]["annee"]["ca_ht"],
                             "besoin": sims[s]["besoin_max"], "financement": fins[s]["total"]} for s in sims}}
    json.dump(res, open(os.path.join(SORTIES, "resultats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
