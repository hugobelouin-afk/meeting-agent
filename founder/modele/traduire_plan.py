#!/usr/bin/env python3
"""Lance compile.py (skill founder-plan) puis traduit son cadre anglais en français.
Le verdict reste celui calculé par compile.py ; aucun chiffre n'est modifié. Ajoute, juste après
le tableau des chiffres clés, les données critiques manquantes et la recommandation (texte du porteur de l'étude)."""
import os, re, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", ".."))
OUT = os.path.join(RACINE, "founder", "business-plan.md")
subprocess.run([sys.executable, os.path.join(RACINE, ".claude", "skills", "founder-plan", "compile.py"), "--dir", os.path.join(RACINE, "founder")], check=True)
s = open(OUT, encoding="utf-8").read()
V = {"Profitable": "Rentable", "Not yet": "Pas encore", "Incomplete": "Incomplet"}
m = re.search(r"\*\*Verdict: (Profitable|Not yet|Incomplete)\*\*", s)
verdict = m.group(1)
s = s.replace(m.group(0), "**Verdict : %s** (calculé par `compile.py` du skill founder-plan : « %s »)" % (V[verdict], verdict))
def eur(mm):
    return mm.group(1).replace(",", " ").replace(".", ",") + " €"
s = re.sub(r"\$-([\d,]+(?:\.\d+)?)", lambda mm: "−" + eur(mm), s)
s = re.sub(r"\$([\d,]+(?:\.\d+)?)", eur, s)
TR = [("· Business plan", "· Business plan"),
 ("Each ticket earns ", "Chaque ticket rapporte "), (" before fixed costs (", " avant charges fixes (contribution de "), ("% contribution).", " %)."),
 ("Year 1 operating LOSS: ", "Perte d'exploitation de l'année 1 : "), ("Year 1 operating profit: ", "Résultat d'exploitation de l'année 1 : "),
 ("Break-even is ", "Point mort : "), (" tickets a day against a capacity of ", " tickets par jour pour une capacité de "),
 (" simulated buyers buy (", " acheteurs simulés achètent ("), (" of 20 acheteurs", " sur 20 acheteurs"), ("%, the bar is ", " %, seuil "), ("%).", " %)."),
 ("| key number | |", "| chiffre clé | |"), ("| Price |", "| Prix (ticket moyen HT) |"), (" a ticket |", " par ticket |"),
 ("| Profit margin at plan |", "| Marge nette au volume prévu |"), ("% per ticket |", " % par ticket |"),
 ("| Break-even |", "| Point mort |"), (" tickets a day |", " tickets par jour |"),
 ("| Year 1 operating profit |", "| Résultat d'exploitation année 1 (outil) |"), ("| Startup spend |", "| Investissement et pré-ouverture HT |"),
 ("| Cash needed before it pays for itself |", "| Trésorerie nécessaire selon l'outil (hors TVA ; voir CFO : 267 208 € réserve comprise) |"),
 ("| Startup money earned back |", "| Investissement remboursé |"), ("not in year 1", "pas dans l'année 1"),
 ("| Buyer panel |", "| Panel simulé |"), (" buy · ", " achètent · "), (" pass |", " passent |"),
 ("## The idea", "## L'idée"), ("## Summary", "## Synthèse"), ("## What the board said", "## Ce qu'a dit le board"),
 ("## The competition", "## La concurrence"), ("## The buyer panel", "## Le panel d'acheteurs (simulé)"), ("## Pricing", "## Les prix"),
 ("## The offer", "## L'offre"), ("## The numbers", "## Les chiffres (CFO)"), ("## Marketing", "## Marketing"), ("## Brand", "## La marque"),
 ("## Operations", "## L'exploitation"), ("## Launch plan", "## Le plan de lancement"), ("## Not done yet", "## Pas encore fait"),
 ("_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._",
  "_Le panel est composé d'acheteurs simulés et les chiffres sont des projections tirées des hypothèses. Confirmer la demande avec de vrais clients et les coûts avec de vrais devis avant de dépenser. Ni conseil financier, ni juridique, ni fiscal._")]
for a, b in TR:
    s = s.replace(a, b)
s = s.replace(" of 20 acheteurs", " sur 20 acheteurs").replace("  %", " %")
AJOUT = open(os.path.join(ICI, "plan_ajout.md"), encoding="utf-8").read()
s = s.replace("\n## L'idée", "\n" + AJOUT + "\n## L'idée", 1)
open(OUT, "w", encoding="utf-8").write(s)
print("Verdict : %s (%s). Écrit %s" % (V[verdict], verdict, OUT))
