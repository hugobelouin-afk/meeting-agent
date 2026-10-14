# Panels simulés : offre de référence, offre complète S6 et combinaison S5

Trois panels de 20 acheteurs simulés, **mêmes profils** et même graine (2026) :
- v2 (`founder/panel/`) : offre de référence S0 ;
- S6 (`panel-S6/`) : S0 + les 11 macarons, les pâtisseries, le plat du midi et les 6 glaces ANGIOLO ;
- S5 (`panel-S5/`) : S0 + madeleines, 5 macarons et entremets sur commande.

Pitchs exacts : `pitch-S6.md` et `pitch-S5.md`. La seule autre différence est le produit des questions de prix : coffret de 6 macarons (S6), boîte de 6 madeleines (S5), latte au safran (v2).

> **Ces acheteurs sont simulés.** Ils servent à formuler des hypothèses et à trouver des objections. Ils ne prouvent ni la demande ni un taux d'achat, et leurs réponses varient d'un tirage à l'autre, même à profil identique. Aucun chiffre de ce document n'entre dans le modèle financier.

## 1. Taux bruts et lecture correcte

| | v2 (S0) | S6 (offre complète) | S5 (combinaison) |
| --- | ---: | ---: | ---: |
| Acheteurs | 10 / 20 (50 %) | 15 / 20 (75 %) | 14 / 20 (70 %) |
| Achats déclarés le premier mois | 12 (1,2 par acheteur) | 19 (1,3) | 17 (1,2) |
| **Acheteurs dont l'achat principal est un produit ajouté** | — | **4** (P007, P009, P010, P011), plus 2 « peut-être » | **4** (P008, P009, P011, P020), plus 5 « peut-être » une madeleine ou une boîte |
| Acheteurs gagnés par rapport à v2 **grâce à un produit ajouté** | — | **2** : P007 (coffret de macarons pour un dîner), P010 (risotto du midi et coffret) | **1** : P020 (espresso et une madeleine tiède) |
| Acheteurs gagnés par rapport à v2 **qui n'achètent que des produits de S0** (safran, latte sans sucre) | — | 3 : P001, P015, P017 | 3 : P001, P010, P015 |

**La hausse brute de 50 % à 70–75 % ne mesure pas l'effet des extensions.**
- Sur les 5 acheteurs de plus de S6, 3 achètent du safran ou un latte sans sucre. Ces produits étaient déjà dans l'offre v2, présentée de la même façon. Leur bascule vient de la variabilité du panel simulé, pas des macarons ni des glaces.
- Il en va de même pour 3 des 4 acheteurs de plus de S5.
- L'effet attribuable aux extensions se limite à **+2 acheteurs sur 20 pour S6** et **+1 sur 20 pour S5**. C'est dans l'ordre de grandeur du modèle, qui retient 3 à 15 visites ajoutées par jour sur 95 tickets.

Ce qui est plus robuste que le taux :
- **Le safran prouvé reste le premier motif d'achat dans les deux panels** : 10 acheteurs sur 15 dans S6 et 10 sur 14 dans S5 achètent d'abord du safran, un coffret ou un latte de S0. C'est le résultat du panel v2. Les extensions ne remplacent pas cette raison d'entrer ; au mieux, elles s'y ajoutent.
- **Les produits ajoutés touchent les profils déjà acheteurs** : gourmand curieux, acheteur de cadeaux, promeneur. Aucun ne convertit les « fidèles à leurs adresses ». Les buveurs de café quotidien passent de 0 sur 4 (v2) à 1 sur 4 dans chaque panel : P007 dans S6, par un coffret cadeau ; P020 dans S5, par une madeleine avec l'espresso.

## 2. Objections nouvelles (dans leurs mots)

