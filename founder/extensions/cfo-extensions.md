# Note du CFO — extensions S0 à S6

Calculs : `modele_ext.py` (sorties complètes dans `sorties/ext-modele.md` et `sorties/resultats-ext.json`).
- Le modèle importe le modèle v2 de l'étude initiale (`founder/modele/saffranerie.py`) et ses hypothèses, **sans les modifier**. S0 reproduit exactement les chiffres de `founder/cfo.md` : EBE an 2 de 9 783 €, financement de 267 208 €.
- Montants HT sauf mention.
- **Année 2** : régime de croisière, avril 2028 à mars 2029, à partir d'une ouverture hypothétique le 1er avril 2027.
- **Fondateurs non payés sauf mention.**
- **Toutes les demandes ajoutées sont des hypothèses (H)** : aucune vente réelle n'existe.

## 1. Hypothèses modifiées ou ajoutées (avant / après)

| sujet | S0 (étude initiale) | étude des extensions | nature |
| --- | --- | --- | --- |
| Carte, prix, mix, volumes de base, charges, personnel, investissements de S0 | `founder/modele/hypotheses.json` v2 | **inchangés** | — |
| Glace | partenaire non nommé, 14 €/L ; 4 € la boule ; 2 parfums ; congélateur sans vitrine | ANGIOLO (C) ; 18 €/L ; 5 € la boule, 8 € les deux (prix de détail d'ANGIOLO, V 2024) ; 4 ou 6 parfums ; vitrine à boules ou pots | C / V / E |
| Achats complémentaires | — | unités pour 100 tickets de base, par produit (ex. : 10 macarons à l'unité, 12 madeleines, 5 plats) | H |
| Visites ajoutées | — | 1 à 10 tickets/jour par extension en croisière (10 pour le plat du midi), suivant la montée en puissance de S0 ; 20 à 50 % viennent de clients existants qui reviennent plus souvent | H |
| Substitution | — | part des achats ajoutés qui remplacent un achat de S0, et contribution perdue (ex. : 40 % des macarons à l'unité remplacent un croissant ou une formule, 2 € perdus) | H |
| Chevauchement des desserts | — | 15 % des ventes de desserts retirées avec 2 familles, 25 % avec 3, 35 % avec 4 | H |
| Invendus | taux fixe par produit | selon l'approvisionnement : taux fixe ; rotation par parfum (quantité livrée = demande du cycle + présentation, ou minimum de commande) ; bacs de glace jetés après 3 jours | E |
| Charges fixes ajoutées | — | énergie à 0,22 €/kWh ; maintenance ; renforts à 15,21 €/h ; heures qualifiées à 22,14 €/h | E |
| Temps des fondateurs | 28 h/semaine, valorisé à 21,25 €/h | + 0,5 à 3 h/semaine par extension, même valeur | E |
| Investissements | — | équipements amortis sur 5 ans ; développement en charge avant ouverture ; premier stock ; réserve de 10 % | E |

## 2. TVA (vérifiée : BOFiP BOI-TVA-LIQ-30-10-10 du 07/02/2024)

| produit | sur place | à emporter | référence |
| --- | ---: | ---: | --- |
| Macarons, madeleines, entremets | 10 % | **5,5 %** | § 210 (pâtisseries contenant du chocolat) et § 330 (pâtisseries sucrées vendues sous emballage de conservation) ; **le texte ne cite ni « macaron » ni « madeleine » : qualification à confirmer par l'expert-comptable** |
| Coffrets de macarons, sachet de madeleines, entremets entier | — | 5,5 % | idem |
| Glace en pot individuel de moins de 200 ml, cornet | 10 % | **10 %** | § 320 ; les bacs familiaux seraient à 5,5 % |
| Plat préparé à emporter pour consommation immédiate | 10 % | **10 %** | § 300 |

Le modèle applique ces taux produit par produit, avec une part consommée sur place supposée (25 à 55 % selon le produit, H).

## 3. Comparatif — scénario central, année 2

| scénario | investissement ajouté | panier TTC | tickets/jour (dont visites ajoutées) | CA HT | marge sur coûts variables | charges fixes | heures salariées ajoutées / sem. | **EBE an 2** | **Δ EBE** | résultat d'exploitation | EBE fondateurs payés | EBE an 1 | financement minimum |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| S0 référence | 0 € | 9,33 € | 94,7 (+0) | 295 338 € | 73 % | 205 686 € | 0 | 9 783 € | — | −5 695 € | −21 157 € | −26 215 € | 267 208 € |
| S1 macarons 11 parfums | 9 600 € | 10,46 € | 98,1 (+3,4) | 343 678 € | 66 % | 209 941 € | 4 | 15 592 € | +5 809 € | −1 065 € | −17 005 € | −24 994 € | 278 978 € |
| S1c macarons, 5 parfums (frais) | 4 200 € | 10,22 € | 96,9 (+2,2) | 331 854 € | 69 % | 207 704 € | 2 | 20 156 € | +10 373 € | 4 419 € | −11 889 € | −18 307 € | 271 190 € |
| S2 madeleines et entremets | 6 950 € | 10,00 € | 96,8 (+2,1) | 323 735 € | 71 % | 210 632 € | 5 | 17 922 € | +8 139 € | 1 504 € | −14 675 € | −20 853 € | 274 430 € |
| S2a madeleines seules | 2 300 € | 9,57 € | 96,2 (+1,5) | 307 883 € | 73 % | 208 968 € | 4 | 17 178 € | +7 395 € | 1 460 € | −14 315 € | −20 511 € | 269 061 € |
| S2b entremets seuls (vitrine) | 4 650 € | 9,88 € | 95,7 (+1,0) | 316 201 € | 70 % | 207 350 € | 1 | 13 622 € | +3 839 € | −2 556 € | −18 423 € | −23 953 € | 272 228 € |
| S3 traiteur | 9 900 € | 10,76 € | 104,2 (+9,5) | 373 354 € | 68 % | 220 839 € | 17,5 | 33 465 € | +23 682 € | 16 587 € | −790 € | −8 523 € | 275 914 € |
| S4 glaces, vitrine de 6 bacs | 6 600 € | 9,51 € | 96,7 (+2,0) | 307 131 € | 70 % | 207 371 € | 2 en saison | 6 873 € | **−2 910 €** | −9 565 € | −24 619 € | −32 970 € | 277 977 € |
| S4p glaces en pots | 2 100 € | 9,42 € | 95,7 (+1,0) | 301 183 € | 72 % | 206 004 € | 0 | 11 736 € | +1 953 € | −3 882 € | −19 480 € | −24 826 € | 269 407 € |
| **S5 combinaison** (madeleines, 5 macarons surgelés, entremets sur commande) | **8 800 €** | **10,43 €** | 97,7 (+3,1) | 341 691 € | 71 % | 211 679 € | 6,5 | **29 389 €** | **+19 607 €** | 13 192 € | **−3 761 €** | −10 497 € | 275 030 € |
| S5T = S5 + traiteur | 18 700 € | 11,72 € | 107,3 (+12,6) | 419 707 € | 67 % | 226 832 € | 24 | 53 071 € | +43 288 € | 35 473 € | +16 606 € | +7 194 € | 283 736 € |
| S6 offre complète | 33 050 € | 11,88 € | 109,7 (+15,0) | 434 748 € | **59 %** | 231 725 € | 27,5 | 24 521 € | +14 738 € | 4 563 € | −13 602 € | −25 646 € | **309 115 €** |

**Chiffre d'affaires et résultat ne bougent pas ensemble.**
- S6 ajoute **139 410 €** de CA HT (+47 %) mais seulement **14 738 €** d'EBE. C'est **moins que S5**, qui ajoute 46 353 € de CA pour 19 607 € d'EBE.
- S6 coûte 34 085 € de financement de plus que S5 et 21 h salariées de plus par semaine.
- Ses invendus atteignent 37 164 € par an, contre 699 € pour S5.

## 4. D'où vient l'écart d'EBE (central, année 2)

| scénario | achats complémentaires des clients existants | visites ajoutées | substitution | glaces de S0 remplacées | invendus | charges fixes ajoutées | **Δ EBE** | Δ amortissements | fondateurs (valeur) | **Δ résultat complet** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| S1 | 16 595 € | 13 310 € | −6 282 € | — | **−13 560 €** | −4 255 € | 5 809 € | −1 180 € | −1 658 € | 2 972 € |
| S1c | 14 001 € | 8 874 € | −5 247 € | — | −5 236 € | −2 018 € | 10 373 € | −260 € | −1 105 € | 9 008 € |
| S2 | 17 631 € | 5 588 € | −5 397 € | — | −4 736 € | −4 946 € | 8 139 € | −940 € | −1 658 € | 5 542 € |
| S2a | 11 146 € | 4 018 € | −4 377 € | — | −111 € | −3 282 € | 7 395 € | −240 € | −552 € | 6 602 € |
| S2b | 9 596 € | 2 556 € | −1 973 € | — | −4 676 € | −1 664 € | 3 839 € | −700 € | −1 105 € | 2 034 € |
| S3 | 11 381 € | **34 798 €** | −2 435 € | — | −4 909 € | **−15 153 €** | 23 682 € | −1 400 € | −3 315 € | 18 967 € |
| S4 | 11 274 € | 3 904 € | −129 € | −7 051 € | **−9 223 €** | −1 685 € | −2 910 € | −960 € | −552 € | −4 422 € |
| S4p | 7 839 € | 1 768 € | −67 € | −7 051 € | −217 € | −318 € | 1 953 € | −140 € | −276 € | 1 537 € |
| **S5** | 22 081 € | 11 512 € | −7 296 € | — | −699 € | −5 993 € | **19 607 €** | −720 € | −2 210 € | **16 677 €** |
| S5T | 33 463 € | 46 310 € | −9 730 € | — | −5 608 € | −21 146 € | 43 288 € | −2 120 € | −5 525 € | 35 643 € |
| S6 | 44 966 € | 51 352 € | −11 325 € | −7 051 € | **−37 164 €** | −26 039 € | 14 738 € | −4 480 € | −7 183 € | 3 075 € |

**Les hausses ne s'additionnent pas.** Le modèle applique un chevauchement entre familles de desserts (mêmes clients, même appétit, même budget) :

| | somme des extensions prises isolément | calcul combiné |
| --- | ---: | ---: |
| S2 | 11 234 € | 8 139 € |
| S5 | 28 140 € | 19 607 € |
| S6 | 37 815 € | 14 738 € |

**Contribution de chaque ajout à l'intérieur des combinaisons :**
- S5 : macarons +10 372 € ; madeleines +4 726 € ; entremets sur commande +4 509 €.
- S6 :
  - plat du midi +23 682 € ;
  - madeleines +4 200 € ;
  - entremets +863 € ;
  - **macarons 11 parfums −3 581 €** ;
  - **glaces 6 bacs −10 426 €**.

## 5. Prudent, central, favorable (EBE année 2, et écart avec S0 dans le même cas)

- **Prudent** : trafic de base de 65 tickets/jour et demande des extensions ×0,5.
- **Favorable** : 135 tickets/jour et demande ×1,5.

| scénario | prudent | central | favorable |
| --- | ---: | ---: | ---: |
| S0 | −76 528 € | 9 783 € | 125 800 € |
| S1 | −91 733 € (−15 205) | 15 592 € (+5 809) | 149 620 € (+23 820) |
| S1c | −78 424 € (−1 897) | 20 156 € (+10 373) | 150 066 € (+24 266) |
| S2 | −79 294 € (−2 767) | 17 922 € (+8 139) | 150 625 € (+24 825) |
| S2a | −75 655 € (+873) | 17 178 € (+7 395) | 143 009 € (+17 208) |
| S3 | −74 090 € (+2 437) | 33 465 € (+23 682) | 174 881 € (+49 081) |
| S4 | −90 659 € (−14 131) | 6 873 € (−2 910) | 140 520 € (+14 720) |
| S4p | −78 209 € (−1 681) | 11 736 € (+1 953) | 134 015 € (+8 215) |
| **S5** | **−72 162 € (+4 366)** | **29 389 € (+19 607)** | **167 609 € (+41 809)** |
| S5T | −69 724 € (+6 803) | 53 071 € (+43 288) | 216 690 € (+90 889) |
| S6 | **−116 040 € (−39 512)** | 24 521 € (+14 738) | 206 025 € (+80 225) |

**Lecture :**
- **Aucune extension ne sauve le cas prudent.** À 65 tickets/jour, tous les scénarios perdent 70 000 à 116 000 € par an, et la trésorerie baisse encore au mois 24.
- S5 et S5T améliorent le cas prudent. S1 (11 macarons), S4 (vitrine à glaces) et surtout S6 **l'aggravent** : leurs charges et leurs invendus restent quand la demande manque.

## 6. Seuils de rentabilité et ventes nécessaires

**Tickets par jour nécessaires** (moyenne de l'année 2, visites ajoutées comprises) :

| scénario | EBE = 0 | EBE = 0 en payant les fondateurs | résultat = 0 (amortissements) | résultat complet = 0 |
| --- | ---: | ---: | ---: | ---: |
| S0 | 90,4 | 104,0 | 97,2 | 110,8 |
| S1 | 91,5 | 105,2 | 98,5 | 112,2 |
| S1c | 88,4 | 102,0 | 95,1 | 108,6 |
| S2a | 88,9 | 102,3 | 95,6 | 109,0 |
| S3 | 90,0 (dont 80,5 de base) | 104,6 | 97,2 | 111,7 |
| S4 | 93,8 | 107,1 | 100,7 | 114,0 |
| **S5** | **85,6** (dont 82,6 de base) | **99,3** | 92,3 | 106,0 |
| S5T | 86,1 (dont 73,5 de base) | 100,6 | 93,1 | 107,7 |
| S6 | **100,4** | 114,8 | 108,0 | 122,4 |

**Le meilleur scénario n'abaisse le point mort que de 5 tickets par jour** (de 90 à 86). Les extensions ne changent pas la nature du risque : il faut toujours ≈ 86 clients par jour, 7 jours sur 7. **S6 le relève à 100.**

**Au seuil de S5**, il faut vendre chaque jour, en moyenne :
- en produits de S0 (avant substitution) : ≈ 56 boissons, 28 gourmandises, 7 formules, 9 safrans et 10 pots ou coffrets ;
- en produits ajoutés : 10 madeleines, 1 sachet, 8 macarons à l'unité, 2,6 coffrets de 6, 0,6 coffret de 12 et 0,6 entremets.

**Ventes qu'une extension doit générer pour couvrir son propre coût** (seule, année 2) :

| extension | demande centrale supposée | couvre ses coûts de trésorerie à | couvre aussi amortissements et fondateurs à |
| --- | --- | --- | --- |
| Macarons 11 parfums, frais | 21,7 articles/jour | 79 % de cette demande (17,2/jour) | 88 % (19,1/jour) |
| Macarons, 5 parfums, frais | 16,6 articles/jour | 47 % (7,8/jour) | 52 % (8,6/jour) |
| **Macarons, 5 parfums, surgelés** | 16,6 articles/jour | **14 % (2,3/jour)** | 23 % (3,8/jour) |
| Madeleines sur place | 16,1 articles/jour | **31 % (4,9/jour)** | 38 % (6,1/jour) |
| Entremets en vitrine | 6,2/jour | 61 % (3,8/jour) | 80 % (4,9/jour) |
| Entremets sur commande | 0,9/jour | 6 % | 15 % |
| Plat du midi | 14,1 plats/jour | 39 % (**5,5 plats/jour**) | 51 % (7,2/jour) |
| Glaces, 6 bacs | 10,7/jour en saison | **114 % : inatteignable sans dépasser l'hypothèse** | 121 % |
| Glaces en pots | 8,4/jour en saison | 79 % (6,6/jour) | 83 % (7,0/jour) |

**Rotation des macarons par parfum** (pièces ; un coffret de 6 compte 6 pièces) :

| gamme | vendues par parfum et par jour (central) | invendus | seuil de trésorerie par parfum et par jour | seuil complet par parfum |
| --- | ---: | ---: | ---: | ---: |
| 11 parfums, frais | 5,3 | 37 % | **4,2** | 4,6 |
| 5 parfums, frais | 9,0 | 23 % | 4,2 | 4,6 |
| 5 parfums, surgelés | 9,0 | 4 % | **1,2** | 2,0 |

Avec 11 parfums livrés frais, le seuil (4,2) est à 20 % de la demande supposée (5,3) : la moindre erreur de prévision fait perdre de l'argent.

## 7. Résultat, trésorerie, financement

| scénario | investissements S0 | + équipements | + développement | + stock | besoin de trésorerie maximal (24 mois) | réserve | **total à mobiliser** | Δ vs S0 | récupération de l'investissement ajouté |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| S0 | 203 733 € | — | — | — | 249 735 € | 17 473 € | **267 208 €** | — | — |
| S1 | | 5 900 € | 2 500 € | 1 200 € | 260 665 € | 18 313 € | 278 978 € | +11 770 € | 1,7 an |
| S2a | | 1 200 € | 800 € | 300 € | 251 388 € | 17 673 € | 269 061 € | +1 853 € | 0,3 an |
| S3 | | 7 000 € | 2 500 € | 400 € | 257 491 € | 18 423 € | 275 914 € | +8 706 € | 0,4 an |
| S4 | | 4 800 € | 1 000 € | 800 € | 259 924 € | 18 053 € | 277 977 € | +10 769 € | non calculable (Δ EBE < 0) |
| **S5** | | 3 600 € | 3 400 € | 1 800 € | 256 857 € | 18 173 € | **275 030 €** | **+7 822 €** | **≈ 5 mois** |
| S5T | | 10 600 € | 5 900 € | 2 200 € | 264 613 € | 19 123 € | 283 736 € | +16 528 € | ≈ 5 mois |
| S6 | | 22 400 € | 7 800 € | 2 850 € | 288 622 € | 20 493 € | **309 115 €** | **+41 907 €** | 2,2 ans |

**Comment lire ce tableau :**
- **Creux de trésorerie.** Dans tous les cas, il tombe en mai 2027, juste après l'ouverture : il vient des travaux et des équipements de S0. Les extensions l'approfondissent du montant de leurs investissements, sans le déplacer.
- **Budget minimal.** Il suit la même logique. Les 182 000 € de la version minimale de S0 deviennent :
  - ≈ 190 000 € avec S5 ;
  - ≈ 198 700 € avec S5T ;
  - ≈ 224 000 € avec S6.
- **Délai de récupération.** Il rapporte l'investissement ajouté à l'EBE ajouté en croisière. Il n'est calculable que si l'extension améliore l'EBE.

## 8. Sensibilités — Δ EBE année 2 par rapport à S0

| variable | S1 | S1c | S2a | S2b | S3 | S4 | S4p | **S5** | S5T | S6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Base centrale | 5 809 | 10 373 | 7 395 | 3 839 | 23 682 | −2 910 | 1 953 | **19 607** | 43 288 | 14 738 |
| Demande des extensions ×0,5 | −11 726 | 867 | 2 056 | −1 137 | 4 264 | −13 696 | −2 674 | **6 807** | 11 071 | −33 445 |
| Demande des extensions ×1,5 | 17 357 | 18 832 | 12 733 | 8 816 | 43 099 | 7 712 | 6 423 | 32 406 | 75 505 | 59 084 |
| **Demande totale inchangée** (aucune visite ajoutée, dépense par client constante) | −28 811 | −13 083 | −2 055 | −10 669 | −20 957 | −10 768 | −1 059 | **−11 177** | −32 134 | −76 698 |
| **Fréquentation inchangée** (achats complémentaires seulement) | −11 576 | 1 537 | 3 396 | 1 322 | −7 782 | −8 207 | 216 | **8 321** | 539 | −39 036 |
| Invendus doublés | −7 750 | 5 137 | 7 284 | −837 | 18 772 | −12 133 | 1 736 | 18 908 | 37 680 | −22 427 |
| Minimums de commande doublés | −18 312 | 4 441 | 7 395 | 2 277 | 23 682 | −18 786 | 1 953 | 19 607 | 43 288 | −32 890 |
| Renforts et heures de production doublés | 2 646 | 8 792 | 4 232 | 3 048 | 9 844 | −3 701 | 1 953 | 14 467 | 24 311 | −7 007 |
| Saisonnalité aplatie | 3 349 | 8 385 | 7 212 | 3 701 | 25 636 | −2 803 | 2 032 | 17 916 | 43 552 | 14 142 |
| Prix des ajouts −10 % | 517 | 6 280 | 5 849 | 1 675 | 17 124 | −5 071 | 322 | 14 447 | 31 571 | 435 |
| Coût d'achat des ajouts +20 % | −1 498 | 5 773 | 7 037 | 926 | 17 136 | −6 140 | 505 | 15 743 | 32 879 | −4 029 |
| Trafic de base prudent, demande des ajouts centrale | 1 620 | 7 558 | 5 028 | 1 348 | 20 028 | −5 966 | 1 734 | 14 725 | 34 752 | 1 905 |
| Trafic de base favorable, demande des ajouts centrale | 10 313 | 13 996 | 10 378 | 7 065 | 27 669 | 1 097 | 2 212 | 25 875 | 53 544 | 30 011 |

**Demande inchangée contre croissance plausible.**
- **Si la demande totale reste la même**, chaque extension **perd de l'argent**. Le client dépense le même budget, et les charges ajoutées restent.
  - Les madeleines perdent le moins (−2 055 €), parce que leur marge (87 %) dépasse celle de S0 (73 %).
  - Le plat du midi (−20 957 €) et S6 (−76 698 €) perdent le plus.
- **Croissance « plausible » retenue** : ≈ 3 visites de plus par jour pour S5 (+3 %), 12,6 pour S5T (+13 %). Elle repose sur deux éléments :
  - des produits introuvables ailleurs (madeleine tiède et macarons au safran) ;
  - le déjeuner, un moment que S0 ne sert pas.
- **Rien ne la prouve.** Le panel simulé attribue au plus 1 à 2 acheteurs sur 20 aux extensions (`consumer-extensions.md`).
- **S5 reste positive sans aucune visite ajoutée** (+8 321 €), grâce aux seuls achats complémentaires. C'est la raison de la recommander.
- **Le plat du midi, lui, dépend entièrement des nouveaux clients du déjeuner** : sans eux, −7 782 €.

## 9. Rentabilité autonome : le travail des fondateurs

| | S0 | S5 | S5T | S6 |
| --- | ---: | ---: | ---: | ---: |
| EBE an 1, fondateurs non payés | −26 215 € | −10 497 € | +7 194 € | −25 646 € |
| EBE an 1, fondateurs payés à 21,25 €/h | −57 155 € | −43 647 € | −29 271 € | −63 768 € |
| EBE an 2, fondateurs non payés | +9 783 € | +29 389 € | +53 071 € | +24 521 € |
| **EBE an 2, fondateurs payés** | **−21 157 €** | **−3 761 €** | **+16 606 €** | −13 602 € |

- **S5 réduit fortement la dépendance au travail gratuit, sans la supprimer** : il manque encore 3 761 € en croisière pour payer Hugo et Laurent.
- Seul S5T devient autonome en année 2, mais grâce au plat du midi, qui est l'hypothèse la moins étayée.

## 10. Verdict de l'outil `founder-plan`

Script `verdicts.py`, mêmes règles que pour S0 : contribution positive, année 1 bénéficiaire, point mort sous la capacité, au moins 25 % d'acheteurs dans le panel.

| scénario | verdict | année 1 (outil, ticket moyen constant) | point mort | panel |
| --- | --- | ---: | ---: | ---: |
| S0 | **Pas encore** | −25 336 € | 91 tickets/jour | 50 % |
| S5 | **Pas encore** | −9 775 € | 86 | 70 % |
| S5T | « Rentable » | +7 900 € | 87 | 70 % (panel S5 : aucun panel n'a vu le plat seul) |
| S6 | **Pas encore** | −17 049 € | 100 | 75 % |

**Le « Rentable » de S5T ne doit pas être lu comme un feu vert.**
- Il repose sur 10 visites de plus par jour au déjeuner, hypothèse non testée.
- Il ne paie pas les fondateurs : en les payant, l'année 1 est à −29 271 €.
- Il suppose un bail qui autorise la remise en température et un traiteur que l'étude n'a pas trouvé.

## 11. Limites du modèle

- Les volumes de base de S0 (95 tickets/jour) restent **la première incertitude**. Les extensions n'y changent rien.
- La perte de 4 places assises dans S6 n'est pas chiffrée, ce qui est favorable à S6.
- Les durées de vie, les minimums de commande et les prix d'achat sont des estimations : **aucun devis**.
- Le chevauchement des desserts et la substitution sont des hypothèses. Le test réel doit les mesurer, au moyen de jours avec et sans extension (`launch-extensions.md`).
