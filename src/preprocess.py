"""M2-B1 — Pipeline de préparation pour le scoring crédit Eckmühl."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


NUMERIC_FEATURES: list[str] = [
    "duration_months",
    "credit_amount",
    "installment_rate_pct_income",
    "residence_since_years",
    "age",
    "n_existing_credits",
    "n_people_liable",
]

BASE_ORDINAL_FEATURES: dict[str, list[str]] = {
    "employment_since": [
        "unemployed",
        "< 1 year",
        "1-4 years",
        "4-7 years",
        ">= 7 years",
    ],
}

ORDINAL_FEATURES: dict[str, list[str]] = {
    **BASE_ORDINAL_FEATURES,
    "customer_segment": [
        "basic",
        "plus",
        "premium",
        "private",
    ],
}

CATEGORICAL_FEATURES: list[str] = [
    "checking_account_status",
    "credit_history",
    "purpose",
    "savings_account",
    "personal_status_sex",
    "other_debtors",
    "property",
    "other_installment_plans",
    "housing",
    "job",
    "telephone",
    "foreign_worker",
]

TARGET_COLUMN: str = "credit_risk"

TARGET_MAPPING: dict[str, int] = {
    "good_credit": 0,
    "bad_credit": 1,
}


def load_dataset(path: Path) -> tuple[pd.DataFrame, pd.Series]:
    """Load and enrich the German Credit dataset.

    The supplementary file is joined by row position because it contains
    exactly one customer_segment value for each row of the raw dataset.

    Args:
        path: Path to german_credit_raw.csv.

    Returns:
        A tuple containing the selected features and mapped target.

    Raises:
        FileNotFoundError: If an expected input file does not exist.
        ValueError: If the target or supplementary dataset is invalid.
        KeyError: If an expected feature is missing.
    """
    supplement_path = path.with_name("german_credit_supplement.csv")

    if not path.exists():
        raise FileNotFoundError(f"Dataset brut introuvable : {path}")

    if not supplement_path.exists():
        raise FileNotFoundError(
            f"Complément de données introuvable : {supplement_path}"
        )

    raw_df = pd.read_csv(path)
    supplement_df = pd.read_csv(supplement_path)

    if supplement_df.columns.tolist() != ["customer_segment"]:
        raise ValueError(
            "Le complément doit contenir uniquement la colonne "
            "'customer_segment'."
        )

    if len(raw_df) != len(supplement_df):
        raise ValueError(
            "Le dataset brut et le complément doivent contenir "
            "le même nombre de lignes."
        )

    df = pd.concat(
        [
            raw_df.reset_index(drop=True),
            supplement_df.reset_index(drop=True),
        ],
        axis=1,
    )

    y = df[TARGET_COLUMN].map(TARGET_MAPPING)

    if y.isna().any():
        unknown_targets = (
            df.loc[y.isna(), TARGET_COLUMN]
            .drop_duplicates()
            .tolist()
        )

        raise ValueError(
            f"Cible non mappée : {unknown_targets}"
        )

    all_features = (
        NUMERIC_FEATURES
        + list(ORDINAL_FEATURES)
        + CATEGORICAL_FEATURES
    )

    duplicated_features = {
        feature
        for feature in all_features
        if all_features.count(feature) > 1
    }

    if duplicated_features:
        raise ValueError(
            "Features présentes dans plusieurs familles : "
            f"{sorted(duplicated_features)}"
        )

    missing_features = [
        feature
        for feature in all_features
        if feature not in df.columns
    ]

    if missing_features:
        raise KeyError(
            f"Colonnes attendues absentes du CSV : {missing_features}"
        )

    X = df[all_features].copy()

    return X, y.astype("int64")


def _build_preprocessor(
    include_customer_segment: bool,
) -> ColumnTransformer:
    """Build either the initial or adapted ColumnTransformer."""
    ordinal_features = (
        ORDINAL_FEATURES
        if include_customer_segment
        else BASE_ORDINAL_FEATURES
    )

    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
        ]
    )

    ordinal_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent"),
            ),
            (
                "ordinal",
                OrdinalEncoder(
                    categories=[
                        ordinal_features[column]
                        for column in ordinal_features
                    ],
                    handle_unknown="use_encoded_value",
                    unknown_value=-1,
                ),
            ),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent"),
            ),
            (
                "onehot",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False,
                ),
            ),
        ]
    )

    return ColumnTransformer(
        transformers=[
            (
                "num",
                numeric_pipeline,
                NUMERIC_FEATURES,
            ),
            (
                "ord",
                ordinal_pipeline,
                list(ordinal_features),
            ),
            (
                "cat",
                categorical_pipeline,
                CATEGORICAL_FEATURES,
            ),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )


def build_preprocessor() -> ColumnTransformer:
    """Build the final preprocessor including customer_segment."""
    return _build_preprocessor(
        include_customer_segment=True,
    )


def fit_and_save(
    data_path: Path,
    output_path: Path,
) -> None:
    """Fit and persist the final preprocessing pipeline.

    The pipeline is fitted on the complete dataset because this exercise
    produces a preprocessing artifact rather than a predictive model.
    """
    X, _y = load_dataset(data_path)

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                build_preprocessor(),
            ),
        ]
    )

    pipeline.fit(X)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        pipeline,
        output_path,
        compress=3,
    )


if __name__ == "__main__":
    fit_and_save(
        data_path=Path("data/german_credit_raw.csv"),
        output_path=Path("src/pipeline.joblib"),
    )