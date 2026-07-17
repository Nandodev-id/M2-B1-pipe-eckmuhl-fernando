# M2-B1 — Squelette repo (Banque Eckmühl — audit + pipeline)

> **Repo template GitHub.** Clique sur **« Use this template »** en haut à
> droite de cette page → **Create a new repository** → nomme-le
> `M2-B1-pipe-eckmuhl-<prénom>` sur **ton** compte GitHub personnel.
> C'est ce nouveau repo que tu cloneras pour travailler.

---

## 🚀 Démarrage (4 commandes)

```bash
# 0. Clone ton repo perso fraîchement créé
git clone git@github.com:<ton-user>/M2-B1-pipe-eckmuhl-<prenom>.git
cd M2-B1-pipe-eckmuhl-<prenom>

# 1. Environnement virtuel
python -m venv .venv && source .venv/bin/activate     # Linux/macOS
# .venv\Scripts\activate                              # Windows

# 2. Dépendances
pip install -r requirements.txt

# 3. Vérification
jupyter notebook notebooks/M2-B1_template.ipynb       # → s'ouvre dans le navigateur
```

Si ces 4 commandes marchent, ton poste est prêt.

> 📦 Le dataset `german_credit_raw.csv` est **déjà dans `data/`** (livré avec
> le template). Le `.gitignore` versionne ce CSV brut d'entrée mais exclut
> les sorties que tu produis (`*.parquet`, pipeline `.joblib`) — ne te casse
> pas la tête.

---

## 📁 Structure du repo

```
M2-B1-pipe-eckmuhl-<prenom>/
├── data/
│   ├── german_credit_raw.csv          # fourni avec le template (versionné)
│   ├── german_credit_supplement.csv   # fourni — complément customer_segment (tâche 5 bis)
│   └── german_credit_clean.parquet    # produit en bonus (gitignored)
├── scripts/
│   └── generate_supplement.py         # (repro) régénère le complément, seed 42
├── notebooks/
│   └── M2-B1_template.ipynb           # à dupliquer en M2-B1_<prenom>_audit.ipynb
├── src/
│   ├── preprocess.py                  # squelette Pipeline avec TODO
│   └── pipeline.joblib                # produit en tâche 5 (gitignored)
├── ressources/                        # 📚 mini-cours d'appui (lecture juste-à-temps)
│   ├── README.md                      # ordre de mobilisation + objectifs
│   ├── 01_Audit_qualite_pandas_essentiel.md
│   ├── 02_Disparate_impact_essentiel.md
│   ├── 03_ColumnTransformer_Pipeline_essentiel.md
│   ├── 04_Parquet_pyarrow_essentiel.md
│   ├── 05_Datasheet_Gebru_essentiel.md
│   └── liens_officiels.md
├── audit.md                           # template à remplir (max 2 pages)
├── datasheet.md                       # template Gebru à remplir (1 page)
├── requirements.txt
├── .gitignore
└── README.md (ce fichier — à compléter)
```

---

## 📚 Mini-cours d'appui

Les **5 mini-cours pédagogiques** du brief sont fournis dans
[`./ressources/`](./ressources/). Lecture juste-à-temps, ~15-20 min chacun :

| Tâche | Mini-cours |
|---|---|
| Audit qualité d'un dataset tabulaire | [`01_Audit_qualite_pandas_essentiel.md`](./ressources/01_Audit_qualite_pandas_essentiel.md) |
| Disparate impact (règle des 4/5) | [`02_Disparate_impact_essentiel.md`](./ressources/02_Disparate_impact_essentiel.md) |
| Industrialisation Pipeline + ColumnTransformer | [`03_ColumnTransformer_Pipeline_essentiel.md`](./ressources/03_ColumnTransformer_Pipeline_essentiel.md) |
| Persistance Parquet (pyarrow) | [`04_Parquet_pyarrow_essentiel.md`](./ressources/04_Parquet_pyarrow_essentiel.md) |
| Datasheet Gebru (7 sections) | [`05_Datasheet_Gebru_essentiel.md`](./ressources/05_Datasheet_Gebru_essentiel.md) |

Cf. [`./ressources/README.md`](./ressources/README.md) pour l'ordre de mobilisation détaillé.

---

## 🧭 Démarche attendue

### 🎯 Socle — à terminer par tout le monde (valide C2 + C3)

1. **Découverte** (30 min) — charge le CSV, repère cible + variables sensibles
2. **Audit qualité** (1 h) — manquants, outliers, 4 visualisations
3. **Audit éthique** (1 h) — disparate impact sur 2+ variables sensibles
4. **Choix prétraitement** (30 min) — remplis les listes dans `preprocess.py`
5. **Industrialisation** (1 h 15) — `Pipeline` + `ColumnTransformer`, persisté
5 bis. **Adapter** (20 min) — un complément `customer_segment` arrive :
   intègre-le au pipeline et justifie ton choix d'encodage (geste C3 N2)
6. **Synthèse** (30 min) — complète `audit.md` (verdict DPO + recommandations)

> 🔎 **Auto-vérification** : une fois `src/pipeline.joblib` produit (tâches 5 et
> 5 bis), lance `python contract_test.py` pour valider ton pipeline (lignes
> préservées, aucun NaN après imputation, déterminisme, nombre de colonnes
> figé). Renseigne d'abord `expected_n_features` comme indiqué dans le fichier.

### ⭐ Extensions — seulement si le socle est propre

7. **Parquet + réflexe stockage** (~10 min) — sauve en `.parquet`, justifie
   le choix (vs CSV, vs PostgreSQL)
8. **Datasheet Gebru** (~30 min) — premier jet de `datasheet.md` (la version
   complète, c'est jeudi en M2-B2)
9. **Fairlearn** — recalcule tes DI avec `MetricFrame`

> ⚠️ N'entame pas les extensions avant d'avoir un socle solide. Mieux vaut un
> socle nickel qu'un bonus bâclé.

→ Compétences visées : **C2 — imiter** + **C3 — imiter puis adapter**.

---

## ✅ Conventions de code

- Python 3.11+
- Type hints sur toutes les signatures publiques
- Pas de `print` (utiliser `display()` ou `logging`)
- `random_state=42` partout où il y a de l'aléa
- `pathlib.Path` pour les chemins (pas de `os.path`)

---

## 🆘 Bloqué·e ?

1. Relis le mini-cours correspondant à ta tâche actuelle (cf.
   [`./ressources/README.md`](./ressources/README.md)).
2. Vérifie que `german_credit_raw.csv` est bien dans `data/` (livré avec le
   template — il doit y être dès le clone).
3. Si tu butes sur **`ColumnTransformer`** : prends 10 min pour faire un
   exemple ultra-minimal en console (1 numérique + 1 catégorielle), puis
   remonte vers ton vrai dataset.
4. Demande en direct mercredi sur Discord — `fil-M2-B1`. N'attends pas
   30 min sur le même point.