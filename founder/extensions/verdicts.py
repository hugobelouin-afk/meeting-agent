#!/usr/bin/env python3
"""Verdict calculé par l'outil du skill founder-plan pour S0, S5, S5T et S6.

    python3 founder/extensions/verdicts.py

Pour chaque scénario, écrit founder/extensions/verdicts/<S>/numbers.json (unité = ticket,
moyennes de l'année 2 du modèle des extensions, montée en puissance de l'année 1) et y copie
les résultats du panel correspondant, puis appelle compile.verdict() sans rien modifier dans
founder/. S5T reprend le panel S5 (aucun panel n'a vu le plat du midi sans les autres ajouts).
"""

import json
import os
import shutil
import sys

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))
sys.path.insert(0, ICI)
import modele_ext as M  # noqa: E402
import importlib.util  # noqa: E402

spec = importlib.util.spec_from_file_location("compile_plan", os.path.join(RACINE, ".claude", "skills", "founder-plan", "compile.py"))
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

PANELS = {"S0": os.path.join(RACINE, "founder", "panel"), "S5": os.path.join(ICI, "panel-S5"),
          "S5T": os.path.join(ICI, "panel-S5"), "S6": os.path.join(ICI, "panel-S6")}


def numbers(H, X, sid, base):
    r = M.scenario(H, X, sid, "central")
    a = r["an2"]
    jours = H["calendrier"]["jours_par_mois"]
    tickets = a["tickets_jour"] * jours * 12
    prix = a["ca_ht"] / tickets
    var = (a["ca_ht"] - a["contrib"]) / tickets
    d_fixe = a["d_fixe"] / 12.0
    rows1 = [x for x in r["rows"] if 0 <= x["t"] < 12]
    rows2 = [x for x in r["rows"] if 12 <= x["t"] < 24]
    sec = sum(x["sec_jour"] for x in rows2) / sum(x["tickets"] for x in rows2)
    sec0 = sum(x["sec_jour"] for x in M.scenario(H, X, "S0", "central")["rows"] if 12 <= x["t"] < 24) / \
        sum(x["tickets"] for x in M.scenario(H, X, "S0", "central")["rows"] if 12 <= x["t"] < 24)
    nj = json.loads(json.dumps(base))
    nj["business"] = "La Saffranerie — %s — unité = ticket moyen, montants HT en euros" % M.nom(X, sid)
    nj["price"] = round(prix, 4)
    nj["variable"] = [{"label": "Coûts variables moyens par ticket (matières, safran, crème, achats des extensions, emballages, invendus, carte)",
                       "cost": round(var, 4)}]
    if d_fixe:
        nj["fixed_monthly"] = base["fixed_monthly"] + [{"label": "Extensions : énergie, maintenance, renforts et heures de production",
                                                        "cost": round(d_fixe, 2)}]
    inv = r["inv"]
    if inv["total"]:
        nj["startup"] = base["startup"] + [{"label": "Extensions : équipements, développement et premier stock", "cost": inv["total"]}]
    nj["capacity_per_day"] = int(base["capacity_per_day"] * sec0 / sec)
    nj["plan_per_day"] = round(a["tickets_jour"], 1)
    nj["ramp_per_day"] = [round(x["tickets"], 1) for x in rows1]
    nj["_note"] = ("Généré par founder/extensions/verdicts.py à partir du modèle des extensions (année 2 pour le ticket moyen, "
                   "année 1 pour la montée en puissance). Montants en euros HT ; l'outil affiche '$'.")
    return nj


def main():
    H, X = M.charger()
    with open(os.path.join(RACINE, "founder", "numbers.json"), encoding="utf-8") as f:
        base = json.load(f)
    out = {}
    for sid in ("S0", "S5", "S5T", "S6"):
        d = os.path.join(ICI, "verdicts", sid)
        os.makedirs(os.path.join(d, "panel"), exist_ok=True)
        nj = base if sid == "S0" else numbers(H, X, sid, base)
        with open(os.path.join(d, "numbers.json"), "w", encoding="utf-8") as f:
            json.dump(nj, f, ensure_ascii=False, indent=1)
        shutil.copy(os.path.join(PANELS[sid], "results.json"), os.path.join(d, "panel", "results.json"))
        v, checks, num, panel = C.verdict(d)
        out[sid] = {"verdict": v, "checks": [(ok, t) for ok, t in checks],
                    "year1_profit": num["year1_profit"], "breakeven_per_day": num["breakeven_per_day"],
                    "contribution": num["contribution"], "cash_needed": num["cash_needed"]}
        print("%-4s %-10s an 1 : %10.0f € ; point mort %.1f tickets/jour" % (sid, v, num["year1_profit"], num["breakeven_per_day"]))
        for ok, t in checks:
            print("     %s %s" % ("✓" if ok else "✗", t))
    with open(os.path.join(ICI, "verdicts", "verdicts.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
