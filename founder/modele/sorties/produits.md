# Coût et marge par produit — La Saffranerie

Généré par `founder/modele/saffranerie.py` à partir de `founder/modele/hypotheses.json` (v2 — 13/10/2026 (après les étapes marketing et ops)).
Prix TTC proposés ; HT calculé avec la TVA sur place / à emporter et la part consommée sur place ; safran au prix de cession (2,00 €/g) ; crème au coût complet (29,23 €/kg, mode « faconnier »). Pertes = % des matières. Carte bancaire = 1,5 % du TTC.

Statuts : ouverture, saison (avril–septembre), ouverture_si_test (signature : seulement si le test de faisabilité est concluant), report (après preuve de demande et faisabilité de la cuisson), retire (non recommandé).

| produit | statut | prix TTC | HT moyen | matières | safran | crème | emballage | pertes | carte | coût variable | marge € | marge % |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Espresso | ouverture | 3,00 € | 2,73 € | 0,42 € | 0,00 € | 0,00 € | 0,07 € | 0,02 € | 0,04 € | 0,55 € | 2,17 € | 80 % |
| Latte / café crème 30 cl | ouverture | 5,00 € | 4,55 € | 0,70 € | 0,00 € | 0,00 € | 0,12 € | 0,03 € | 0,07 € | 0,92 € | 3,62 € | 80 % |
| Latte au safran 30 cl (non sucré) | ouverture | 6,00 € | 5,45 € | 0,72 € | 0,10 € | 0,00 € | 0,12 € | 0,03 € | 0,09 € | 1,06 € | 4,39 € | 80 % |
| Latte frappé 40 cl | saison | 5,50 € | 5,00 € | 0,70 € | 0,00 € | 0,00 € | 0,17 € | 0,03 € | 0,08 € | 0,98 € | 4,02 € | 80 % |
| Latte frappé au safran 40 cl (glaçons de safran) | saison | 6,50 € | 5,91 € | 0,72 € | 0,12 € | 0,00 € | 0,17 € | 0,04 € | 0,10 € | 1,14 € | 4,76 € | 81 % |
| Thé en feuilles | ouverture | 4,50 € | 4,09 € | 0,20 € | 0,00 € | 0,00 € | 0,10 € | 0,01 € | 0,07 € | 0,37 € | 3,72 € | 91 % |
| Infusion de safran (thé blanc ou nature) | ouverture | 5,50 € | 5,00 € | 0,12 € | 0,12 € | 0,00 € | 0,10 € | 0,01 € | 0,08 € | 0,42 € | 4,58 € | 92 % |
| Signature « Or blanc » : infusion claire + cristal de sucre au safran | ouverture_si_test | 6,50 € | 5,91 € | 0,25 € | 0,12 € | 0,00 € | 0,11 € | 0,02 € | 0,10 € | 0,60 € | 5,31 € | 90 % |
| Croissant pur beurre | ouverture | 2,20 € | 2,06 € | 0,62 € | 0,00 € | 0,00 € | 0,03 € | 0,09 € | 0,03 € | 0,78 € | 1,28 € | 62 % |
| Croissant fourré à la crème au safran | ouverture | 4,50 € | 4,21 € | 0,62 € | 0,00 € | 0,88 € | 0,04 € | 0,15 € | 0,07 € | 1,75 € | 2,46 € | 58 % |
| Glace safran (partenaire) 1 boule | saison | 4,00 € | 3,64 € | 0,98 € | 0,00 € | 0,00 € | 0,12 € | 0,10 € | 0,06 € | 1,25 € | 2,38 € | 66 % |
| Glace 2 boules (safran + un parfum) | saison | 6,50 € | 5,91 € | 1,96 € | 0,00 € | 0,00 € | 0,12 € | 0,20 € | 0,10 € | 2,37 € | 3,54 € | 60 % |
| Crêpe sucre | report | 4,50 € | 4,09 € | 0,28 € | 0,00 € | 0,00 € | 0,07 € | 0,02 € | 0,07 € | 0,43 € | 3,66 € | 89 % |
| Crêpe Nutella | retire | 6,00 € | 5,45 € | 0,49 € | 0,00 € | 0,00 € | 0,07 € | 0,03 € | 0,09 € | 0,68 € | 4,78 € | 88 % |
| Crêpe à la crème au safran | report | 7,00 € | 6,36 € | 0,20 € | 0,00 € | 1,02 € | 0,07 € | 0,07 € | 0,10 € | 1,47 € | 4,89 € | 77 % |
| Gaufre sucre | report | 5,00 € | 4,55 € | 0,43 € | 0,00 € | 0,00 € | 0,07 € | 0,03 € | 0,07 € | 0,61 € | 3,94 € | 87 % |
| Gaufre Nutella | retire | 6,50 € | 5,91 € | 0,64 € | 0,00 € | 0,00 € | 0,07 € | 0,05 € | 0,10 € | 0,86 € | 5,05 € | 86 % |
| Gaufre à la crème au safran | report | 7,50 € | 6,82 € | 0,35 € | 0,00 € | 1,02 € | 0,07 € | 0,11 € | 0,11 € | 1,66 € | 5,15 € | 76 % |
| Formule « Dégustation » : latte au safran + croissant au safran | ouverture | 9,50 € | 8,69 € | 1,34 € | 0,10 € | 0,88 € | 0,15 € | 0,16 € | 0,14 € | 2,77 € | 5,92 € | 68 % |
| Safran en filaments 0,5 g (lot et analyse affichés) | ouverture | 12,00 € | 11,37 € | 1,20 € | 1,00 € | 0,00 € | 0,05 € | 0,02 € | 0,18 € | 2,45 € | 8,92 € | 78 % |
| Safran en filaments 1 g | ouverture | 22,00 € | 20,85 € | 1,40 € | 2,00 € | 0,00 € | 0,05 € | 0,03 € | 0,33 € | 3,81 € | 17,04 € | 82 % |
| Safran en filaments 2 g | ouverture | 40,00 € | 37,91 € | 1,60 € | 4,00 € | 0,00 € | 0,05 € | 0,06 € | 0,60 € | 6,31 € | 31,61 € | 83 % |
| Crème au safran, pot 100 g | ouverture | 10,50 € | 9,95 € | 0,65 € | 0,00 € | 2,92 € | 0,05 € | 0,11 € | 0,16 € | 3,89 € | 6,07 € | 61 % |
| Crème au safran, pot 200 g | ouverture | 18,00 € | 17,06 € | 0,90 € | 0,00 € | 5,85 € | 0,05 € | 0,20 € | 0,27 € | 7,27 € | 9,79 € | 57 % |
| Coffret cadeau : pot 100 g + safran 0,5 g | ouverture | 24,00 € | 22,75 € | 3,35 € | 1,00 € | 2,92 € | 0,05 € | 0,15 € | 0,36 € | 7,83 € | 14,92 € | 66 % |

Coût de la crème au safran selon le mode de production (€/kg, hors pot) :

- interne : 21,42 €/kg (E : 1,5 h pour 10 kg + mise en pot ; mélangeur-broyeur et petit matériel 5 000–15 000 € ; local et plan de maîtrise sanitaire requis)
- faconnier : 29,23 €/kg (E : 8–18 €/kg de façon selon volume ; minimum de commande 50–500 kg ; aucun devis obtenu)
- hybride : 29,53 €/kg (E : pots chez un façonnier ; version « fourrage » assemblée en boutique (petit matériel))