| objection | S6 | S5 | conséquence pour l'offre |
| --- | --- | --- | --- |
| **« Tout safran », boutique qui veut tout faire** | P003 : « avec 11 parfums de macarons, des glaces et un plat du jour, j'ai peur d'une boutique sucrée pour touristes où le safran n'est qu'un décor » ; P004 : « une maison du safran qui vend 11 macarons, des glaces et un plat du midi ressemble à une boutique Instagram qui veut tout faire » ; P016 : concept « tout safran » qui « sent le piège à touristes » | P004 : « du safran partout (café, croissant, madeleine, macaron), c'est un gadget » ; P016 (même idée) | L'offre complète **affaiblit la crédibilité de la maison experte**, qui est la raison d'achat n° 1. Argument contre S6. |
| **Macarons : les grandes maisons sont à deux rues, au même prix** | 11 acheteurs sur 20 : P004, P005 (« le prix des grandes maisons sans le nom »), P008, P009, P010, P011, P012, P013, P016, P019, P020 | — | Un macaron classique n'a aucune raison d'être acheté ici. **Seul le macaron au safran se défend**, et il doit être meilleur ou différent. |
| **Trop sucré, le safran disparaît** | P001, P006, P008, P015, P017, P018 | P002, P003, P006, P008, P017, P018 | Recettes peu sucrées où le safran se sent ; teneur en sucre affichée (demandée par P017). |
| **Madeleines : bonnes tièdes, pas en cadeau** | — | P006, P012, P013, P020 : « tièdes, elles ne tiennent pas jusqu'au lendemain » ; P012 demande une boîte de voyage qui tienne une semaine ; P020 une boîte de 3 vers 6 € | La madeleine se vend **à l'unité, tiède**. Une boîte cadeau suppose un conditionnement et une durée de vie validés (inconnus). |
| **Le plat du midi est « à sa place »** | P010 : « le risotto milanais, là le safran est à sa place » | — | Un seul acheteur. Le plat est cohérent avec l'usage du safran que connaissent les clients (paella, risotto), mais un seul signal ne prouve rien. |
| **Glaces** | P004 : « les lattes, les macarons et les glaces, je les laisse aux touristes » ; personne ne cite la glace comme motif | — | Aucun signal favorable. Cohérent avec la proximité d'ANGIOLO. |

## 3. Prix (Van Westendorp, outil `founder-pricing/van_westendorp.py`)

| produit | fourchette acceptable | point d'indifférence | prix testé | lecture |
| --- | --- | ---: | ---: | --- |
| Coffret de 6 macarons (S6) | 9,04 € à 19,96 € | 13,04 € | 16,50 € | dans la fourchette, au-dessus du point d'indifférence ; 5 acheteurs sur 20 trouvent déjà 16,50 € « cher » |
| Boîte de 6 madeleines (S5) | 6,03 € à 14,98 € | 9,03 € | 12,00 € | dans la fourchette mais haut : 9 acheteurs sur 20 placent leur seuil « cher » à 12 € ou moins |

Ces prix guident le test, ils ne le remplacent pas. Ils conduisent à deux propositions :
- coffret de 6 macarons maintenu à 16,50 €, avec un test à 15 € ;
- boîte de madeleines ramenée à **10 € les 6**, ou remplacée par un sachet de 3 à 5,50 €.

Le modèle financier garde 12 € ; la sensibilité « prix −10 % » en montre l'effet.

## 4. Ce que les panels changent dans la recommandation

1. **Ne pas présenter l'offre complète.** Le panel ne fait pas apparaître de demande nouvelle importante. Il fait apparaître une objection nouvelle : la dispersion, qui touche la raison d'achat principale.
2. **Macarons : uniquement au safran**, au plus un classique tournant. Les classiques font face à Pierre Hermé et Ladurée, cités spontanément par 11 acheteurs sur 20.
3. **Madeleines : à l'unité et tièdes d'abord.** La boîte reste à tester avec un vrai conditionnement.
4. **Plat du midi : un seul signal positif.** Il reste une hypothèse à tester en réel, après ouverture.
5. **Glaces élargies : aucun signal.** Le panel n'y voit pas de raison de venir.
