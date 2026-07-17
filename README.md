# M2-B1 — Banque Eckmühl : audit et pipeline

Audit qualité et éthique du dataset German Credit, accompagné d'un pipeline de préparation réutilisable, persisté et vérifié par un test de conformité.

## Livrables

* [`notebooks/M2-B1_fernando_audit.ipynb`](notebooks/M2-B1_fernando_audit.ipynb) : audit qualité, audit éthique et justification des prétraitements ;
* [`src/preprocess.py`](src/preprocess.py) : chargement, enrichissement et préparation des données ;
* `src/pipeline.joblib` : pipeline final entraîné et persisté ;
* [`contract_test.py`](contract_test.py) : vérification du contrat de transformation ;
* [`audit.md`](audit.md) : synthèse destinée au DPO.

## Reproduction

Depuis la racine du projet :

```bash
python -m pip install -r requirements.txt
jupyter nbconvert --execute --to notebook --inplace notebooks/M2-B1_fernando_audit.ipynb
python src/preprocess.py && python contract_test.py
```

Le test final doit afficher :

```text
Contract test OK — 5 lignes préservées, 58 colonnes en sortie, aucun NaN, transformation déterministe.
```

## Données

Le fichier `data/german_credit_raw.csv` contient :

* **1 000 dossiers** ;
* **20 variables explicatives** ;
* la cible `credit_risk`, composée de `good_credit` et `bad_credit`.

Le fichier `data/german_credit_supplement.csv` ajoute `customer_segment`. Il contient une ligne pour chaque dossier et est joint au dataset principal selon la position des lignes.

## Prétraitements

* Variables numériques : imputation par la médiane puis standardisation.
* Variables nominales : imputation par la modalité la plus fréquente puis encodage en indicateurs.
* Variables ordinales : imputation par la modalité la plus fréquente puis encodage selon un ordre explicite.
* `customer_segment` : ordre `basic < plus < premium < private`.

Le pipeline final accepte **21 variables d'entrée** et produit **58 variables préparées**.

## Résultats principaux

* Aucun `NaN` après transformation.
* Nombre de lignes préservé.
* Transformation déterministe.
* Disparate impact de `foreign_worker` : **0,7766**, sous le seuil d'alerte de **0,8**.
* Disparate impact selon le sexe dérivé : **0,8966**, sans alerte forte selon la règle des quatre cinquièmes.
