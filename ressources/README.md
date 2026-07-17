# Ressources M2-B1 — Audit + industrialisation pipe scoring crédit

> Brief associé : **M2-B1**.
> Mode : individuel, présentiel mercredi, 5 heures synchrone.
> Le brief lui-même est diffusé sur **Simplonline** (énoncé + liens utiles).

Ce dossier `ressources/` est livré dans le **repo template GitHub**
[`Formation-SIMPLON-IA/ia-dev-id-parcours-m2-b1`](https://github.com/Formation-SIMPLON-IA/ia-dev-id-parcours-m2-b1).
Si tu lis ce fichier, c'est que tu as déjà cliqué sur **« Use this template »**
et cloné ton repo perso `M2-B1-pipe-eckmuhl-<prénom>`. Pour l'installation
et le démarrage, cf. le [`README.md`](../README.md) à la racine.

---

## 📚 Ordre de mobilisation au fil de la journée

| Tâche du brief | Durée | Mini-cours associé |
|---|---|---|
| 1. Découverte dataset | 30 min | (lecture du `german_credit_raw.csv` directement) |
| 2. Audit qualité | 1 h | [`01_Audit_qualite_pandas_essentiel.md`](./01_Audit_qualite_pandas_essentiel.md) |
| 3. Audit éthique | 1 h | [`02_Disparate_impact_essentiel.md`](./02_Disparate_impact_essentiel.md) |
| 4. Choix prétraitement | 30 min | [`03_ColumnTransformer_Pipeline_essentiel.md`](./03_ColumnTransformer_Pipeline_essentiel.md) (partie *Concepts clés*) |
| 5. Industrialisation Pipeline | 1 h 15 | [`03_ColumnTransformer_Pipeline_essentiel.md`](./03_ColumnTransformer_Pipeline_essentiel.md) (intégral) |
| 6. Parquet + datasheet | 45 min | [`04_Parquet_pyarrow_essentiel.md`](./04_Parquet_pyarrow_essentiel.md) + [`05_Datasheet_Gebru_essentiel.md`](./05_Datasheet_Gebru_essentiel.md) |
| 7. Synthèse `audit.md` | 30 min | — |

> 💡 **Tu n'es pas obligé·e de lire les mini-cours en amont.** Chacun est conçu
> pour être consulté **au moment où tu en as besoin**, pendant la tâche
> correspondante. Lecture + exercice guidé en ~15-20 min chacun.

---

## 🎯 Ce qu'on cherche à atteindre

À la fin de M2-B1, tu dois avoir :

- Un **notebook d'audit** propre, top-to-bottom, sections claires
  (qualité / éthique / prétraitement)
- Un **Pipeline scikit-learn persisté** (`src/pipeline.joblib`) rechargeable
- Un **dataset propre Parquet** (`data/german_credit_clean.parquet`) relit
  sans erreur via `pd.read_parquet`
- Une **datasheet Gebru** complète (7 sections, 1 page) — schéma documenté
  dedans
- Un **`audit.md`** lisible par le DPO (2 pages max, vocabulaire métier)
- Un repo GitHub `M2-B1-pipe-eckmuhl-<prénom>` avec ≥ 3 commits propres

→ Compétences visées : **C2 — imiter** + **C3 — imiter puis adapter**.

---

## 🔗 Liens externes

Toutes les URLs externes utilisées dans les mini-cours sont consolidées dans
[`liens_officiels.md`](./liens_officiels.md), vérifiées avant chaque envoi
de brief par l'outillage formateur.

---

## 🆘 Bloqué·e ?

1. **Relis le mini-cours** correspondant à ta tâche actuelle.
2. **Vérifie ton dataset** : le `german_credit_raw.csv` doit avoir 1 000
   lignes et 21 colonnes. Si tu as moins, refait le téléchargement.
3. **Sur `ColumnTransformer`** : commence par un exemple minimal (1 num +
   1 cat) avant d'attaquer Eckmühl.
4. **Demande en direct mercredi** — tu es en distanciel Discord, autant en
   profiter. N'attends pas d'être bloqué·e 30 min sur le même point.

**Garde-fou** : pas besoin de coder hors mercredi 9h-17h. Le brief est
calibré pour tenir dans les 5h sync. Si tu finis avant, viens en MP.