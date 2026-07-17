"""Contract test du pipeline de préparation Eckmühl — à compléter.

Ce script valide que le `src/pipeline.joblib` que tu as produit respecte le
contrat attendu pour la suite (entraînement, déploiement). Plus exigeant
qu'un simple `print OK` : on vérifie le rechargement, la préservation des
lignes, l'absence de NaN après imputation, l'expansion des colonnes par
l'encodage, et la stabilité (déterminisme) de la transformation.

À lancer depuis la racine du repo, **après** avoir produit `src/pipeline.joblib`
(tâches 5 et 5 bis) :

    python contract_test.py

Mini-cours d'appui : `ressources/03_ColumnTransformer_Pipeline_essentiel.md`
"""
from __future__ import annotations

import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent / "src"))
from preprocess import load_dataset  # noqa: E402

MODEL_PATH = Path(__file__).parent / "src" / "pipeline.joblib"
DATA_PATH = Path(__file__).parent / "data" / "german_credit_raw.csv"


def _to_dense(matrix) -> np.ndarray:
    """Convertit une sortie éventuellement creuse (OneHotEncoder) en array dense."""
    return matrix.toarray() if hasattr(matrix, "toarray") else np.asarray(matrix)


def contract_test_pipeline(
    model_path: Path,
    x_sample: pd.DataFrame,
    expected_n_features: int | None = None,
) -> None:
    """Valide le contrat du pipeline de préparation rechargé.

    Args:
        model_path: chemin vers le `pipeline.joblib` à valider.
        x_sample: DataFrame d'au moins 5 lignes, aligné sur les features
            attendues par le pipeline (mêmes colonnes qu'à l'entraînement).
        expected_n_features: nombre de colonnes attendu en sortie, relevé
            depuis ton notebook (`pipeline.transform(X).shape[1]`). Sert à
            détecter une dérive d'encodage.
    """
    n_in = len(x_sample)
    pipeline = joblib.load(model_path)

    out = _to_dense(pipeline.transform(x_sample))

    assert out.ndim == 2, f"sortie non 2D : ndim={out.ndim}"
    assert out.shape[0] == n_in, (
        f"lignes non préservées : entrée {n_in}, sortie {out.shape[0]}"
    )
    assert out.shape[1] >= x_sample.shape[1], (
        f"sortie ({out.shape[1]} col) plus étroite que l'entrée "
        f"({x_sample.shape[1]} col) — l'encodage a-t-il bien été appliqué ?"
    )
    assert not np.isnan(out.astype(float)).any(), (
        "des NaN subsistent après transformation — l'imputation est incomplète"
    )

    # Déterminisme : transformer deux fois doit donner exactement le même résultat.
    out_bis = _to_dense(pipeline.transform(x_sample))
    assert np.allclose(out, out_bis), "transformation non déterministe"

    if expected_n_features is not None:
        assert out.shape[1] == expected_n_features, (
            f"dérive d'encodage — observé {out.shape[1]} colonnes, "
            f"attendu {expected_n_features} (relevé notebook)"
        )

    print(
        f"Contract test OK — {n_in} lignes préservées, {out.shape[1]} colonnes "
        f"en sortie, aucun NaN, transformation déterministe."
    )


if __name__ == "__main__":
    # 1. Relève le nombre de colonnes de sortie depuis ton notebook :
    #
    #    from src.preprocess import load_dataset
    #    import joblib
    #    pipe = joblib.load("src/pipeline.joblib")
    #    X, _ = load_dataset("data/german_credit_raw.csv")
    #    print(pipe.transform(X).shape[1])
    #
    # 2. Reporte ce nombre dans `expected_n_features` ci-dessous, puis lance
    #    `python contract_test.py` depuis la racine du repo.
    #
    # ⚠️ Ce nombre évolue à la tâche 5 bis (ajout de `customer_segment`) :
    #    +1 colonne si tu l'encodes en ordinal, +k colonnes si tu l'encodes
    #    en one-hot. C'est exactement ce que ce test fige.

    expected_n_features: int | None = None  # ← reporte ici la valeur de ton notebook

    if expected_n_features is None:
        raise NotImplementedError(
            "Renseigne `expected_n_features` à partir du snippet ci-dessus, "
            "puis relance ce script."
        )

    X, _y = load_dataset(DATA_PATH)
    contract_test_pipeline(MODEL_PATH, X.head(5), expected_n_features=expected_n_features)