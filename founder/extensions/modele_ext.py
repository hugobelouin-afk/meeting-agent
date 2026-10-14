#!/usr/bin/env python3
"""Étude complémentaire « extensions » de La Saffranerie : scénarios S0 à S6.

    python3 founder/extensions/modele_ext.py

La référence S0 est le modèle v2 de l'étude initiale : ce script importe
founder/modele/saffranerie.py et lit founder/modele/hypotheses.json sans les
modifier. Les hypothèses propres aux extensions sont dans hypotheses_ext.json.

Méthode (montants HT sauf mention ; scénario central sauf mention) :
  1. le mois t du scénario S0 donne les tickets/jour de base (rampe et saison comprises) ;
  2. chaque extension ajoute des achats complémentaires (unités pour 100 tickets de base),
     des visites supplémentaires (nouveaux clients ou visites plus fréquentes), retire la
     contribution des ventes qu'elle remplace (substitution) et, pour la glace, les ventes
     de glace de S0 qu'elle remplace ;
  3. quand plusieurs familles de desserts coexistent, un chevauchement réduit leurs ventes
     (mêmes clients, même appétit, même budget) : les hausses ne s'additionnent pas ;
  4. les invendus dépendent du mode d'approvisionnement : taux fixe, rotation par
     référence (quantité livrée = max(demande du cycle + présentation, minimum)) ou bacs ;
  5. charges fixes ajoutées : énergie, maintenance, renforts, heures de production,
     salarié dédié ; temps des fondateurs valorisé à part ; amortissement sur 5 ans ;
  6. la trésorerie et la TVA des extensions s'ajoutent mois par mois à celles de S0.
"""

import copy
import json
import math
import os
import sys

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
MODELE = os.path.normpath(os.path.join(ICI, "..", "modele"))
sys.path.insert(0, MODELE)
import saffranerie as S  # noqa: E402
from saffranerie import e, n, pc  # noqa: E402

SORTIES = os.path.join(ICI, "sorties")
CAS = ("prudent", "central", "favorable")
TVA_ACHATS = 0.055      # pâtisseries, glaces, plats achetés à un fournisseur (taux du bien, à confirmer)
TVA_EMB = 0.20
TVA_VAR_S0 = 0.10       # convention du modèle S0 pour ses achats variables
ORDRE = ["S0", "S1", "S1c", "S2", "S2a", "S2b", "S3", "S4", "S4p", "S5", "S5T", "S6"]


# ── chargement ──────────────────────────────────────────────────────────────────
def charger():
    with open(os.path.join(MODELE, "hypotheses.json"), encoding="utf-8") as f:
        H = json.load(f)
    with open(os.path.join(ICI, "hypotheses_ext.json"), encoding="utf-8") as f:
        X = json.load(f)
    resoudre(X)
    return H, X


def resoudre(X):
    E = X["extensions"]
    for x in E.values():
        for champ in ("produits", "substitution", "saison"):
            if isinstance(x.get(champ), str):
                x[champ] = copy.deepcopy(E[x[champ]][champ])


def modifier(X, modifs):
    """Copie de X avec des valeurs remplacées : 'extension.champ.sous_champ' ; un produit se désigne par son id."""
    Y = copy.deepcopy(X)
    for chemin, v in modifs.items():
        cles = chemin.split(".")
        d = Y if cles[0] in Y else Y["extensions"]
        for c in cles[:-1]:
            d = next(p for p in d if p["id"] == c) if isinstance(d, list) else d[c]
        d[cles[-1]] = copy.deepcopy(v)
    return Y


# ── économie unitaire ───────────────────────────────────────────────────────────
def eco(p, H):
    ttc = p["prix_ttc"]
    ht = p["part_sp"] * ttc / (1 + p["tva_sp"]) + (1 - p["part_sp"]) * ttc / (1 + p["tva_emp"])
    emb = p["part_sp"] * p["emb_sp"] + (1 - p["part_sp"]) * p["emb_emp"]
    cb = ttc * H["taux_cb"]
    var = p["cout"] + emb + cb
    return {"ttc": ttc, "ht": ht, "cout": p["cout"], "emb": emb, "cb": cb, "var": var, "contrib": ht - var,
            "pct": (ht - var) / ht}


def invendus(x, units, prods, ctx):
    """(coût HT des invendus par jour, pièces perdues par jour, pièces produites par jour)."""
    P = x["pertes"]
    mult = ctx.get("pertes_mult", 1.0)
    moq = ctx.get("moq_mult", 1.0)
    if P["mode"] == "taux":
        c = sum(units[k] * prods[k]["cout"] * r / (1 - r) for k, r in P["taux"].items() if k in units)
        pcs = sum(units[k] * prods[k].get("pieces", 1) * r / (1 - r) for k, r in P["taux"].items() if k in units)
        vendues = sum(units[k] * prods[k].get("pieces", 1) for k in units)
        return c * mult, pcs * mult, vendues + pcs * mult
    excl = set(P.get("sans_perte", []))
    if P["mode"] == "rotation":
        pieces = sum(units[k] * prods[k].get("pieces", 1) for k in units if k not in excl)
        if pieces <= 1e-9:
            return 0.0, 0.0, 0.0
        cp = sum(units[k] * prods[k]["cout"] for k in units if k not in excl) / pieces
        N, cyc = P["references"], P["cycle_j"]
        d = pieces / N * cyc
        if P["vie_j"] >= 2 * cyc:   # le reste d'un cycle se vend au cycle suivant
            w = P["taux_base"] * d
        else:                        # le reste en fin de cycle est perdu
            q = max(d + P["presentation_min"], P["minimum_par_reference"] * moq)
            w = q - d + P["taux_base"] * d
        wj = N * w / cyc * mult
        return wj * cp, wj, pieces + wj
    if P["mode"] == "bacs":
        boules = sum(units[k] * prods[k].get("boules", 1) for k in units)
        if boules <= 1e-9:
            return 0.0, 0.0, 0.0
        cb_ = sum(units[k] * prods[k]["cout"] for k in units) / boules
        N, B = P["references"], P["boules_par_bac"] * moq
        d = boules / N
        vend = min(B, d * P["vie_j"])
        w = (B - vend) * d / vend + P["taux_base"] * d
        wj = N * w * mult
        return wj * cb_, wj, boules + wj
    raise ValueError(P["mode"])


