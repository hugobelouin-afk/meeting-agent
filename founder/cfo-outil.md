# Économie unitaire (outil unit_economics.py) : La Saffranerie (rue du Dragon) — unité = ticket moyen, montants HT en euros

Chaque chiffre vient du fichier d'entrée `founder/numbers.json` (généré par le modèle). Sortie traduite ; aucun chiffre modifié.

## Un ticket

| ligne | par ticket |
| --- | ---: |
| Prix HT | 8,66 € |
| Matières, safran (prix de cession) et crème | −1,96 € |
| Emballages et pertes | −0,21 € |
| Commissions carte | −0,14 € |
| **Contribution** (ce que chaque ticket laisse pour payer les charges fixes) | **6,36 €** (73 %) |

## La marge qui compte

Charges fixes : 17 238 € par mois (Loyer 6 667 €, Charges locatives et taxe foncière refacturées 800 €, Énergie et eau 450 €, Assurance multirisque et RC professionnelle 150 €, Expert-comptable, social et juridique courant 450 €, Caisse certifiée, logiciels, terminal de paiement 100 €, Internet et téléphone 50 €, Entretien, maintenance machine, hygiène, petits consommables 300 €, Déchets et biodéchets 60 €, Banque 30 €, Musique diffusée (SACEM/SPRE) 40 €, Dégustations offertes en vitrine 150 €, Analyses safran par lot (ISO 3632) et contrôle qualité 80 €, Divers et imprévus d'exploitation 250 €, Personnel (S2_minimal) 7 012 €, Communication mensuelle (B) 650 €).

- **Point mort : 91 tickets par jour.** En dessous, chaque mois est en perte.
- **Marge nette au volume prévu** (95 par jour) : **4 %** de chaque vente, après tous les coûts.
- Capacité : 318 par jour.

## Année 1, mois par mois

| mois | tickets par jour | CA HT | résultat | cumul (après 202 733 € d'investissement HT) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 64 | 16 532 € | −5 110 € | −207 843 € |
| 2 | 64 | 16 532 € | −5 110 € | −212 952 € |
| 3 | 72 | 18 663 € | −3 546 € | −216 498 € |
| 4 | 74 | 19 131 € | −3 203 € | −219 701 € |
| 5 | 68 | 17 598 € | −4 328 € | −224 028 € |
| 6 | 85 | 22 042 € | −1 067 € | −225 095 € |
| 7 | 87 | 22 640 € | −628 € | −225 723 € |
| 8 | 85 | 22 042 € | −1 067 € | −226 790 € |
| 9 | 108 | 28 151 € | 3 415 € | −223 375 € |
| 10 | 76 | 19 651 € | −2 821 € | −226 196 € |
| 11 | 80 | 20 769 € | −2 001 € | −228 198 € |
| 12 | 90 | 23 446 € | −37 € | −228 235 € |

- **Résultat d'exploitation année 1 : −25 502 €** pour 247 198 € de CA HT.
- Après les 202 733 € d'investissement : −228 235 €.
- Investissement remboursé : pas dans l'année 1.
- Trésorerie nécessaire avant autofinancement (selon l'outil, hors TVA et calendrier de paiement) : **228 235 €**.

## Et si…

| scénario | marge au volume prévu | point mort par jour | résultat année 1 |
| --- | ---: | ---: | ---: |
| Plan de base | 4 % | 91 | −25 502 € |
| Prix −10 % | -7 % | 105 | −50 221 € |
| Volume −20 % | -14 % | 91 | −61 773 € |
| Coûts unitaires +15 % | -0 % | 96 | −35 378 € |

## Signaux d'alerte

- L'année 1 perd de l'argent en exploitation (−25 502 €).
- L'investissement n'est pas remboursé dans l'année 1.
