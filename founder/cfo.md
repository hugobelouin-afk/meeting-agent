# CFO — La Saffranerie (version 1, avant les étapes ops et marketing)

> Cette note sera recalculée après /founder-marketing et /founder-ops (consigne du porteur). Les chiffres viennent de `founder/modele/saffranerie.py` (hypothèses v1) et de l'outil `unit_economics.py` du skill (`founder/cfo-outil.md`), qui donnent le même point mort. Ce n'est ni un conseil financier, ni un conseil fiscal, ni un conseil juridique : un expert-comptable doit valider le montage, la paie et la TVA avant que l'argent ne circule.

## Note du CFO

- **La marge unitaire est bonne.** Ticket moyen 9,33 € TTC (8,66 € HT) ; contribution de 6,36 € par ticket, soit 73 % du HT. Le safran pèse peu dans les coûts : 0,10 € par latte, 2,00 € par gramme vendu 22 €.
- **Le point mort est élevé.** Avec le planning minimal tenable (2 CDI, 1 temps partiel, Hugo 22 h/semaine non payé), il faut **91 tickets par jour, 7 jours sur 7**. C'est 844 € TTC par jour, soit environ 25 300 € TTC par mois. En payant le travail d'Hugo, il en faut **102 par jour**.
- **Résultat de l'année 1** (scénario central : 95 tickets/jour en croisière, 79 en moyenne sur l'année 1) : EBE de **−26 509 €** sans payer les fondateurs. **Année 2 : +9 816 €**, soit à peine l'équilibre. Si l'on paie le travail d'Hugo, l'année 2 reste négative (−14 494 €).
- **La ligne à surveiller : la fréquentation.** Volume −20 % : EBE de −62 579 € en année 1. Loyer −25 % : point mort de 82 tickets. Prix −10 % : 105 tickets. Le prix et le loyer pèsent beaucoup, mais **le volume réel est l'inconnue n° 1**, et rien ne le mesure encore.
- **Trésorerie à mobiliser** (scénario central, réserve comprise) : **≈ 266 000 €**. Fourchette selon le budget : 181 000 € (minimal viable) à 570 000 € (ambitieux). Dans le scénario prudent, la trésorerie baisse encore au mois 24 : **ce scénario ne s'autofinance jamais**.
- **Trois façons d'améliorer la marge**, chiffrées avec le modèle :
  1. Négocier le loyer ou choisir un autre local. À 5 000 €/mois, le point mort passe de 91 à 82 tickets et l'EBE de l'année 1 gagne 20 000 €.
  2. Augmenter la part de safran et de pots. Ils représentent 41 % du CA HT dans l'hypothèse centrale, avec des marges de 57 à 83 %. Un ticket +10 % fait gagner environ 24 000 € d'EBE sur l'année 1 (sensibilité « prix +10 % » : 80 tickets).
  3. Supprimer les honoraires d'agence (−31 000 € de besoin, réserve comprise) et obtenir une franchise de loyer pendant les travaux (−19 000 €). Cela ne change pas le point mort, mais réduit la mise de départ.
- **Conditions du board liées à l'argent** : C1 (point mort sans la signature, scénario bas couvert) **non remplie**. Le point mort sans la signature est de 91 tickets, et le scénario prudent ne converge pas. C6 (document intra-groupe) **non remplie** : la cession à 2 €/g est une hypothèse.
## Annexe A — Modèle financier détaillé — La Saffranerie

Version des hypothèses : **v1 — 13/10/2026 (avant les étapes ops et marketing)**. Généré par `founder/modele/saffranerie.py`. Montants HT sauf mention. Ouverture **hypothétique** le 2027-04-01.

## 1. Ticket moyen pondéré (scénario central, moyenne annuelle pondérée par la saison)