# ── une extension, un mois ──────────────────────────────────────────────────────
CHAMPS = ("ht", "ttc", "contrib", "achats", "emb", "cb", "var_base", "var_moins", "fixe", "fixe_tva", "personnel",
          "fond", "pertes", "pertes_pcs", "produites", "nouv", "sec", "sec_pointe", "h_sal", "c_nouv", "c_att",
          "c_sub", "c_rem", "ca_ext_ttc", "u_att", "u_sub", "u_rem", "u_nouv", "nouv_freq")


def cout_horaire(H, X, fx):
    G = X["global"]
    prov = 1 + H["personnel"]["plannings"][H["personnel"]["planning_retenu"]]["provision"]
    renfort = G["taux_horaire_renfort"] * G["ratio_cout_renfort"] * prov
    prod = G["cout_horaire_production_qualifie"] * prov if fx.get("cout_horaire") == "qualifie" else renfort
    return renfort, prod, prov


def delta_ext(H, X, cle, t, mc, T, tk, ctx):
    """Effet journalier (flux) et mensuel (charges fixes) d'une extension pour le mois calendaire mc."""
    x = X["extensions"][cle]
    G = X["global"]
    fx = x["fixes"]
    jours = H["calendrier"]["jours_par_mois"]
    d = {k: 0.0 for k in CHAMPS}
    d["units"] = {}
    actif = (mc in x["saison_seule"]) if x.get("saison_seule") else True
    c_r, c_p, prov = cout_horaire(H, X, fx)
    rm = ctx.get("renfort_mult", 1.0)
    hr = fx.get("renfort_h_semaine", 0) * rm if actif else 0.0
    hp = fx.get("production_h_semaine", 0) * rm if actif else 0.0
    sal = fx.get("salarie_mois", 0) * prov if actif else 0.0
    energie = fx["kwh_jour"] * G["prix_kwh"] * jours if actif else 0.0
    autres = fx.get("maintenance_mois", 0) + fx.get("dechets_mois", 0)
    d["personnel"] = (hr * c_r + hp * c_p) * 52 / 12 + sal
    d["fixe"] = d["personnel"] + energie + autres
    d["fixe_tva"] = (energie + autres) * 0.20
    d["h_sal"] = hr + hp + (35 if sal else 0)
    d["fond"] = fx.get("fondateur_h_semaine", 0) * 52 / 12 * G["cout_horaire_fondateur"] if actif else 0.0
    if not actif:
        return d
    s = x["saison"].get(str(mc), 1.0)
    if ctx.get("saison_plate"):
        s = 1.0
    f_ch = 1.0 - ctx["chev"] if x["famille_dessert"] else 1.0
    rampe = H["montee_en_puissance"]
    r_t = rampe[t] if t < len(rampe) else 1.0
    dem = ctx["dem"] * ctx.get("dem_ext", {}).get(cle, 1.0)
    prods = {p["id"]: p for p in x["produits"]}
    if ctx.get("prix_mult") or ctx.get("cout_mult"):
        prods = copy.deepcopy(prods)
        for p in prods.values():
            p["prix_ttc"] *= ctx.get("prix_mult", 1.0)
            p["cout"] *= ctx.get("cout_mult", 1.0)
    E = {k: eco(p, H) for k, p in prods.items()}
    att = {k: T * x["attache_pour_100"].get(k, 0) / 100.0 * s * dem * f_ch for k in prods}
    nouv = 0.0 if ctx.get("sans_nouveaux") else x["nouveaux_tickets_jour"] * r_t * s * dem * f_ch
    pn = x["panier_nouveaux"]
    un_n = {k: nouv * pn.get(k, 0) for k in prods}
    units = {k: att[k] + un_n[k] for k in prods}
    d["units"] = units
    d["nouv"] = nouv
    d["nouv_freq"] = nouv * x.get("part_frequence", 0.0)
    d["u_att"] = sum(att.values())
    d["u_nouv"] = sum(un_n.values())
    # ventes de glace de S0 remplacées
    rem_u = rem_c = rem_ht = rem_ttc = rem_sec = 0.0
    if x.get("remplace_s0"):
        mix = S.mix_mois(H, mc, ctx["scen"])
        for k in x["remplace_s0"]:
            q = T * mix.get(k, 0) / 100.0
            r0 = ctx["P0"][k]
            rem_u += q
            rem_c += q * r0["marge"]
            rem_ht += q * r0["ht"]
            rem_ttc += q * r0["ttc"]
            rem_sec += q * r0["temps_s"]
    att_tot = sum(att.values())
    part_incr = 1.0
    if rem_u > 0 and att_tot > 0:
        part_incr = max(0.0, att_tot - rem_u) / att_tot
    # substitution : contribution perdue sur les ventes existantes remplacées
    pct0 = ctx["pct0"]
    sub_c = 0.0
    for k in prods:
        if ctx.get("sub_totale"):
            sub_c += att[k] * part_incr * E[k]["ht"] * pct0
        else:
            part, perdu = x["substitution"].get(k, [0.0, 0.0])
            sub_c += att[k] * part_incr * part * perdu
    d["u_sub"] = sum(att[k] * part_incr * (1.0 if ctx.get("sub_totale") else x["substitution"].get(k, [0.0, 0.0])[0])
                     for k in prods)
    d["u_rem"] = rem_u
    sub_ht = sub_c / pct0
    sub_ttc = sub_ht * tk["ttc"] / tk["ht"]
    # part de ticket de base achetée par les visites supplémentaires
    tb = pn.get("_ticket_base", 0.0) * nouv
    base_c, base_ht, base_ttc = tb * tk["contrib"], tb * tk["ht"], tb * tk["ttc"]
    # invendus
    p_cout, p_pcs, prod = invendus(x, units, prods, ctx)
    # agrégats journaliers
    d["ht"] = sum(units[k] * E[k]["ht"] for k in prods) + base_ht - sub_ht - rem_ht
    d["ttc"] = sum(units[k] * E[k]["ttc"] for k in prods) + base_ttc - sub_ttc - rem_ttc
    d["ca_ext_ttc"] = sum(units[k] * E[k]["ttc"] for k in prods)
    d["achats"] = sum(units[k] * E[k]["cout"] for k in prods) + p_cout
    d["emb"] = sum(units[k] * E[k]["emb"] for k in prods)
    d["cb"] = sum(units[k] * E[k]["cb"] for k in prods)
    d["var_base"] = base_ht - base_c
    d["var_moins"] = (sub_ht - sub_c) + (rem_ht - rem_c)
    d["c_att"] = sum(att[k] * E[k]["contrib"] for k in prods)
    d["c_nouv"] = sum(un_n[k] * E[k]["contrib"] for k in prods) + base_c
    d["c_sub"] = sub_c
    d["c_rem"] = rem_c
    d["pertes"] = p_cout
    d["pertes_pcs"] = p_pcs
    d["produites"] = prod
    d["contrib"] = d["c_att"] + d["c_nouv"] - sub_c - rem_c - p_cout
    enc = H["capacite"]["secondes_encaissement_ticket"]
    sec = sum(units[k] * prods[k]["service_s"] for k in prods) + nouv * (enc + pn.get("_ticket_base", 0) *
                                                                           (tk["temps_s"] - enc)) - rem_sec
    d["sec"] = sec
    d["sec_pointe"] = sec * x.get("pointe_part_unites", H["horaires"]["part_ventes_heure_pointe"])
    return d


