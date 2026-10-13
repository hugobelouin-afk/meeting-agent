# Panel consommateurs (simulé) — synthèse

Date : 13/10/2026. Outil : `panel.py` du skill founder-consumer, **20 acheteurs simulés** (mode --quick), graine 2026. Profil client validé par le porteur : `founder/customer.json`. Pitch testé (version 1, toute la carte présentée) : `founder/pitch.md`. Résultats bruts : `founder/panel/results.md` et `founder/panel/answers/`.

> **Limites, dites une fois.** Ce sont des agents simulés, pas des clients. Ils servent à faire apparaître des objections, des segments et des formulations. Ils ne mesurent ni une demande réelle, ni un taux de conversion. Les modèles de langage penchent vers l'acquiescement : **30 % est un plafond, pas une prévision**. Aucune réponse ci-dessous ne peut être utilisée comme témoignage client. Défaut de l'outil à signaler : les « habitudes » sont tirées au hasard, si bien que deux touristes se voient attribuer un trajet domicile-travail. Les agents l'ont signalé et ont tranché eux-mêmes.

## 1. Le résultat

**6 achètent · 14 passent (30 %).** Les 6 acheteurs déclarent tous **un seul achat le premier mois** : **aucun ne se décrit comme un client régulier.**

## 2. Qui achète, qui n'achète pas

| Segment | Acheteurs | Taux | Lecture |
| --- | ---: | ---: | --- |
| Parisien aisé d'un autre arrondissement | 5 | 60 % (mince) | Viennent une fois, par curiosité ou pour un cadeau. |
| Touriste | 8 | 25 % | Achètent une fois s'ils passent devant ; le pot ne les intéresse pas, le sachet de safran éventuellement. |
| **Habitué du quartier** | 7 | **14 % (mince)** | **Le segment censé payer le loyer au quotidien est celui qui achète le moins.** |

| Comportement | Taux | Lecture |
| --- | ---: | --- |
| Gourmand curieux qui partage | 3/3 | Attiré par la boisson qui change de couleur, mais pour **une visite filmée**. |
| Cadeaux et épicerie fine | 2/3 | Achètent du **safran ou un pot à offrir**, à condition que l'origine soit prouvée. |
| Promeneur | 1/3 | Dépend de la vitrine et du prix affiché. |
| **Café quotidien** | **0/4** | Le latte à 6,50 € coûte deux fois leur café crème habituel. |
| Attentif au sucre | 0/3 | La carte paraît entièrement sucrée. |
| Cuisinier exigeant | 0/2 | Pas d'origine, pas de catégorie ISO, pas de récolte affichées : pas d'achat. |
| Fidèle à ses adresses | 0/2 | Ne change pas d'habitude. |

Tous les groupes comptent moins de 8 acheteurs : ce sont des **signaux** à vérifier, pas des taux.

## 3. Pourquoi ils passent (dans leurs mots, traduits quand nécessaire)

1. **Trop sucré** (raison principale de 3 refus ; le sucre apparaît dans 12 réponses sur 20, comptage par mots-clés) : « Tout ce que je vois là est sucré : sucre infusé, crème au chocolat blanc, Nutella, glace. » (P001)
2. **Prix d'un café du quotidien** (3) : « Mon café crème à emporter, je le paie un peu plus de 3 euros au même comptoir depuis des années ; 6,50 € pour un latte parfumé, c'est le double. » (P002)
3. **Habitude** (3) : « J'ai mon café du matin, et le safran de mes risottos du week-end, je l'achète déjà chez mon épicier. » (P004)
4. **Confiance dans le safran** (raison principale de 2 refus ; origine, catégorie ou récolte évoquées dans 10 réponses sur 20) : « Je n'achète pas de safran sans savoir d'où il vient, et rien ici ne me le dit. » (P003) ; « Je l'achète à La Grande Épicerie, où je sais ce que je prends. » (P019)
5. **Gadget pour la photo ou les touristes** (évoqué dans 15 réponses sur 20) : « J'ai l'impression de payer le décor et le mot "safran" plutôt que le goût. » (P016)

Objections transversales qui comptent pour l'offre (comptages par mots-clés sur les 20 réponses, indicatifs) :
- **« Safran = paella / risotto »**, pas une boisson : barrière de familiarité, évoquée dans 6 réponses.
- **Peur d'un goût médicinal ou noyé dans le lait** : évoquée dans 5 réponses.
- **Le pot de 200 g, « je ne le finirai jamais »** : cité par 3 (P003, P013, P020). **Format probablement trop grand pour un premier achat.**
- **Olympus Croci est inconnu** : la marque mère ne rassure pas à elle seule (P006, P013, P014, P019).
- **Nutella et crêpes** font perdre du crédit à la maison de safran (P013, P014, P019).

## 4. Ce qui ferait basculer un non (réponses les plus fréquentes)

1. **Une dégustation gratuite en passant** (citée par 7).
2. **Un latte au safran sans sucre ajouté**, composition affichée (cité par 6).
3. **L'origine, la catégorie ISO 3632 et l'année de récolte affichées**, avec la possibilité de sentir le safran (citées par 5).
4. Un petit format de dégustation vers 3,50–4 € (P020).
5. Un avis d'un compte food parisien suivi (P007, P015).

## 5. Ce que le panel apprend (et ce qu'il n'apprend pas)

- **Enthousiasme initial : présent mais étroit.** Il vient des gourmands qui partagent et des acheteurs de cadeaux, pour une visite.
- **Fidélisation : non démontrée.** 0 acheteur régulier, 0 sur 4 chez les buveurs de café quotidien, 1 sur 7 chez les habitués. C'est le risque R1 du board, confirmé par le panel simulé.
- **Le safran à emporter est le produit qui convainc le mieux** (cadeau, safran 0,5–1 g), à condition que la preuve d'origine soit visible.
- **Prix du latte au safran (Van Westendorp, 20 réponses)** : plage acceptable **3,52 € à 7,00 €**, point d'indifférence 5,01 €, médianes « bonne affaire » 4,50 € et « cher » 6,50 €. Le prix testé (6,50 €) est dans la plage, mais en haut. Voir `founder/pricing-curve.md`.

## 6. Faut-il passer à 100 acheteurs ?

**Non, pas maintenant.** Les objections sont déjà concordantes (sucre, preuve d'origine, prix du quotidien, réachat nul), et un panel de 100 réponses simulées ne mesurerait pas mieux le réachat réel, qui est la vraie inconnue. Il ne ferait que préciser des taux de segment qui restent, par construction, des plafonds. La prochaine information utile est **réelle** : comptage de passage, dégustation payante, prévente (voir /founder-launch). Un nouveau panel de 20 acheteurs, avec la même graine, testera l'offre révisée dans /founder-offer.

## 7. À changer avant de dépenser

- Offre : retirer le sucre par défaut (latte au safran non sucré, sucre en option), afficher la preuve d'origine, proposer un petit format de dégustation et un petit pot. → /founder-offer
- Prix : tester le latte au safran entre 5,50 € et 6,50 € plutôt qu'au-delà. → /founder-pricing
- Marketing : répondre à « safran = paella » et à « gadget » par la dégustation et la preuve, pas par la couleur. → /founder-marketing
