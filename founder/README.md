# Dossier Founder — La Saffranerie (étude du 13/10/2026)

Commencer par **`summary.md`** (une demi-page), puis **`one-pager.md`**, puis **`business-plan.md`** (tout le dossier compilé, verdict calculé en tête).

| Étape | Fichier | Contenu |
| --- | --- | --- |
| Idée | `idea.md` | le projet tel que présenté |
| 1. Board | `board.md`, `board/` | vote, risques, conditions (C1–C11), mémos des trois lentilles |
| 2. Concurrents | `competitors.md`, `competitors.csv` | 16 concurrents et références, prix, carte de positionnement, manque à combler |
| 3. Panel | `customer.json`, `pitch-v1.md`, `consumer.md`, `panel-v1/` | 20 acheteurs simulés sur le pitch initial |
| 4. Prix | `pricing.md`, `pricing-curve.md` | grille TTC, marges, prix nécessaire, tests de prix |
| 5. Offre | `offer.md`, `pitch.md`, `panel/` | offre révisée, signature, re-test du panel (même graine) |
| 6. CFO | `cfo.md`, `cfo-sources.md`, `cfo-outil.md`, `numbers.json` | note du CFO v2, TVA, financement, budgets, scénarios, sensibilités |
| 7. Marketing | `marketing.md` | positionnement, canaux, B / 3B / 10B, campagne de 30 jours, accroches |
| 8. Marque | `brand.md` | nom, vérifications, voix, identité visuelle |
| 9. Exploitation | `ops.md` | crème, signature, fournisseurs, planning, routines, obligations, risques |
| 10. Lancement | `launch.md` | questions pour la visite, test réel et seuils, compte à rebours, 30 premiers jours |
| 11. Plan | `summary.md`, `business-plan.md`, `one-pager.md` | verdict et recommandation |
| Modèle | `modele/` | `saffranerie.py` (modèle), `hypotheses.json` (v2), `hypotheses-v1.json`, `sorties/` |
| Recherches | `recherches/notes.md` | faits vérifiés, sources et dates, données communiquées |

Recalculer après une nouvelle donnée (devis, bail, comptage, prix de cession) : modifier `modele/hypotheses.json`, puis
`python3 founder/modele/saffranerie.py && python3 founder/modele/traduire_outil.py && python3 founder/modele/traduire_plan.py`.
La note de `cfo.md` (sections 1 à 11) est rédigée à la main : la reprendre si les chiffres changent.

## Étude complémentaire du 14/10/2026 : extensions (macarons, pâtisseries, traiteur, glaces)

Dossier séparé **`extensions/`**, qui ne modifie aucun fichier ci-dessus. Commencer par **`extensions/plan-extensions.md`** : recommandation, comparatif S0–S6, verdict par extension, test réel, données manquantes. Index : `extensions/README.md`.