| catégorie | unités pour 100 tickets | CA HT par ticket | part du CA HT |
| --- | ---: | ---: | ---: |
| Boissons | 67,2 | 3,04 € | 35 % |
| Gourmandises | 34,2 | 1,25 € | 14 % |
| Formules | 8,0 | 0,70 € | 8 % |
| Safran | 10,5 | 1,85 € | 21 % |
| Crème en pots et coffrets | 12,7 | 1,82 € | 21 % |
| **Total** | **133 articles** | **8,66 €** | 100 % |

- Ticket moyen : **9,33 € TTC**, 8,66 € HT, coût variable 2,31 € (dont carte 0,14 €), **contribution 6,36 € par ticket (73 % du HT)**.
- Safran consommé : 0,144 g par ticket en moyenne.

## 2. Charges fixes mensuelles (central, planning « S2_minimal »)

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
| Personnel : Barista-conseiller CDI 35 h | 2 499 € | indispensable |
| Personnel : Barista-conseiller CDI 35 h | 2 499 € | indispensable |
| Personnel : Équipier temps partiel 24 h (week-end + 2 après-midi) | 1 494 € | indispensable |
| Provision absences, congés, dimanches et fériés | 519 € | indispensable |
| Communication mensuelle (budget B) | 650 € | indispensable |
| **Total charges fixes décaissées** | **17 238 €** | |

