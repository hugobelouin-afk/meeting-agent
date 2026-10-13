# CFO — La Saffranerie (version 2, recalculée après les étapes marketing et ops)

Chiffres tirés de `founder/modele/saffranerie.py` (hypothèses v2, `founder/modele/hypotheses.json`) et de l'outil `unit_economics.py` du skill (annexe C, même point mort). Sources de chaque chiffre : `founder/cfo-sources.md`. **Ce n'est ni un conseil financier, ni un conseil fiscal, ni un conseil juridique.** Un expert-comptable doit valider le montage, la paie, la TVA et l'intégration fiscale avant que l'argent ne circule. Montants HT sauf mention ; « TTC » quand il s'agit de décaissements.

## 1. Note du CFO en sept points

1. **La marge unitaire est bonne.** Ticket moyen de 9,33 € TTC (8,66 € HT), contribution de 6,32 € par ticket, soit 73 % du HT. Le safran coûte peu dans les recettes : 0,10 € par latte, 2,00 € par gramme vendu 22 €.
2. **Le point mort est élevé : 91 tickets par jour, 7 jours sur 7** (843 € TTC par jour, ≈ 25 300 € TTC par mois), avec le planning minimal tenable et sans payer les fondateurs. **En payant leur travail, il en faut 104.** En exploitation autonome, sans les fondateurs au comptoir : 101.
3. **Année 1, scénario central** (95 tickets/jour en croisière, 79 en moyenne sur l'année 1) : EBE de **−26 215 €**, résultat d'exploitation de −41 693 €. **Année 2 : EBE de +9 783 €**, mais −21 157 € si l'on paie le travail des fondateurs. **Sans travail gratuit, le central ne devient pas rentable.**
4. **La ligne à surveiller : la fréquentation.** Volume −20 % : EBE de −62 109 € en année 1. Le scénario prudent (65 tickets/jour) perd environ 77 000 € par an en régime de croisière : il ne s'autofinance jamais. Le prix et le loyer pèsent aussi (point mort de 105 tickets si les prix baissent de 10 % ; 82 avec un loyer de 5 000 €), mais **la fréquentation est l'inconnue n° 1, et rien ne la mesure encore.**
5. **Trésorerie à mobiliser** : **≈ 182 000 € au minimum viable** (fourchette de 127 000 € à 264 000 € selon le bail et les travaux, + 55 000 € par tranche de 50 000 € de droit au bail). **≈ 267 000 € dans la version centrale** et **≈ 297 000 € dans la version confortable**, réserve comprise.
6. **Trois façons d'améliorer le résultat**, chiffrées avec le modèle :
   - **Loyer** : à 5 000 €/mois, le point mort passe de 91 à 82 tickets et l'EBE de l'année 1 gagne 20 000 €. Les deux annonces de la même rue affichent 857 €/m²/an, contre 1 127 €/m²/an pour le local envisagé.
   - **Ticket** : une hausse de 10 % (par le prix ou par davantage de safran et de pots vendus) ramène le point mort à 80 tickets et l'EBE de l'année 1 à −2 014 € (gain de 24 200 €).
   - **Mise de départ** : sans honoraires d'agence, le besoin baisse de 31 200 € ; avec une franchise de loyer pendant les travaux, de 19 400 €. Le point mort ne change pas, mais le risque engagé diminue.
7. **Conditions du board liées à l'argent** :
   - C1 (point mort sans la signature, scénario bas couvert) : **non remplie**. Point mort de 91 sans la signature, et le scénario prudent ne converge pas.
   - C6 (document intra-groupe) : **non remplie**, la cession à 2 €/g est une hypothèse.
   - C9 (exploitation servable) : **remplie sur le papier** avec le planning S2, à condition de donner un statut aux fondateurs.

## 2. Chiffre d'affaires, marge, résultat et trésorerie (scénario central, année 1)

| Notion | Montant | Ce que cela mesure |
| --- | ---: | --- |
| Chiffre d'affaires TTC encaissé | ≈ 264 900 € | l'argent qui entre en caisse, TVA comprise |
| Chiffre d'affaires HT | 245 986 € | les ventes de l'entreprise |
| Marge sur coûts variables | 179 471 € (73 %) | ce qui reste après matières, safran, crème, emballages, pertes et commissions |
| Charges fixes décaissées | 205 686 € | loyer, charges, personnel, communication, etc. |
| EBE | −26 215 € | performance d'exploitation avant amortissements |
| Amortissements | 15 478 € | travaux sur 9 ans, équipements sur 3 à 5 ans |
| Résultat d'exploitation | −41 693 € | perte comptable (IS nul) |
| Trésorerie cumulée au mois 12 (après investissements, TVA remboursée) | ≈ −232 000 € | ce que l'actionnaire a dû apporter |

## 3. TVA : taux et calendrier

| Vente | Taux retenu | Base |
| --- | ---: | --- |
| Tout ce qui est consommé sur place (boissons, viennoiseries, glaces) | 10 % | restauration, BOI-TVA-LIQ-30-10-10 |
| Boissons à emporter en gobelet | 10 % | consommation immédiate (§ 300) |
| Viennoiseries à emporter | 5,5 % | annexe BOI-ANNX-000495 |
| Glace à l'unité (cornet, pot < 200 ml) | 10 % | § 320 |
| Safran en fiole | 5,5 % | produit alimentaire |
| Crème au safran en pot | **5,5 % si pâte à tartiner** (§ 210) ; 20 % si chocolat blanc ou confiserie | **à confirmer** avant l'étiquetage |
| Formule à emporter | taux mixte (≈ 8,8 % pondéré) | ventilation à faire en caisse |

- **Décaissements TTC avant ouverture** : ≈ 238 000 € TTC (central), dont ≈ 34 500 € de TVA récupérable.
- **Calendrier supposé** : régime réel normal mensuel ; TVA nette payée le mois suivant ; **crédit de TVA remboursé environ 2 mois après la demande**. Ce délai est une hypothèse, pas une garantie : un remboursement tardif creuse le besoin d'autant. D'où le bloc « TVA avancée » dans le financement.

## 4. Investissements : ce qui s'amortit, ce qui se récupère, ce qui se consomme (central, HT)

| Nature | Montant | Traitement |
| --- | ---: | --- |
| Immobilisations amortissables (travaux, architecte, enseigne, machine, moulins, froid, four, plonge, mobilier, caisse, congélateur) | 103 500 € | amorties sur 3 à 9 ans |
| Dépôt de garantie | 20 000 € | **récupérable** en fin de bail : ce n'est pas une charge |
| Droit au bail éventuel | 0 € (inconnu, 0 à 100 000 € testés) | immobilisation incorporelle non amortie, revendable avec le bail |
| Dépenses de pré-ouverture consommées (honoraires, avocat, loyers pendant les travaux, crème, marque, INPI, recrutement, lancement, assurances) | 71 233 € | charges (les honoraires peuvent être immobilisés : choix comptable) |
| Stock initial | 9 000 € | actif, consommé à la vente |
| **Total** | **203 733 €** | |

## 5. Financement minimum (scénario central, sans double compte)

| Bloc | Montant |
| --- | ---: |
| 1. Dépenses et engagements avant ouverture (HT) | 194 733 € |
| 2. Stock initial (9 000 €) et TVA avancée non remboursée au creux (34 547 €) | 43 547 € |
| 3. Pertes d'exploitation cumulées jusqu'au creux (mai 2027) | 11 455 € |
| = Besoin maximal simulé sur 24 mois | 249 735 € |
| 4. Réserve pour aléas (10 % des investissements hors dépôt et stock) | 17 473 € |
| **Total à mobiliser** | **267 208 €** |

Après le creux, le remboursement de TVA de juin 2027 améliore la trésorerie de ≈ 35 000 €. Les pertes de l'année 1 consomment ensuite une partie de ce répit. L'actionnaire doit donc disposer de la totalité de la somme dès le départ.

## 6. Trois budgets d'ouverture

| | Minimal viable | Confortable | Ambitieux |
| --- | ---: | ---: | ---: |
| Investissements et pré-ouverture HT | 137 383 € | 217 333 € | 369 433 € |
| Communication (lancement / mensuel) | B : 6 800 € / 650 € | 3B : 20 400 € / 1 950 € | 10B : 68 000 € / 6 500 € |
| Réserve | 10 % | 15 % | 15 % |
| **Total à mobiliser** | **182 183 €** | **297 425 €** | **580 891 €** |
| Point mort (tickets/jour) | 91 | 98 | 122 |
| EBE année 2, à volume égal | +9 783 € | −5 817 € | −60 417 € |

Le détail poste par poste et le statut de chaque ligne (indispensable, différable, facultatif) figurent en annexe B. Ce que coûte chaque version de plus que la précédente : travaux plus complets, architecte, équipements neufs, mobilier, identité de marque plus aboutie, communication 3B ou 10B. **Aucune ne change le point mort à la baisse** ; seules les ventes supplémentaires peuvent justifier l'écart (voir `founder/marketing.md` : il faut environ 19 tickets de plus par jour pour payer 3B, et 83 pour payer 10B).

## 7. Les fondateurs : trésorerie ou rentabilité autonome

| Organisation | Point mort | EBE année 1 | EBE année 2 | Lecture |
| --- | ---: | ---: | ---: | --- |
| S1 : intention du porteur (1 CDI + fondateurs) | 69 | +24 064 € | — | **non tenable** : ≈ 33 h par semaine sans personne, ≈ 40 h de travail gratuit des fondateurs |
| S2 : planning minimal, fondateurs non payés (≈ 28,5 h/semaine) | 91 | −26 215 € | +9 783 € | rentabilité qui **dépend du travail gratuit** |
| S2 en valorisant les fondateurs (21,25 €/h) | 104 | −57 155 € | −21 157 € | **vraie rentabilité de l'activité** |
| S3 : exploitation autonome (responsable payé, fondateurs absents) | 101 | −49 426 € | — | proche de S2 valorisé |

## 8. Scénarios et hypothèses

| | Prudent | Central | Favorable |
| --- | --- | --- | --- |
| Fréquentation en croisière | 65 tickets/j | 95 tickets/j | 135 tickets/j |
| Part de safran et de pots | −30 % | base | +20 % |
| Pourquoi | habitués peu convertis (panel : 1 sur 7), surtout touristes et cadeaux | hypothèse de travail | bouche-à-oreille, une partie des voisins fidélisée |
| EBE année 1 / année 2 | −98 365 € / −76 528 € | −26 215 € / +9 783 € | +70 778 € / +125 800 € |
| Financement avec réserve | 398 794 € **et la trésorerie baisse encore au mois 24** | 267 208 € | 254 511 € |

Rampe d'ouverture : 65 % du volume de croisière au mois 1, 62 % au mois 2, puis progression jusqu'à 100 % au mois 12. Saisonnalité : de 0,82 en janvier à 1,20 en décembre. Ces deux séries sont des estimations (annexe A).

## 9. Ce qui pourrait changer le verdict : une variante plus petite

Simulation sur le même modèle (non retenue comme base) : **boutique-dégustation d'environ 35–40 m², loyer de 3 500 €/mois**, ouverte 6 jours sur 7 de 11h à 19h, 1 CDI + 1 temps partiel de 21 h + fondateurs ≈ 16 h, part de safran et de pots +30 %. Résultat :
- point mort de **59 tickets/jour** (67 en valorisant les fondateurs) ; ticket de 10,49 € TTC ; charges fixes de 10 795 €/mois ;
- financement ≈ 206 000 € (central) ;
- avec des volumes réduits de 40 % par rapport à la rue du Dragon (57 tickets/jour en croisière centrale), l'EBE de l'année 2 reste légèrement négatif (−3 613 €).

**Conclusion** : un local plus petit et moins cher baisse le point mort d'un tiers, mais ne dispense pas de prouver la demande. La question décisive reste la même : **combien de personnes entrent, et combien reviennent ?**

## 10. Vue groupe (Olympus Croci + filiale)

- Safran consommé ou vendu par la boutique en année 1 (central) : ≈ 4,2 kg. À 2 €/g, la marge d'Olympus Croci est de ≈ 1 700 € : **négligeable**. Vendre du safran à la filiale ne rentabilise pas le projet au niveau du groupe.
- Si Olympus Croci détient au moins 95 % de la filiale, l'**intégration fiscale** (art. 223 A du CGI) permettrait d'imputer les pertes de la filiale sur les bénéfices du groupe. L'effet en trésorerie vaudrait au plus le taux d'IS appliqué à la perte. À faire confirmer par l'expert-comptable.
- La boutique peut servir de vitrine aux ventes d'Olympus Croci (en ligne, professionnels). Cet effet **n'est pas modélisé** : faute de donnée, il ne doit pas servir à justifier la décision tant qu'il n'est pas mesuré.

## 11. Ce qui a changé entre la v1 et la v2

| Changement | Effet |
| --- | --- |
| Signature retirée du mix de base (condition C1) | point mort 87 → 91 |
| Lancement B 5 800 € → 6 800 € | besoin +1 000 € |
| Glace partenaire 9,50 → 14 €/L | marge de la glace 75 % → 66 % |
| Provision CFE 100 €/mois | charges fixes +100 € |
| Planning S2 révisé (temps partiel de 21 h ; fondateurs 28,5 h) | masse salariale −198 €/mois ; travail non payé +6,5 h/semaine |
| Résultat | point mort 91 (v1 sans signature : 91) ; 104 en valorisant les fondateurs (v1 : 102) ; financement 267 208 € (v1 : 265 814 €) |


---

## Annexe A — Sortie complète du modèle (v2)

Version des hypothèses : **v2 — 13/10/2026 (après les étapes marketing et ops)**. Généré par `founder/modele/saffranerie.py`. Montants HT sauf mention. Ouverture **hypothétique** le 2027-04-01.

### 1. Ticket moyen pondéré (scénario central, moyenne annuelle pondérée par la saison)

| catégorie | unités pour 100 tickets | CA HT par ticket | part du CA HT |
| --- | ---: | ---: | ---: |
| Boissons | 67,2 | 3,04 € | 35 % |
| Gourmandises | 34,2 | 1,25 € | 14 % |
| Formules | 8,0 | 0,70 € | 8 % |
| Safran | 10,5 | 1,85 € | 21 % |
| Crème en pots et coffrets | 12,7 | 1,82 € | 21 % |
| **Total** | **133 articles** | **8,66 €** | 100 % |

- Ticket moyen : **9,33 € TTC**, 8,66 € HT, coût variable 2,34 € (dont carte 0,14 €), **contribution 6,32 € par ticket (73 % du HT)**.
- Safran consommé : 0,144 g par ticket en moyenne.

### 2. Charges fixes mensuelles (central, planning « S2_minimal »)

| poste | € HT / mois | statut |
| --- | ---: | --- |
| Loyer | 6 667 € | indispensable |
| Charges locatives et taxe foncière refacturées | 800 € | indispensable |
| Énergie et eau | 450 € | indispensable |
| Assurance multirisque et RC professionnelle | 150 € | indispensable |
| Expert-comptable, social et juridique courant | 450 € | indispensable |
| Caisse certifiée, logiciels, terminal de paiement | 100 € | indispensable |
| Internet et téléphone | 50 € | indispensable |
| Entretien, maintenance machine, hygiène, petits consommables | 300 € | indispensable |
| Déchets et biodéchets | 60 € | indispensable |
| Banque | 30 € | indispensable |
| Musique diffusée (SACEM/SPRE) | 40 € | facultatif |
| Dégustations offertes en vitrine | 150 € | indispensable |
| Analyses safran par lot (ISO 3632) et contrôle qualité | 80 € | indispensable |
| Divers et imprévus d'exploitation | 250 € | indispensable |
| CFE (provision) | 100 € | indispensable |
| Personnel : Barista-conseiller CDI 35 h | 2 499 € | indispensable |
| Personnel : Barista-conseiller CDI 35 h | 2 499 € | indispensable |
| Personnel : Équipier temps partiel 21 h | 1 311 € | indispensable |
| Provision absences, congés, dimanches et fériés | 505 € | indispensable |
| Communication mensuelle (budget B) | 650 € | indispensable |
| **Total charges fixes décaissées** | **17 140 €** | |

- Travail des fondateurs non rémunéré dans ce planning : 28 h/semaine, valorisé à 2 578 €/mois au coût d'un responsable de boutique.
- La CFE est provisionnée (estimation) ; les amortissements ne font pas partie des charges fixes décaissées.

### 3. Point mort (scénario central)

| | sans valoriser les fondateurs | en valorisant le travail des fondateurs | avec la boisson signature (si test réussi) |
| --- | ---: | ---: | ---: |
| Charges fixes / mois | 17 140 € | 19 719 € | 17 140 € |
| CA HT / mois | 23 494 € | 27 028 € | 23 267 € |
| CA TTC / mois (équivalent) | 25 303 € | 29 109 € | 25 074 € |
| CA TTC / jour | 843 € | 970 € | 836 € |
| **Tickets / jour** | **91** | **104** | **87** |
| Tickets / heure d'ouverture (moyenne) | 10,0 | 11,6 | 9,7 |
| Tickets à l'heure de pointe (15 % du jour) | 13,6 | 15,6 | 13,0 |

Produits vendus par jour au point mort (sans valorisation) :

- Boissons : 60,7
- Gourmandises : 30,9
- Formules : 7,2
- Safran : 9,5
- Crème en pots et coffrets : 11,5

### 4. Capacité de service

- Temps de service moyen par ticket (préparation + conseil + encaissement) : 130 s.
- Une personne seule : **23,5 tickets/heure** au rythme soutenable (85 % d'utilisation) ; deux personnes : **42,3 tickets/heure**.
- Capacité journalière avec le planning retenu (renfort 38 h/semaine) : **≈ 313 tickets/jour**.
- Point mort à l'heure de pointe : 13,6 tickets, contre 23,5 pour une personne seule : une personne seule suffit en théorie, sans marge pour le conseil safran.

### 5. Trois scénarios — première année (planning retenu, communication B)

| | prudent | central | favorable |
| --- | ---: | ---: | ---: |
| Tickets/jour en croisière (hypothèse) | 65 | 95 | 135 |
| Tickets/jour moyens sur l'année 1 | 54 | 79 | 113 |
| Ticket moyen TTC (annuel) | 8,17 € | 9,33 € | 10,11 € |
| CA HT année 1 | 146 524 € | 245 986 € | 379 718 € |
| Marge sur coûts variables | 107 321 € | 179 471 € | 276 464 € |
| Charges fixes décaissées | 205 686 € | 205 686 € | 205 686 € |
| **EBE année 1 (fondateurs non payés)** | **−98 365 €** | **−26 215 €** | **70 778 €** |
| Amortissements | 15 478 € | 15 478 € | 15 478 € |
| Résultat d'exploitation | −113 843 € | −41 693 € | 55 300 € |
| **EBE en valorisant le travail des fondateurs** | **−129 305 €** | **−57 155 €** | **39 838 €** |
| Point mort tickets/jour (fondateurs non payés) | 104 | 91 | 84 |
| Point mort tickets/jour (fondateurs valorisés) | 119 | 104 | 97 |
| EBE année 2 (croisière, fondateurs non payés) | −76 528 € | 9 783 € | 125 800 € |
| EBE année 2 en valorisant les fondateurs | −107 468 € | −21 157 € | 94 860 € |
| Besoin de trésorerie maximal sur 24 mois (hors réserve) | 381 321 € **et toujours en baisse au mois 24** | 249 735 € | 237 038 € |
| Mois du creux | mars 2029 | mai 2027 | avr. 2027 |
| **Financement minimum avec réserve** | **398 794 €** | **267 208 €** | **254 511 €** |

### 6. Première année mois par mois — scénario central

| mois | tickets/j | ticket TTC | CA HT | marge s/ coûts var. | charges fixes | EBE | résultat | TVA (flux) | flux de trésorerie | trésorerie cumulée |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| janv. 2027 | 0 | — | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | −5 800 € | −5 800 € |
| févr. 2027 | 0 | — | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | −72 800 € | −78 600 € |
| mars 2027 | 0 | — | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | −137 120 € | −215 720 € |
| avr. 2027 | 64 | 9,67 € | 17 092 € | 12 467 € | 17 140 € | −4 673 € | −5 963 € | 0 € | −28 289 € | −244 008 € |
| mai 2027 | 64 | 9,67 € | 17 095 € | 12 469 € | 17 140 € | −4 671 € | −5 961 € | 0 € | −5 727 € | −249 735 € |
| juin 2027 | 72 | 9,67 € | 19 301 € | 14 078 € | 17 140 € | −3 062 € | −4 352 € | 35 602 € | 31 604 € | −218 131 € |
| juil. 2027 | 74 | 9,67 € | 19 791 € | 14 436 € | 17 140 € | −2 705 € | −3 995 € | 1 055 € | −2 559 € | −220 690 € |
| août 2027 | 68 | 9,67 € | 18 198 € | 13 274 € | 17 140 € | −3 867 € | −5 157 € | 936 € | −3 926 € | −224 617 € |
| sept. 2027 | 85 | 9,67 € | 22 786 € | 16 620 € | 17 140 € | −520 € | −1 810 € | 910 € | −359 € | −224 975 € |
| oct. 2027 | 87 | 8,22 € | 19 960 € | 14 602 € | 17 140 € | −2 539 € | −3 829 € | 996 € | −2 510 € | −227 486 € |
| nov. 2027 | 85 | 9,27 € | 21 969 € | 16 018 € | 17 140 € | −1 123 € | −2 412 € | 748 € | −1 298 € | −228 784 € |
| déc. 2027 | 108 | 11,03 € | 33 469 € | 24 302 € | 17 140 € | 7 162 € | 5 872 € | 967 € | 7 647 € | −221 137 € |
| janv. 2028 | 76 | 8,22 € | 17 318 € | 12 669 € | 17 140 € | −4 471 € | −5 761 € | 924 € | −4 648 € | −225 785 € |
| févr. 2028 | 80 | 8,22 € | 18 322 € | 13 404 € | 17 140 € | −3 737 € | −5 027 € | 481 € | −4 305 € | −230 091 € |
| mars 2028 | 90 | 8,22 € | 20 685 € | 15 132 € | 17 140 € | −2 009 € | −3 298 € | 1 101 € | −1 838 € | −231 928 € |

Les mois avant l'ouverture portent les investissements TTC ; la TVA récupérable revient avec un délai de 2 mois (hypothèse).

### 7. Financement minimum — scénario central

| bloc | montant | contenu |
| --- | ---: | --- |
| 1. Dépenses et engagements avant ouverture (HT) | 194 733 € | dépôt de garantie 20 000 € (récupérable en fin de bail), honoraires, travaux, équipements, loyers pendant travaux, marque, crème, lancement |
| 2. Stock initial et TVA avancée non encore remboursée au creux | 43 547 € | stock 9 000 € + TVA avancée 34 547 € |
| 3. Pertes d'exploitation cumulées jusqu'au creux (montée en puissance) | 11 455 € | creux en mai 2027 |
| = Besoin maximal simulé | 249 735 € | |
| 4. Réserve pour aléas (10 % des investissements hors dépôt et stock) | 17 473 € | travaux et équipements dans un local non visité |
| **Total à mobiliser** | **267 208 €** | |

### 8. Sensibilités (scénario central, une variable à la fois)

| variable | point mort tickets/j | EBE année 1 | besoin + réserve |
| --- | ---: | ---: | ---: |
| Base centrale | 91 | −26 215 € | 267 208 € |
| Prix de tous les produits −10 % | 105 | −50 417 € | 293 165 € |
| Prix de tous les produits +10 % | 80 | −2 014 € | 263 573 € |
| Volume −20 % | 91 | −62 109 € | 318 995 € |
| Volume +20 % | 91 | 9 679 € | 261 851 € |
| Coût de la crème +30 % | 93 | −29 435 € | 267 648 € |
| Crème produite en interne | 88 | −20 552 € | 266 435 € |
| Pertes doublées | 92 | −28 912 € | 267 651 € |
| Safran cédé à 6 €/g | 100 | −43 280 € | 277 189 € |
| Safran cédé à 12 €/g | 119 | −68 877 € | 333 559 € |
| Avec la boisson signature (si test réussi) | 87 | −19 106 € | 266 161 € |
| Planning S1 (intention : 1 salarié + fondateurs) — NON TENABLE, voir ops | 69 | 24 064 € | 258 828 € |
| Planning S3 (exploitation autonome) | 101 | −49 426 € | 286 031 € |
| Fondateurs valorisés (S2) | 104 | −57 155 € | 301 490 € |
| Loyer −25 % (autre local, ≈ 5 000 €) | 82 | −6 215 € | 263 208 € |
| Loyer +12,5 % (7 500 €, comme les annonces voisines) | 95 | −36 215 € | 269 208 € |
| Charges fixes hors personnel au maximum de fourchette | 100 | −47 575 € | 282 874 € |
| Communication 3B (mensuel ×3, lancement ×3) | 98 | −41 815 € | 286 648 € |
| Communication 10B (mensuel ×10, lancement ×10) | 122 | −96 415 € | 443 550 € |
| Droit au bail 50 000 € | 91 | −26 215 € | 322 208 € |
| Droit au bail 100 000 € | 91 | −26 215 € | 377 208 € |
| Travaux au maximum (95 000 €) | 91 | −26 215 € | 319 208 € |
| Pas d'agence (honoraires 0 €) | 91 | −26 215 € | 236 008 € |
| Franchise de loyer pendant les travaux | 91 | −26 215 € | 247 795 € |

### 9. Vue groupe (Olympus Croci + filiale), sans double compte

- Safran consommé ou vendu par la boutique en année 1 (central) : **4 152 g** (4,15 kg).
- Marge d'Olympus Croci sur ce safran au prix de cession de 2,00 €/g (coût 1,60 €/g) : **1 661 €**. Elle s'ajoute à l'EBE de la boutique (−26 215 €) pour la vue consolidée : −24 554 €.
- Le capital apporté par Olympus Croci est compté une seule fois, comme ressource de la filiale. La marge interne ne crée pas de trésorerie pour le groupe : elle déplace la marge d'une société à l'autre.



---

## Annexe B — Budgets d'ouverture poste par poste

Scénario de volume **central** dans les trois cas : on ne suppose pas que dépenser plus fait vendre plus (voir founder/marketing.md pour la contribution nécessaire). Montants HT sauf mention ; hypothèses v2 — 13/10/2026 (après les étapes marketing et ops).

| poste | statut | minimal viable | confortable | ambitieux |
| --- | --- | ---: | ---: | ---: |
| Dépôt de garantie (3 mois de loyer HT) | indispensable | 20 000 € | 20 000 € | 20 000 € |
| Honoraires d'agence (preneur) | indispensable si agence | 24 000 € | 24 000 € | 24 000 € |
| Droit au bail / pas-de-porte | inconnu | 0 € | 0 € | 0 € |
| Rédaction du bail, avocat, création de la société | indispensable | 2 000 € | 4 000 € | 7 000 € |
| Loyer et charges pendant les travaux (2 mois) | indispensable sauf franchise | 14 933 € | 14 933 € | 14 933 € |
| Travaux d'aménagement (comptoir, électricité, plomberie, sol, éclairage, peinture, accessibilité) | indispensable | 30 000 € | 55 000 € | 95 000 € |
| Architecte d'intérieur / maîtrise d'œuvre | différable | 0 € | 6 000 € | 12 000 € |
| Enseigne, vitrophanie, signalétique (avec déclaration préalable) | indispensable | 2 000 € | 4 000 € | 8 000 € |
| Machine espresso 2 groupes | indispensable | 5 000 € | 9 500 € | 13 000 € |
| Moulins (espresso + décaféiné/filtre), filtration d'eau | indispensable | 2 000 € | 3 500 € | 5 000 € |
| Four à viennoiseries, froid positif et négatif, vitrine réfrigérée | indispensable | 6 000 € | 9 000 € | 14 000 € |
| Lave-vaisselle professionnel, plonge, petit matériel, vaisselle réemployable | indispensable | 3 500 € | 5 500 € | 8 000 € |
| Mobilier (tabourets, tables basses) et présentoirs de vente | indispensable | 4 000 € | 8 000 € | 15 000 € |
| Caisse certifiée, terminal, tablette, balance | indispensable | 800 € | 1 500 € | 2 500 € |
| Congélateur glaces (format pots du partenaire, sans vitrine à boules) | différable | 0 € | 1 500 € | 6 000 € |
| Crème : analyses (vieillissement, microbiologie, nutrition), étiquetage, lancement façonnier | indispensable | 3 500 € | 6 000 € | 10 000 € |
| Identité de marque, design packaging, site vitrine | indispensable (version minimale) | 3 000 € | 8 000 € | 20 000 € |
| Dépôt de marque INPI et recherches d'antériorité | indispensable | 350 € | 1 000 € | 2 500 € |
| Recrutement, formation hygiène (HACCP), salaires avant ouverture (2 semaines) | indispensable | 2 500 € | 4 500 € | 7 000 € |
| Communication de lancement (budget B) | indispensable | 6 800 € | 20 400 € | 68 000 € |
| Stock initial (safran conditionné, pots de crème, café, emballages) | indispensable | 6 000 € | 9 000 € | 14 000 € |
| Assurances, frais bancaires et divers avant ouverture | indispensable | 1 000 € | 2 000 € | 3 500 € |
| **Total investissements et pré-ouverture HT** | | 137 383 € | 217 333 € | 369 433 € |

| financement | minimal viable | confortable | ambitieux |
| --- | ---: | ---: | ---: |
| 1. Dépenses et engagements avant ouverture (HT) | 131 383 € | 208 333 € | 355 433 € |
| 2. Stock initial + TVA avancée au creux | 28 207 € | 46 267 € | 14 000 € |
| 3. Pertes d'exploitation jusqu'au creux | 11 455 € | 14 575 € | 161 143 € |
| Besoin maximal simulé (24 mois) | 171 045 € | 269 175 € | 530 576 € |
| 4. Réserve pour aléas | 11 138 € (10 %) | 28 250 € (15 %) | 50 315 € (15 %) |
| **Total à mobiliser** | **182 183 €** | **297 425 €** | **580 891 €** |
| Communication : lancement / mensuel | 6 800 € / 650 € | 20 400 € / 1 950 € | 68 000 € / 6 500 € |
| Point mort (tickets/jour) | 91 | 98 | 122 |
| EBE année 1 (central, sans hausse de ventes) | −26 215 € | −41 815 € | −96 415 € |
| EBE année 2 | 9 783 € | −5 817 € | −60 417 € |
| Trésorerie cumulée à 24 mois (hors apport) | −155 786 € | −267 456 € | −530 576 € |


---

## Annexe C — Sortie de l'outil unit_economics.py du skill founder-cfo

Chaque chiffre vient du fichier d'entrée `founder/numbers.json` (généré par le modèle). Sortie traduite ; aucun chiffre modifié.

### Un ticket

| ligne | par ticket |
| --- | ---: |
| Prix HT | 8,66 € |
| Matières, safran (prix de cession) et crème | −1,99 € |
| Emballages et pertes | −0,21 € |
| Commissions carte | −0,14 € |
| **Contribution** (ce que chaque ticket laisse pour payer les charges fixes) | **6,32 €** (73 %) |

### La marge qui compte

Charges fixes : 17 140 € par mois (Loyer 6 667 €, Charges locatives et taxe foncière refacturées 800 €, Énergie et eau 450 €, Assurance multirisque et RC professionnelle 150 €, Expert-comptable, social et juridique courant 450 €, Caisse certifiée, logiciels, terminal de paiement 100 €, Internet et téléphone 50 €, Entretien, maintenance machine, hygiène, petits consommables 300 €, Déchets et biodéchets 60 €, Banque 30 €, Musique diffusée (SACEM/SPRE) 40 €, Dégustations offertes en vitrine 150 €, Analyses safran par lot (ISO 3632) et contrôle qualité 80 €, Divers et imprévus d'exploitation 250 €, CFE (provision) 100 €, Personnel (S2_minimal) 6 814 €, Communication mensuelle (B) 650 €).

- **Point mort : 91 tickets par jour.** En dessous, chaque mois est en perte.
- **Marge nette au volume prévu** (95 par jour) : **4 %** de chaque vente, après tous les coûts.
- Capacité : 313 par jour.

### Année 1, mois par mois

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

### Et si…

| scénario | marge au volume prévu | point mort par jour | résultat année 1 |
| --- | ---: | ---: | ---: |
| Plan de base | 4 % | 91 | −25 336 € |
| Prix −10 % | -7 % | 105 | −50 056 € |
| Volume −20 % | -14 % | 91 | −61 406 € |
| Coûts unitaires +15 % | -1 % | 96 | −35 364 € |

### Signaux d'alerte

- L'année 1 perd de l'argent en exploitation (−25 336 €).
- L'investissement n'est pas remboursé dans l'année 1.
