# Étude complémentaire — extensions de La Saffranerie (14/10/2026)

Cette étude teste les extensions proposées par l'associé : macarons, madeleines et entremets, plats du midi, glaces élargies.
- Elle compare sept scénarios, de S0 à S6, plus des variantes : S1c, S2a, S2b, S4p, S5T.
- **Elle ne modifie aucun fichier de l'étude initiale** (`founder/`). La référence S0 est le modèle v2, importé tel quel.

**Commencer par `plan-extensions.md`** : la recommandation, puis les 8 livrables demandés.

| fichier | contenu |
| --- | --- |
| `plan-extensions.md` | décision : recommandation, avant/après, comparatif S0–S6, verdict par extension, gamme de macarons, sélection, équipements, fournisseurs, test, données manquantes |
| `reference-S0.md` | le scénario de référence extrait des analyses existantes (carte, prix, panier, fréquentation, marges, charges, investissement, personnel, verdict), avec ses limites |
| `recherches-extensions.md` | journal des recherches : faits vérifiés (liens, dates), données communiquées, estimations, **recherches sans résultat** |
| `competitors-extensions.md`, `competitors-extensions.csv` | références de marché (macarons, madeleines, déjeuner, glace) et fournisseurs |
| `consumer-extensions.md`, `pitch-S5.md`, `pitch-S6.md`, `panel-S5/`, `panel-S6/` | deux panels simulés de 20 acheteurs (mêmes profils et même graine que le panel v2) et leur lecture critique |
| `offer-extensions.md`, `pricing-extensions.md` | offre, gamme, prix, coffrets, formules ; sensibilité au prix |
| `ops-extensions.md` | modes de fabrication, personnel, meubles et équipements, surfaces, capacité, hygiène, devis à obtenir |
| `cfo-extensions.md` | hypothèses modifiées (avant/après), TVA, comparatif, effets décomposés, seuils, financement, sensibilités, travail des fondateurs, verdict de l'outil |
| `launch-extensions.md` | test réel : ordre, budget, seuils et règles de décision |
| `hypotheses_ext.json` | hypothèses propres aux extensions (étiquettes C, V, E, H) |
| `modele_ext.py`, `sorties/ext-modele.md`, `sorties/resultats-ext.json` | modèle des extensions et ses résultats complets |
| `verdicts.py`, `verdicts/` | verdict calculé par l'outil `founder-plan` pour S0, S5, S5T et S6 |

Recalculer après une nouvelle donnée (devis, minimum de commande, prix d'ANGIOLO, résultat du test) :
1. modifier `hypotheses_ext.json` ;
2. lancer `python3 founder/extensions/modele_ext.py && python3 founder/extensions/verdicts.py` ;
3. reprendre à la main les chiffres des notes (`cfo-extensions.md`, `plan-extensions.md`).

Toutes les demandes ajoutées sont des hypothèses. Le panel est simulé. Aucun devis n'a été obtenu, aucun fournisseur contacté, aucune dépense engagée.