- Travail des fondateurs non rémunéré dans ce planning : 22 h/semaine, valorisé à 2 026 €/mois au coût d'un responsable de boutique.
- CFE non comptée en année 1 (exonération l'année de création, à confirmer) ; amortissements hors charges fixes décaissées.

## 3. Point mort (scénario central)

| | sans valoriser les fondateurs | en valorisant le travail des fondateurs | avec la boisson signature (si test réussi) |
| --- | ---: | ---: | ---: |
| Charges fixes / mois | 17 238 € | 19 264 € | 17 238 € |
| CA HT / mois | 23 497 € | 26 258 € | 23 275 € |
| CA TTC / mois (équivalent) | 25 305 € | 28 279 € | 25 082 € |
| CA TTC / jour | 844 € | 943 € | 836 € |
| **Tickets / jour** | **91** | **102** | **87** |
| Tickets / heure d'ouverture (moyenne) | 10,0 | 11,2 | 9,7 |
| Tickets à l'heure de pointe (15 % du jour) | 13,6 | 15,2 | 13,0 |

Produits vendus par jour au point mort (sans valorisation) :

- Boissons : 60,7
- Gourmandises : 30,9
- Formules : 7,2
- Safran : 9,5
- Crème en pots et coffrets : 11,5

## 4. Capacité de service

- Temps de service moyen par ticket (préparation + conseil + encaissement) : 130 s.
- Une personne seule : **23,5 tickets/heure** au rythme soutenable (85 % d'utilisation) ; deux personnes : **42,3 tickets/heure**.
- Capacité journalière avec le planning retenu (renfort 40 h/semaine) : **≈ 319 tickets/jour**.
- Point mort à l'heure de pointe : 13,6 tickets, contre 23,5 pour une personne seule : une personne seule suffit en théorie, sans marge pour le conseil safran.

## 5. Trois scénarios — première année (planning retenu, communication B)

| | prudent | central | favorable |
| --- | ---: | ---: | ---: |
| Tickets/jour en croisière (hypothèse) | 65 | 95 | 135 |
| Tickets/jour moyens sur l'année 1 | 54 | 79 | 113 |
| Ticket moyen TTC (annuel) | 8,17 € | 9,33 € | 10,11 € |
| CA HT année 1 | 146 524 € | 245 986 € | 379 718 € |
| Marge sur coûts variables | 107 922 € | 180 349 € | 277 712 € |
| Charges fixes décaissées | 206 858 € | 206 858 € | 206 858 € |
| **EBE année 1 (fondateurs non payés)** | **−98 936 €** | **−26 509 €** | **70 854 €** |
| Amortissements | 15 478 € | 15 478 € | 15 478 € |
| Résultat d'exploitation | −114 414 € | −41 987 € | 55 376 € |
| **EBE en valorisant le travail des fondateurs** | **−123 246 €** | **−50 819 €** | **46 544 €** |
| Point mort tickets/jour (fondateurs non payés) | 104 | 91 | 84 |
| Point mort tickets/jour (fondateurs valorisés) | 116 | 102 | 94 |
| EBE année 2 (croisière, fondateurs non payés) | −76 875 € | 9 816 € | 126 340 € |
| EBE année 2 en valorisant les fondateurs | −101 185 € | −14 494 € | 102 030 € |
| Besoin de trésorerie maximal sur 24 mois (hors réserve) | 381 240 € **et toujours en baisse au mois 24** | 248 441 € | 235 730 € |
| Mois du creux | mars 2029 | mai 2027 | avr. 2027 |
| **Financement minimum avec réserve** | **398 613 €** | **265 814 €** | **253 104 €** |

## 6. Première année mois par mois — scénario central

| mois | tickets/j | ticket TTC | CA HT | marge s/ coûts var. | charges fixes | EBE | résultat | TVA (flux) | flux de trésorerie | trésorerie cumulée |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| janv. 2027 | 0 | — | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | −5 800 € | −5 800 € |
| févr. 2027 | 0 | — | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | −72 800 € | −78 600 € |
| mars 2027 | 0 | — | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | −137 120 € | −215 720 € |
| avr. 2027 | 64 | 9,67 € | 17 092 € | 12 599 € | 17 238 € | −4 639 € | −5 929 € | 0 € | −27 042 € | −242 761 € |
| mai 2027 | 64 | 9,67 € | 17 095 € | 12 601 € | 17 238 € | −4 638 € | −5 927 € | 0 € | −5 680 € | −248 441 € |
| juin 2027 | 72 | 9,67 € | 19 301 € | 14 227 € | 17 238 € | −3 012 € | −4 301 € | 35 389 € | 31 456 € | −216 985 € |
| juil. 2027 | 74 | 9,67 € | 19 791 € | 14 588 € | 17 238 € | −2 650 € | −3 940 € | 1 042 € | −2 503 € | −219 488 € |
| août 2027 | 68 | 9,67 € | 18 198 € | 13 414 € | 17 238 € | −3 825 € | −5 114 € | 921 € | −3 885 € | −223 373 € |
| sept. 2027 | 85 | 9,67 € | 22 786 € | 16 795 € | 17 238 € | −443 € | −1 733 € | 894 € | −279 € | −223 652 € |
| oct. 2027 | 87 | 8,22 € | 19 960 € | 14 602 € | 17 238 € | −2 637 € | −3 926 € | 982 € | −2 622 € | −226 273 € |
| nov. 2027 | 85 | 9,27 € | 21 969 € | 16 018 € | 17 238 € | −1 220 € | −2 510 € | 730 € | −1 414 € | −227 687 € |
| déc. 2027 | 108 | 11,03 € | 33 469 € | 24 302 € | 17 238 € | 7 064 € | 5 774 € | 967 € | 7 549 € | −220 138 € |
| janv. 2028 | 76 | 8,22 € | 17 318 € | 12 669 € | 17 238 € | −4 569 € | −5 859 € | 924 € | −4 746 € | −224 884 € |
| févr. 2028 | 80 | 8,22 € | 18 322 € | 13 404 € | 17 238 € | −3 834 € | −5 124 € | 481 € | −4 403 € | −229 287 € |
| mars 2028 | 90 | 8,22 € | 20 685 € | 15 132 € | 17 238 € | −2 106 € | −3 396 € | 1 101 € | −1 936 € | −231 222 € |

Les mois avant l'ouverture portent les investissements TTC ; la TVA récupérable revient avec un délai de 2 mois (hypothèse).

## 7. Financement minimum — scénario central

| bloc | montant | contenu |
| --- | ---: | --- |
| 1. Dépenses et engagements avant ouverture (HT) | 193 733 € | dépôt de garantie 20 000 € (récupérable en fin de bail), honoraires, travaux, équipements, loyers pendant travaux, marque, crème, lancement |
| 2. Stock initial et TVA avancée non encore remboursée au creux | 43 347 € | stock 9 000 € + TVA avancée 34 347 € |
| 3. Pertes d'exploitation cumulées jusqu'au creux (montée en puissance) | 11 362 € | creux en mai 2027 |
| = Besoin maximal simulé | 248 441 € | |
| 4. Réserve pour aléas (10 % des investissements hors dépôt et stock) | 17 373 € | travaux et équipements dans un local non visité |
| **Total à mobiliser** | **265 814 €** | |

## 8. Sensibilités (scénario central, une variable à la fois)

| variable | point mort tickets/j | EBE année 1 | besoin + réserve |
| --- | ---: | ---: | ---: |
| Base centrale | 91 | −26 509 € | 265 814 € |
| Prix de tous les produits −10 % | 105 | −50 710 € | 292 326 € |
| Prix de tous les produits +10 % | 80 | −2 308 € | 262 179 € |
| Volume −20 % | 91 | −62 579 € | 318 573 € |
| Volume +20 % | 91 | 9 561 € | 260 400 € |
| Coût de la crème +30 % | 93 | −29 729 € | 266 254 € |
| Crème produite en interne | 88 | −20 846 € | 265 041 € |
| Pertes doublées | 92 | −29 126 € | 266 231 € |
| Safran cédé à 6 €/g | 100 | −43 574 € | 276 350 € |
| Safran cédé à 12 €/g | 118 | −69 171 € | 332 720 € |
| Avec la boisson signature (si test réussi) | 87 | −19 400 € | 264 767 € |
| Planning S1 (intention : 1 salarié + fondateurs) — NON TENABLE, voir ops | 68 | 26 143 € | 257 039 € |
| Planning S3 (exploitation autonome) | 101 | −48 929 € | 283 611 € |
| Fondateurs valorisés (S2) | 102 | −50 819 € | 287 391 € |
| Loyer −25 % (autre local, ≈ 5 000 €) | 82 | −6 509 € | 261 814 € |
| Loyer +12,5 % (7 500 €, comme les annonces voisines) | 95 | −36 509 € | 267 814 € |
| Charges fixes hors personnel au maximum de fourchette | 99 | −46 069 € | 278 435 € |
| Communication 3B (mensuel ×3, lancement ×3) | 98 | −42 109 € | 282 854 € |
| Communication 10B (mensuel ×10, lancement ×10) | 122 | −96 709 € | 433 711 € |
| Droit au bail 50 000 € | 91 | −26 509 € | 320 814 € |
| Droit au bail 100 000 € | 91 | −26 509 € | 375 814 € |
| Travaux au maximum (95 000 €) | 91 | −26 509 € | 317 814 € |
| Pas d'agence (honoraires 0 €) | 91 | −26 509 € | 234 614 € |
| Franchise de loyer pendant les travaux | 91 | −26 509 € | 246 402 € |

## 9. Vue groupe (Olympus Croci + filiale), sans double compte

- Safran consommé ou vendu par la boutique en année 1 (central) : **4 152 g** (4,15 kg).
- Marge d'Olympus Croci sur ce safran au prix de cession de 2,00 €/g (coût 1,60 €/g) : **1 661 €**. Elle s'ajoute à l'EBE de la boutique (−26 509 €) pour la vue consolidée : −24 848 €.
- Le capital apporté par Olympus Croci est compté une seule fois, comme ressource de la filiale. La marge interne ne crée pas de trésorerie pour le groupe : elle déplace la marge d'une société à l'autre.

## Annexe B — Économie unitaire (outil unit_economics.py) : La Saffranerie (rue du Dragon) — unité = ticket moyen, montants HT en euros

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
