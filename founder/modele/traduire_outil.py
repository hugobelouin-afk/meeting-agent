#!/usr/bin/env python3
"""Lance unit_economics.py (skill founder-cfo) sur ../numbers.json et traduit sa sortie en français, en euros.
Aucun chiffre n'est modifié : seuls les libellés et le symbole monétaire changent."""
import os, re, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
OUTIL = os.path.join(ICI, "..", "..", ".claude", "skills", "founder-cfo", "unit_economics.py")
txt = subprocess.run([sys.executable, OUTIL, os.path.join(ICI, "..", "numbers.json")], capture_output=True, text=True, check=True).stdout
def euro(m):
    neg, val = m.group(1), m.group(2)
    return ("−" if neg else "") + val.replace(",", " ").replace(".", ",") + " €"
txt = re.sub(r"(-?)\$(\d{1,3}(?:,\d{3})*(?:\.\d+)?)", lambda m: euro(m), txt)
TR = [("# Unit economics:", "# Économie unitaire (outil unit_economics.py) :"),
 ("Every number below comes from the input file. Nothing is looked up or guessed.", "Chaque chiffre vient du fichier d'entrée `founder/numbers.json` (généré par le modèle). Sortie traduite ; aucun chiffre modifié."),
 ("## One ticket", "## Un ticket"), ("| line | per ticket |", "| ligne | par ticket |"), ("| Price |", "| Prix HT |"),
 ("**Contribution** (what each ticket leaves to pay the fixed costs)", "**Contribution** (ce que chaque ticket laisse pour payer les charges fixes)"),
 ("## The margin that matters", "## La marge qui compte"), ("Fixed costs:", "Charges fixes :"), (" a month (", " par mois ("),
 ("- **Break-even:", "- **Point mort :"), ("tickets a day.** Below that you lose money every month.", "tickets par jour.** En dessous, chaque mois est en perte."),
 ("- **Profit margin at your plan**", "- **Marge nette au volume prévu**"), (" a day): ", " par jour) : "), ("of every sale, after every cost.", "de chaque vente, après tous les coûts."),
 ("- Capacity:", "- Capacité :"), (" a day.", " par jour."),
 ("## Year 1, month by month", "## Année 1, mois par mois"),
 ("| month | tickets a day | revenue | profit | cumulative (after", "| mois | tickets par jour | CA HT | résultat | cumul (après"), (" startup) |", " d'investissement HT) |"),
 ("- **Year 1 operating profit:", "- **Résultat d'exploitation année 1 :"), ("** on ", "** pour "), (" of revenue.", " de CA HT."),
 ("- After the ", "- Après les "), (" startup spend: ", " d'investissement : "),
 ("- Startup money earned back:", "- Investissement remboursé :"), ("not within year 1", "pas dans l'année 1"), ("month ", "mois "),
 ("- Cash you need before it pays for itself:", "- Trésorerie nécessaire avant autofinancement (selon l'outil, hors TVA et calendrier de paiement) :"),
 ("## What if", "## Et si…"), ("| scenario | margin at plan | break-even a day | year 1 profit |", "| scénario | marge au volume prévu | point mort par jour | résultat année 1 |"),
 ("| Base plan |", "| Plan de base |"), ("| Price -10% |", "| Prix −10 % |"), ("| Volume -20% |", "| Volume −20 % |"), ("| Unit costs +15% |", "| Coûts unitaires +15 % |"),
 ("## Red flags", "## Signaux d'alerte"), ("Year 1 loses money on operations", "L'année 1 perd de l'argent en exploitation"),
 ("The startup spend is not earned back within year 1.", "L'investissement n'est pas remboursé dans l'année 1."),
 ("Break-even needs", "Le point mort exige"), ("but capacity is", "mais la capacité est de"),
 ("No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.", "Aucun signal d'alerte dans ces chiffres. Ils ne valent que ce que valent les entrées : vérifier chaque coût par un devis.")]
for a, b in TR:
    txt = txt.replace(a, b)
txt = re.sub(r"(\d+)%", r"\1 %", txt)
open(os.path.join(ICI, "..", "cfo-outil.md"), "w", encoding="utf-8").write(txt)
print(txt)