# ── un scénario complet ─────────────────────────────────────────────────────────
_CACHE = {}


def sim0(H, scen, vm):
    k = (id(H), scen, round(vm, 9))
    if k not in _CACHE:
        _CACHE[k] = S.simulation(H, scen, volume_mult=vm)
    return _CACHE[k]


def invest_ext(X, exts):
    E = X["extensions"]
    capex = sum(v for k in exts for _, v in E[k]["capex"])
    dev = sum(E[k]["developpement"] for k in exts)
    stock = sum(E[k]["stock_initial"] for k in exts)
    surface = sum(E[k]["surface_m2"] for k in exts)
    return {"capex": capex, "dev": dev, "stock": stock, "total": capex + dev + stock, "surface": surface}


def scenario(H, X, sid, cas="central", ctx_extra=None, vm=1.0):
    G = X["global"]
    exts = X["scenarios"][sid] if isinstance(sid, str) else list(sid)
    ctx = {"dem": G["multiplicateur_demande"][cas], "scen": cas, "P0": S.table_produits(H),
           "pct0": S.ticket_annuel(H, cas)["contrib_pct"]}
    ctx.update(ctx_extra or {})
    if ctx.get("trafic"):
        ctx["scen"] = ctx["trafic"]
    base = sim0(H, ctx["scen"], vm)
    jours = H["calendrier"]["jours_par_mois"]
    inv = invest_ext(X, exts)
    amort_m = inv["capex"] / G["amort_ans_equipement"] / 12.0
    fond0 = base["cf"]["personnel"]["fond_valorisation"]
    P0 = ctx["P0"]
    rows = []
    due = {}
    refund = {}
    cum_d = 0.0
    par_ext = {k: {"an1": 0.0, "an2": 0.0, "an2_detail": {c: 0.0 for c in CHAMPS}, "units_an2": {}} for k in exts}
    for r in base["rows"]:
        t = r["t"]
        D = {c: 0.0 for c in CHAMPS}
        net = 0.0
        tva_due = 0.0
        if t == -2:
            net -= inv["dev"] * 1.2
            refund[t + 2] = refund.get(t + 2, 0.0) + inv["dev"] * 0.2
        if t == -1:
            net -= inv["capex"] * 1.2
            refund[t + 2] = refund.get(t + 2, 0.0) + inv["capex"] * 0.2
        if t == 0:
            net -= inv["stock"] * (1 + TVA_ACHATS)
            tva_due -= inv["stock"] * TVA_ACHATS
        if t >= 0 and exts:
            mc = r["m"]
            T = r["tickets_jour"]
            tk = S.ticket(H, S.mix_mois(H, mc, ctx["scen"]), P0)
            actifs = [k for k in exts if X["extensions"][k]["famille_dessert"] and
                      (not X["extensions"][k].get("saison_seule") or mc in X["extensions"][k]["saison_seule"])]
            ctx["chev"] = 0.0 if ctx.get("sans_chevauchement") else \
                G["chevauchement_desserts"].get(str(len(actifs)), 0.0) if actifs else 0.0
            for k in exts:
                dx = delta_ext(H, X, k, t, mc, T, tk, ctx)
                for c in CHAMPS:
                    D[c] += dx[c]
                ebe_k = dx["contrib"] * jours - dx["fixe"]
                if t < 12:
                    par_ext[k]["an1"] += ebe_k
                elif t < 24:
                    par_ext[k]["an2"] += ebe_k
                    for c in CHAMPS:
                        par_ext[k]["an2_detail"][c] += dx[c] * (jours if c not in ("fixe", "fixe_tva", "personnel", "fond", "h_sal") else 1)
                    for u, q in dx["units"].items():
                        par_ext[k]["units_an2"][u] = par_ext[k]["units_an2"].get(u, 0.0) + q * jours
            enc_ = D["ttc"] * jours
            dec_ = (D["achats"] * (1 + TVA_ACHATS) + D["emb"] * (1 + TVA_EMB) + D["cb"] +
                    (D["var_base"] - D["var_moins"]) * (1 + TVA_VAR_S0)) * jours + D["fixe"] + D["fixe_tva"]
            tva_due += (D["ttc"] - D["ht"]) * jours - (D["achats"] * TVA_ACHATS + D["emb"] * TVA_EMB +
                                                        (D["var_base"] - D["var_moins"]) * TVA_VAR_S0) * jours - D["fixe_tva"]
            net += enc_ - dec_
        net += refund.get(t, 0.0) - due.get(t, 0.0)
        due[t + 1] = due.get(t + 1, 0.0) + tva_due
        cum_d += net
        row = {"t": t, "cum": r["cum"] + cum_d, "net": r["net"] + net}
        if t >= 0:
            row.update({
                "m": r["m"], "tickets_base": r["tickets_jour"], "nouv": D["nouv"],
                "tickets": r["tickets_jour"] + D["nouv"],
                "ca_ht": r["ca_ht"] + D["ht"] * jours, "ca_ttc": r["ca_ttc"] + D["ttc"] * jours,
                "contrib": r["contrib"] + D["contrib"] * jours, "fixe": r["fixe"] + D["fixe"],
                "fond": fond0 + D["fond"], "amort": r["amort"] + amort_m,
                "d_contrib": D["contrib"] * jours, "d_fixe": D["fixe"], "d_ht": D["ht"] * jours,
                "pertes": D["pertes"] * jours, "pertes_pcs": D["pertes_pcs"] * jours, "produites": D["produites"] * jours,
                "c_nouv": D["c_nouv"] * jours, "c_att": D["c_att"] * jours, "c_sub": D["c_sub"] * jours,
                "c_rem": D["c_rem"] * jours, "sec_jour": r["tickets_jour"] * S.ticket(H, S.mix_mois(H, r["m"], ctx["scen"]), P0)["temps_s"] + D["sec"],
                "sec_pointe": r["tickets_jour"] * S.ticket(H, S.mix_mois(H, r["m"], ctx["scen"]), P0)["temps_s"] *
                H["horaires"]["part_ventes_heure_pointe"] + D["sec_pointe"],
                "h_sal": D["h_sal"], "personnel_ext": D["personnel"], "ca_ext_ttc": D["ca_ext_ttc"] * jours,
                "u_att": D["u_att"], "u_sub": D["u_sub"], "u_rem": D["u_rem"], "u_nouv": D["u_nouv"],
                "nouv_freq": D["nouv_freq"], "chev": ctx.get("chev", 0.0) if exts else 0.0})
            row["ebitda"] = row["contrib"] - row["fixe"]
            row["resultat"] = row["ebitda"] - row["amort"]
        rows.append(row)
    op1 = [x for x in rows if 0 <= x["t"] < 12]
    op2 = [x for x in rows if 12 <= x["t"] < 24]
    cles = ("ca_ht", "ca_ttc", "contrib", "fixe", "fond", "amort", "ebitda", "resultat", "d_contrib", "d_fixe",
            "pertes", "pertes_pcs", "produites", "c_nouv", "c_att", "c_sub", "c_rem", "ca_ext_ttc", "personnel_ext")
    an1 = {k: sum(x[k] for x in op1) for k in cles}
    an2 = {k: sum(x[k] for x in op2) for k in cles}
    for an, op in ((an1, op1), (an2, op2)):
        an["tickets_jour"] = sum(x["tickets"] for x in op) / len(op)
        an["tickets_base_jour"] = sum(x["tickets_base"] for x in op) / len(op)
        an["nouv_jour"] = sum(x["nouv"] for x in op) / len(op)
        an["panier_ttc"] = an["ca_ttc"] / (an["tickets_jour"] * jours * len(op))
        an["contrib_pct"] = an["contrib"] / an["ca_ht"]
        an["h_sal_semaine"] = sum(x["h_sal"] for x in op) / len(op)
        for c in ("u_att", "u_sub", "u_rem", "u_nouv", "nouv_freq", "chev"):
            an[c] = sum(x[c] for x in op) / len(op)
    besoin = -min(0.0, min(x["cum"] for x in rows))
    t_min = min(rows, key=lambda x: x["cum"])["t"]
    derniers = [x["cum"] for x in rows[-3:]]
    stabilise = not (rows[-1]["cum"] <= min(x["cum"] for x in rows) + 1e-6 and derniers[-1] < derniers[0])
    fin0 = S.financement(H, base)
    reserve = fin0["reserve"] + G["reserve"] * (inv["capex"] + inv["dev"])
    return {"sid": sid, "exts": exts, "cas": cas, "rows": rows, "an1": an1, "an2": an2, "inv": inv,
            "besoin": besoin, "mois_creux": t_min, "stabilise": stabilise, "reserve": reserve,
            "financement": besoin + reserve, "invest_total_ht": base["invest_ht"] + inv["total"],
            "invest_s0_ht": base["invest_ht"], "par_ext": par_ext, "cum_fin": rows[-1]["cum"]}


