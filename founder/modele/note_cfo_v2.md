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
