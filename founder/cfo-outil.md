# Économie unitaire (outil unit_economics.py) : La Saffranerie (rue du Dragon) — unité = ticket moyen, montants HT en euros

Chaque chiffre vient du fichier d'entrée `founder/numbers.json` (généré par le modèle). Sortie traduite ; aucun chiffre modifié.

## Un ticket

| ligne | par ticket |
| --- | ---: |
| Prix HT | 8,66 € |
| Matières, safran (prix de cession) et crème | −1,99 € |
| Emballages et pertes | −0,21 € |
| Commissions carte | −0,14 € |
| **Contribution** (ce que chaque ticket laisse pour payer les charges fixes) | **6,32 €** (73 %) |

## La marge qui compte

Charges fixes : 17 140 € par mois (Loyer 6 667 €, Charges locatives et taxe foncière refacturées 800 €, Énergie et eau 450 €, Assurance multirisque et RC professionnelle 150 €, Expert-comptable, social et juridique courant 450 €, Caisse certifiée, logiciels, terminal de paiement 100 €, Internet et téléphone 50 €, Entretien, maintenance machine, hygiène, petits consommables 300 €, Déchets et biodéchets 60 €, Banque 30 €, Musique diffusée (SACEM/SPRE) 40 €, Dégustations offertes en vitrine 150 €, Analyses safran par lot (ISO 3632) et contrôle qualité 80 €, Divers et imprévus d'exploitation 250 €, CFE (provision) 100 €, Personnel (S2_minimal) 6 814 €, Communication mensuelle (B) 650 €).

- **Point mort : 91 tickets par jour.** En dessous, chaque mois est en perte.
- **Marge nette au volume prévu** (95 par jour) : **4 %** de chaque vente, après tous les coûts.
- Capacité : 313 par jour.

## Année 1, mois par mois

| mois | tickets par jour | CA HT | résultat | cumul (après 203 733 € d'investissement HT) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 64 | 16 532 € | −5 079 € | −208 812 € |
| 2 | 64 | 16 532 € | −5 079 € | −213 892 € |
| 3 | 72 | 18 663 € | −3 524 € | −217 416 € |
| 4 | 74 | 19 131 € | −3 183 € | −220 599 € |
| 5 | 68 | 17 598 € | −4 302 € | −224 900 € |
| 6 | 85 | 22 042 € | −1 059 € | −225 959 € |
| 7 | 87 | 22 640 € | −623 € | −226 582 € |
| 8 | 85 | 22 042 € | −1 059 € | −227 641 € |
| 9 | 108 | 28 151 € | 3 398 € | −224 243 € |
| 10 | 76 | 19 651 € | −2 804 € | −227 047 € |
| 11 | 80 | 20 769 € | −1 988 € | −229 035 € |
| 12 | 90 | 23 446 € | −35 € | −229 069 € |

- **Résultat d'exploitation année 1 : −25 336 €** pour 247 198 € de CA HT.
- Après les 203 733 € d'investissement : −229 069 €.
- Investissement remboursé : pas dans l'année 1.
- Trésorerie nécessaire avant autofinancement (selon l'outil, hors TVA et calendrier de paiement) : **229 069 €**.

## Et si…

| scénario | marge au volume prévu | point mort par jour | résultat année 1 |
| --- | ---: | ---: | ---: |
| Plan de base | 4 % | 91 | −25 336 € |
| Prix −10 % | -7 % | 105 | −50 056 € |
| Volume −20 % | -14 % | 91 | −61 406 € |
| Coûts unitaires +15 % | -1 % | 96 | −35 364 € |

## Signaux d'alerte

- L'année 1 perd de l'argent en exploitation (−25 336 €).
- L'investissement n'est pas remboursé dans l'année 1.