# ── recherches de seuils ────────────────────────────────────────────────────────
def bissection(f, a, b, it=50):
    fa, fb = f(a), f(b)
    if fa > 0 and fb > 0:
        return a
    if fa < 0 and fb < 0:
        return None
    for _ in range(it):
        m = (a + b) / 2
        fm = f(m)
        if (fm > 0) == (fb > 0):
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2


def point_mort(H, X, sid, mode="cash"):
    """Tickets de base/jour (moyenne de l'année 2) qui annulent l'EBE, ou le résultat, ou le résultat
    après rémunération des fondateurs ; les visites apportées par les extensions s'y ajoutent."""
    def f(vm):
        r = scenario(H, X, sid, "central", vm=vm)
        a = r["an2"]
        v = a["ebitda"]
        if mode in ("resultat", "complet"):
            v -= a["amort"]
        if mode in ("valorise", "complet"):
            v -= a["fond"]
        return v
    vm = bissection(f, 0.2, 4.0)
    if vm is None:
        return None
    r = scenario(H, X, sid, "central", vm=vm)
    return {"vm": vm, "base": r["an2"]["tickets_base_jour"], "total": r["an2"]["tickets_jour"],
            "nouv": r["an2"]["nouv_jour"], "r": r}


def demande_necessaire(H, X, cle, ref, mode="cash"):
    """Multiplicateur de la demande d'une extension seule qui annule son effet sur l'EBE (cash),
    sur le résultat (amortissements compris) ou sur le résultat complet (fondateurs valorisés)."""
    def f(m):
        r = scenario(H, X, [cle], "central", ctx_extra={"dem_ext": {cle: m}})
        dv = r["an2"]["ebitda"] - ref["an2"]["ebitda"]
        if mode in ("resultat", "complet"):
            dv -= r["an2"]["amort"] - ref["an2"]["amort"]
        if mode == "complet":
            dv -= r["an2"]["fond"] - ref["an2"]["fond"]
        return dv
    m = bissection(f, 0.0, 20.0)
    if m is None:
        return None
    r = scenario(H, X, [cle], "central", ctx_extra={"dem_ext": {cle: m}})
    return {"m": m, "r": r}


# ── rapports ────────────────────────────────────────────────────────────────────
def nom(X, sid):
    return X["noms_scenarios"].get(sid, sid)


def label_mois(H, t):
    return S.mois_label(H, t)


def rapport(H, X):
    G = X["global"]
    jours = H["calendrier"]["jours_par_mois"]
    L = ["# Modèle des extensions — résultats calculés", "",
         "Généré par `founder/extensions/modele_ext.py` à partir de `founder/modele/hypotheses.json` (%s, **non modifié**) "
         "et de `founder/extensions/hypotheses_ext.json` (%s). Montants HT sauf mention. Année 2 = régime de croisière "
         "(avril 2028 à mars 2029, ouverture hypothétique le %s). Fondateurs non payés sauf mention. "
         "**Toutes les demandes sont des hypothèses (H) : aucune vente réelle n'a été mesurée.**" % (
             H["version"], X["version"], H["calendrier"]["ouverture_hypothetique"]), ""]
    res = {}
    R = {}
    for sid in ORDRE:
        R[sid] = {c: scenario(H, X, sid, c) for c in CAS}
    ref = R["S0"]["central"]

    # 1. produits
    L += ["## 1. Économie unitaire des produits ajoutés (avant invendus et substitution)", "",
          "| extension | produit | prix TTC | TVA sur place / à emporter | HT moyen | achat | emballage | carte | contribution | % du HT |",
          "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    vus = set()
    for k, x in X["extensions"].items():
        for p in x["produits"]:
            if p["id"] in vus:
                continue
            vus.add(p["id"])
            q = eco(p, H)
            L.append("| %s | %s | %s | %s / %s | %s | %s | %s | %s | %s | %s |" % (
                k, p["nom"], e(q["ttc"], 2), pc(p["tva_sp"], 1), pc(p["tva_emp"], 1), e(q["ht"], 2), e(q["cout"], 2),
                e(q["emb"], 2), e(q["cb"], 2), e(q["contrib"], 2), pc(q["pct"])))
    L += ["", "Rappel S0 : contribution moyenne de %s par ticket (%s du HT)." % (
        e(S.ticket_annuel(H, "central")["contrib"], 2), pc(S.ticket_annuel(H, "central")["contrib_pct"])), ""]

    # 2. comparatif central
    L += ["## 2. Comparatif des scénarios — central, année 2 (croisière)", "",
          "| scénario | invest. ajouté (équipements + développement + stock) | invest. total HT | tickets/jour (dont visites ajoutées) | panier TTC | CA HT | marge sur coûts variables | % | charges fixes | heures salariées ajoutées / sem. | **EBE an 2** | Δ EBE vs S0 | résultat d'exploitation | EBE fondateurs valorisés | EBE an 1 | financement minimum |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for sid in ORDRE:
        r = R[sid]["central"]
        a, a1 = r["an2"], r["an1"]
        L.append("| %s | %s | %s | %s (+%s) | %s | %s | %s | %s | %s | %s | **%s** | %s | %s | %s | %s | %s |" % (
            nom(X, sid), e(r["inv"]["total"]), e(r["invest_total_ht"]), n(a["tickets_jour"], 1), n(a["nouv_jour"], 1),
            e(a["panier_ttc"], 2), e(a["ca_ht"]), e(a["contrib"]), pc(a["contrib_pct"]), e(a["fixe"]),
            n(a["h_sal_semaine"], 1), e(a["ebitda"]), e(a["ebitda"] - ref["an2"]["ebitda"]), e(a["resultat"]),
            e(a["ebitda"] - a["fond"]), e(a1["ebitda"]), e(r["financement"])))
    L += ["", "Le panier TTC est le chiffre d'affaires TTC divisé par tous les tickets, visites ajoutées comprises. "
          "Le financement minimum reprend la méthode de S0 : besoin de trésorerie maximal sur 24 mois + réserve de 10 %.", ""]

    # 2b. clients et achats
    L += ["## 2 bis. Clients, achats complémentaires, substitution, fréquence — central, année 2 (moyennes par jour)", "",
          "| scénario | visites ajoutées | dont visites plus fréquentes de clients existants | dont nouveaux clients | articles ajoutés achetés par les clients existants | articles ajoutés achetés lors des visites ajoutées | achats de S0 remplacés (substitution) | glaces de S0 remplacées | réduction par chevauchement des desserts (moyenne) |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for sid in ORDRE[1:]:
        a = R[sid]["central"]["an2"]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            sid, n(a["nouv_jour"], 1), n(a["nouv_freq"], 1), n(a["nouv_jour"] - a["nouv_freq"], 1), n(a["u_att"], 1),
            n(a["u_nouv"], 1), n(a["u_sub"], 1), n(a["u_rem"], 1), pc(a["chev"])))
    L += ["", "Les visites ajoutées et leur partage entre fréquence et nouveaux clients sont des hypothèses (H) ; seul un test réel peut les mesurer. "
          "Chevauchement : part des ventes de desserts retirée parce que plusieurs familles sollicitent les mêmes clients.", ""]

    # 3. décomposition
    L += ["## 3. D'où vient l'écart d'EBE — central, année 2", "",
          "| scénario | achats complémentaires | visites ajoutées | substitution | glaces de S0 remplacées | invendus | charges fixes ajoutées | **Δ EBE** | Δ amortissements | Δ résultat | temps des fondateurs (valeur) | Δ résultat complet |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for sid in ORDRE[1:]:
        a = R[sid]["central"]["an2"]
        b = ref["an2"]
        de = a["ebitda"] - b["ebitda"]
        da = a["amort"] - b["amort"]
        df = a["fond"] - b["fond"]
        L.append("| %s | %s | %s | −%s | −%s | −%s | −%s | **%s** | −%s | %s | −%s | %s |" % (
            sid, e(a["c_att"]), e(a["c_nouv"]), e(a["c_sub"]), e(a["c_rem"]), e(a["pertes"]), e(a["d_fixe"]),
            e(de), e(da), e(de - da), e(df), e(de - da - df)))
    L += ["", "Achats complémentaires : contribution des produits ajoutés achetés par les clients de S0, après chevauchement entre desserts. "
          "Visites ajoutées : contribution des visites supplémentaires (nouveaux clients ou visites plus fréquentes), produits ajoutés et part de ticket habituel comprises. "
          "Substitution : contribution perdue sur les produits de S0 qu'achetaient déjà ces clients. Résultat complet : après amortissements et valorisation du temps des fondateurs.", ""]

    # chevauchement
    L += ["### Effet du chevauchement (les hausses ne s'additionnent pas)", "",
          "| scénario | Δ EBE si l'on additionnait les extensions isolées | Δ EBE sans chevauchement | Δ EBE calculé |", "| --- | ---: | ---: | ---: |"]
    for sid in ("S2", "S5", "S6"):
        seul = sum(scenario(H, X, [k], "central")["an2"]["ebitda"] - ref["an2"]["ebitda"] for k in X["scenarios"][sid])
        sans = scenario(H, X, sid, "central", ctx_extra={"sans_chevauchement": True})["an2"]["ebitda"] - ref["an2"]["ebitda"]
        L.append("| %s | %s | %s | %s |" % (sid, e(seul), e(sans), e(R[sid]["central"]["an2"]["ebitda"] - ref["an2"]["ebitda"])))
    L.append("")
    L += ["### Contribution respective de chaque extension à l'intérieur des combinaisons (Δ EBE an 2)", "",
          "| scénario | " + " | ".join(X["extensions"].keys()) + " |", "| --- |" + " ---: |" * len(X["extensions"])]
    for sid in ("S2", "S5", "S5T", "S6"):
        pe = R[sid]["central"]["par_ext"]
        L.append("| %s | %s |" % (sid, " | ".join(e(pe[k]["an2"]) if k in pe else "—" for k in X["extensions"])))
    L.append("")

    # 4. trois cas
    L += ["## 4. Prudent, central, favorable", "",
          "Prudent : trafic de base prudent de S0 (65 tickets/jour en croisière) et demande des extensions ×0,5. "
          "Favorable : trafic favorable (135) et demande ×1,5. Ces cas encadrent l'incertitude ; ils ne sont pas des probabilités.", "",
          "| scénario | EBE an 2 prudent | central | favorable | Δ vs S0 prudent | Δ central | Δ favorable | financement prudent | central | favorable |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for sid in ORDRE:
        rr = R[sid]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s%s | %s | %s |" % (
            sid, *[e(rr[c]["an2"]["ebitda"]) for c in CAS],
            *[e(rr[c]["an2"]["ebitda"] - R["S0"][c]["an2"]["ebitda"]) for c in CAS],
            e(rr["prudent"]["financement"]), "" if rr["prudent"]["stabilise"] else " (toujours en baisse au mois 24)",
            e(rr["central"]["financement"]), e(rr["favorable"]["financement"])))
    L.append("")

    # 5. point mort
    L += ["## 5. Seuil de rentabilité (année 2, central)", "",
          "Tickets de base par jour nécessaires pour un EBE nul, en gardant les taux d'achat des extensions ; les visites apportées par les extensions s'y ajoutent.", "",
          "| scénario | EBE = 0 : tickets de base/jour | + visites ajoutées | **total tickets/jour** | EBE = 0 en payant les fondateurs | résultat = 0 (amortissements) | résultat complet = 0 (amortissements et fondateurs) |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    pms = {}
    for sid in ORDRE:
        p1 = point_mort(H, X, sid, "cash")
        p2 = point_mort(H, X, sid, "resultat")
        p3 = point_mort(H, X, sid, "complet")
        p4 = point_mort(H, X, sid, "valorise")
        pms[sid] = (p1, p2, p3, p4)
        L.append("| %s | %s | %s | **%s** | %s | %s | %s |" % (
            sid, n(p1["base"], 1), n(p1["nouv"], 1), n(p1["total"], 1), n(p4["total"], 1) if p4 else "—",
            n(p2["total"], 1) if p2 else "—", n(p3["total"], 1) if p3 else "—"))
    L.append("")
    # ventes par catégorie au point mort
    L += ["### Ventes quotidiennes au seuil (EBE = 0), par famille de produits", "",
          "| scénario | ventes de S0 au seuil (boissons / gourmandises / formules / safran / pots) | produits ajoutés au seuil (unités/jour) |", "| --- | --- | --- |"]
    t0 = S.ticket_annuel(H, "central")
    for sid in ORDRE:
        p1 = pms[sid][0]
        b = p1["base"]
        s0 = " / ".join(n(b * t0["cat_units"][c], 1) for c in S.CATS)
        ext = []
        for k, pe in p1["r"]["par_ext"].items():
            for u, q in pe["units_an2"].items():
                nomp = next(p["nom"] for p in X["extensions"][k]["produits"] if p["id"] == u)
                ext.append("%s : %s" % (nomp, n(q / 360.0, 1)))
        L.append("| %s | %s | %s |" % (sid, s0, " ; ".join(ext) or "—"))
    L += ["", "Ventes de S0 : unités par jour en moyenne sur l'année, au mix de S0 (avant substitution).", ""]

    # 6. ventes nécessaires par extension
    L += ["## 6. Ventes qu'une extension doit générer pour couvrir son coût (extension seule, central, année 2)", "",
          "Multiplicateur appliqué à toute la demande hypothétique de l'extension (achats complémentaires et visites). "
          "« Cash » : Δ EBE nul ; « résultat » : amortissements couverts ; « complet » : amortissements et temps des fondateurs couverts.", "",
          "| extension | demande centrale : unités/jour (Δ EBE) | seuil cash : multiplicateur, unités/jour | seuil résultat | seuil complet |",
          "| --- | --- | --- | --- | --- |"]
    besoins = {}
    for k in X["extensions"]:
        rc = scenario(H, X, [k], "central")
        uc = sum(rc["par_ext"][k]["units_an2"].values()) / 360.0
        cells = []
        for mode in ("cash", "resultat", "complet"):
            dn = demande_necessaire(H, X, k, ref, mode)
            if dn is None:
                cells.append("inatteignable (≤ ×20)")
                besoins[(k, mode)] = None
            else:
                u = dn["r"]["par_ext"][k]["units_an2"]
                tot = sum(u.values()) / 360.0
                besoins[(k, mode)] = {"m": dn["m"], "u": tot, "detail": {a: q / 360.0 for a, q in u.items()}}
                cells.append("×%s : %s/jour" % (n(dn["m"], 2), n(tot, 1)))
        L.append("| %s | %s (%s) | %s |" % (k, n(uc, 1), e(rc["an2"]["ebitda"] - ref["an2"]["ebitda"]), " | ".join(cells)))
    L.append("")
    # macarons par parfum
    L += ["### Macarons : rotation nécessaire par parfum", "",
          "| gamme | parfums | pièces vendues/jour (central) | par parfum et par jour | invendus (% des pièces livrées) | seuil cash : pièces/jour | par parfum | seuil résultat complet : pièces/jour | par parfum |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for k in ("macarons", "macarons_court", "macarons_reco"):
        x = X["extensions"][k]
        N = x["pertes"]["references"]
        rc = scenario(H, X, [k], "central")
        pcs = {p["id"]: p["pieces"] for p in x["produits"]}
        v = sum(q * pcs[u] for u, q in rc["par_ext"][k]["units_an2"].items()) / 360.0
        a = rc["an2"]
        taux = a["pertes_pcs"] / a["produites"] if a["produites"] else 0
        cells = []
        for mode in ("cash", "complet"):
            b = besoins[(k, mode)]
            if b is None:
                cells += ["—", "—"]
            else:
                rr = scenario(H, X, [k], "central", ctx_extra={"dem_ext": {k: b["m"]}})
                vv = sum(q * pcs[u] for u, q in rr["par_ext"][k]["units_an2"].items()) / 360.0
                cells += [n(vv, 1), n(vv / N, 1)]
        L.append("| %s | %d | %s | %s | %s | %s |" % (k, N, n(v, 1), n(v / N, 1), pc(taux), " | ".join(cells)))
    L.append("")

    # 7. sensibilités
    L += ["## 7. Sensibilités — Δ EBE année 2 par rapport à S0 (central sauf mention)", ""]
    sens = [
        ("Base centrale", {}, None),
        ("Demande des extensions ×0,5", {"dem": 0.5}, None),
        ("Demande des extensions ×1,5", {"dem": 1.5}, None),
        ("Demande totale inchangée : aucune visite ajoutée, dépense par client constante", {"sans_nouveaux": True, "sub_totale": True}, None),
        ("Fréquentation inchangée : aucune visite ajoutée, achats complémentaires seulement", {"sans_nouveaux": True}, None),
        ("Invendus doublés", {"pertes_mult": 2.0}, None),
        ("Minimums de commande doublés (et bacs de 5 L)", {"moq_mult": 2.0}, None),
        ("Renforts et heures de production doublés", {"renfort_mult": 2.0}, None),
        ("Saisonnalité aplatie (pas de pic de fin d'année ni d'été)", {"saison_plate": True}, None),
        ("Prix des produits ajoutés −10 %", {"prix_mult": 0.9}, None),
        ("Coût d'achat des produits ajoutés +20 %", {"cout_mult": 1.2}, None),
        ("Trafic de base prudent (65), demande des extensions centrale", {"trafic": "prudent", "dem": 1.0}, "prudent"),
        ("Trafic de base favorable (135), demande des extensions centrale", {"trafic": "favorable", "dem": 1.0}, "favorable"),
    ]
    cols = [s for s in ORDRE[1:]]
    L += ["| variable | " + " | ".join(cols) + " |", "| --- |" + " ---: |" * len(cols)]
    sens_res = {}
    for lab, cx, trafic in sens:
        refx = R["S0"][trafic or "central"]
        vals = []
        for sid in cols:
            r = scenario(H, X, sid, "central", ctx_extra=cx)
            dv = r["an2"]["ebitda"] - refx["an2"]["ebitda"]
            vals.append(dv)
        sens_res[lab] = dict(zip(cols, vals))
        L.append("| %s | %s |" % (lab, " | ".join(e(v) for v in vals)))
    L += ["", "« Demande totale inchangée » : chaque euro dépensé en produits ajoutés remplace un euro dépensé en produits de S0 ; "
          "le gain ne vient alors que de l'écart de marge, et les charges ajoutées restent. "
          "Ligne « invendus doublés » : coût des invendus ×2. Minimums doublés : 48 pièces par parfum de macaron, 12 entremets, bacs de 5 L.", ""]

    # 8. modes de fabrication
    L += ["## 8. Modes de fabrication comparés (extension seule, central, année 2)", "",
          "| variante | invest. ajouté | heures salariées / sem. | invendus (% livré) | surface (m²) | Δ EBE an 2 | Δ résultat complet |",
          "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    var_res = {}
    lignes_base = [("S1", "macarons"), ("S1c", "macarons_court"), ("S2a", "madeleines"), ("S2b", "entremets"),
                   ("S3", "traiteur"), ("S4", "glaces"), ("S4p", "glaces_pots")]
    variantes = {v["base"]: [] for v in X["variantes"]}
    for v in X["variantes"]:
        variantes[v["base"]].append(v)

    def ligne_var(lab, Xv, sid):
        r = scenario(H, Xv, sid, "central")
        a, b = r["an2"], ref["an2"]
        de = a["ebitda"] - b["ebitda"]
        dc = de - (a["amort"] - b["amort"]) - (a["fond"] - b["fond"])
        taux = a["pertes_pcs"] / a["produites"] if a["produites"] else 0
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (lab, e(r["inv"]["total"]), n(a["h_sal_semaine"], 1), pc(taux),
                                                         n(r["inv"]["surface"], 1), e(de), e(dc)))
        return {"de": de, "dc": dc, "inv": r["inv"]["total"], "taux": taux, "h": a["h_sal_semaine"]}
    for sid, k in lignes_base:
        var_res[sid] = ligne_var("%s (%s)" % (X["extensions"][k]["label"], sid), X, sid)
        for v in variantes.get(sid, []):
            var_res[v["id"]] = ligne_var("↳ %s (%s)" % (v["label"], v["id"]), modifier(X, v["modifs"]), sid)
    L.append("")

    # 9. capacité
    L += ["## 9. Capacité de service à l'heure de pointe (année 2)", "",
          "Charge de travail de l'heure de pointe en %% de la capacité soutenable de deux personnes (%s s de travail utile par heure). "
          "Au-delà de 70 %% l'attente devient visible ; au-delà de 100 %% le service décroche. Le traiteur concentre %s de ses plats dans l'heure du déjeuner." % (
              n(3600 * H["capacite"]["utilisation"] * H["capacite"]["facteur_deux_personnes"]),
              pc(X["extensions"]["traiteur"]["pointe_part_unites"])), "",
          "| scénario | juillet, central | décembre, central | juillet, favorable | décembre, favorable | secondes de service par jour (central, moyenne) |",
          "| --- | ---: | ---: | ---: | ---: | ---: |"]
    cap2 = 3600 * H["capacite"]["utilisation"] * H["capacite"]["facteur_deux_personnes"]
    cap_res = {}
    for sid in ORDRE:
        cells = []
        for c in ("central", "favorable"):
            rows = [x for x in R[sid][c]["rows"] if 12 <= x["t"] < 24]
            for m in (7, 12):
                rw = next(x for x in rows if x["m"] == m)
                cells.append(rw["sec_pointe"] / cap2)
        moy = sum(x["sec_jour"] for x in R[sid]["central"]["rows"] if 12 <= x["t"] < 24) / 12
        cap_res[sid] = cells
        L.append("| %s | %s | %s | %s | %s | %s |" % (sid, *[pc(v) for v in cells], n(moy)))
    L.append("")

    # 10. surfaces
    L += ["## 10. Surfaces (indicatif, sans plan)", "",
          "Implantation S0 de `founder/ops.md` : " + " ; ".join("%s %s m²" % (a, n(b)) for a, b in G["surfaces_s0"]) +
          ". Les équipements ajoutés prennent d'abord la marge non affectée (3 m²), puis les places assises (%s m² par place)." % n(G["m2_par_place"], 2), "",
          "| scénario | surface ajoutée | places assises restantes (sur ≈ %d) | loyer imputé à la surface ajoutée / mois |" % G["places_s0"],
          "| --- | ---: | ---: | ---: |"]
    surf_res = {}
    for sid in ORDRE:
        s_ = R[sid]["central"]["inv"]["surface"]
        places = G["places_s0"] - max(0.0, s_ - 3) / G["m2_par_place"]
        surf_res[sid] = (s_, places)
        L.append("| %s | %s m² | %s | %s |" % (sid, n(s_, 1), n(max(0, places), 0), e(s_ * G["loyer_m2_mois"])))
    L += ["", "Le loyer imputé n'est pas une dépense de plus : c'est la part du loyer payée pour la surface prise à la vente ou aux places assises.", ""]

    # 11. financement
    L += ["## 11. Financement minimum par scénario (central)", "",
          "| scénario | investissements S0 HT | + équipements | + développement | + stock | besoin maximal de trésorerie (24 mois) | creux | réserve | **total à mobiliser** | Δ vs S0 | délai de récupération de l'investissement ajouté |",
          "| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |"]
    fin_res = {}
    for sid in ORDRE:
        r = R[sid]["central"]
        de = r["an2"]["ebitda"] - ref["an2"]["ebitda"]
        if sid == "S0":
            pb = "—"
        elif de > 0:
            pb = "%s ans (sur l'EBE ajouté de l'année 2)" % n(r["inv"]["total"] / de, 1)
        else:
            pb = "non calculable (Δ EBE ≤ 0)"
        fin_res[sid] = (r["financement"], pb)
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | **%s** | %s | %s |" % (
            sid, e(r["invest_s0_ht"]), e(r["inv"]["capex"]), e(r["inv"]["dev"]), e(r["inv"]["stock"]), e(r["besoin"]),
            label_mois(H, r["mois_creux"]), e(r["reserve"]), e(r["financement"]), e(r["financement"] - ref["financement"]), pb))
    L += ["", "Le budget minimum de S0 (≈ 182 000 €, version minimale) suit la même logique : ajouter à ce montant le Δ de chaque scénario.", ""]

    # résultats JSON
    for sid in ORDRE:
        res[sid] = {c: {"ebitda_an2": R[sid][c]["an2"]["ebitda"], "ebitda_an1": R[sid][c]["an1"]["ebitda"],
                        "resultat_an2": R[sid][c]["an2"]["resultat"], "fond_an2": R[sid][c]["an2"]["fond"],
                        "ca_ht_an2": R[sid][c]["an2"]["ca_ht"], "panier_ttc_an2": R[sid][c]["an2"]["panier_ttc"],
                        "tickets_an2": R[sid][c]["an2"]["tickets_jour"], "nouv_an2": R[sid][c]["an2"]["nouv_jour"],
                        "contrib_pct_an2": R[sid][c]["an2"]["contrib_pct"], "fixe_an2": R[sid][c]["an2"]["fixe"],
                        "financement": R[sid][c]["financement"], "stabilise": R[sid][c]["stabilise"],
                        "h_sal": R[sid][c]["an2"]["h_sal_semaine"], "pertes_an2": R[sid][c]["an2"]["pertes"],
                        "c_att": R[sid][c]["an2"]["c_att"], "c_nouv": R[sid][c]["an2"]["c_nouv"],
                        "c_sub": R[sid][c]["an2"]["c_sub"], "c_rem": R[sid][c]["an2"]["c_rem"],
                        "d_fixe": R[sid][c]["an2"]["d_fixe"], "amort_an2": R[sid][c]["an2"]["amort"]}
                    for c in CAS}
        res[sid]["inv"] = R[sid]["central"]["inv"]
        res[sid]["invest_total_ht"] = R[sid]["central"]["invest_total_ht"]
        res[sid]["point_mort"] = {m: (pms[sid][i]["total"] if pms[sid][i] else None) for i, m in enumerate(("cash", "resultat", "complet", "valorise"))}
        res[sid]["point_mort_base"] = pms[sid][0]["base"]
        res[sid]["capacite"] = cap_res[sid]
        res[sid]["surface"] = surf_res[sid]
        res[sid]["payback"] = fin_res[sid][1]
    out = {"scenarios": res, "sensibilites": sens_res, "variantes": var_res,
           "besoins": {"%s|%s" % k: v for k, v in besoins.items()}}
    return "\n".join(L) + "\n", out


def main():
    H, X = charger()
    os.makedirs(SORTIES, exist_ok=True)
    txt, out = rapport(H, X)
    with open(os.path.join(SORTIES, "ext-modele.md"), "w", encoding="utf-8") as f:
        f.write(txt)
    with open(os.path.join(SORTIES, "resultats-ext.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    s = out["scenarios"]
    for sid in ORDRE:
        c = s[sid]["central"]
        print("%-4s EBE an2 %10s  Δ %10s  panier %6s  fin %10s" % (
            sid, e(c["ebitda_an2"]), e(c["ebitda_an2"] - s["S0"]["central"]["ebitda_an2"]), e(c["panier_ttc_an2"], 2),
            e(c["financement"])))


if __name__ == "__main__":
    main()
