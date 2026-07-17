"""Génère le complément de données Eckmühl (variation C3 « adapter »).

Eckmühl renvoie, en cours de mission, une **nouvelle variable** :
`customer_segment` — le segment commercial du client. C'est une variable
**catégorielle ordonnée** (`basic < plus < premium < private`) avec ~5 % de
valeurs manquantes (clients non segmentés).

Le fichier produit a **le même nombre de lignes, dans le même ordre** que
`german_credit_raw.csv` → il se joint par position
(`pd.concat([df, supp], axis=1)`).

Déterministe (seed 42). Usage : ``python scripts/generate_supplement.py``.
"""
from __future__ import annotations

import csv
import random
from pathlib import Path

SEED = 42
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW = DATA_DIR / "german_credit_raw.csv"
OUT = DATA_DIR / "german_credit_supplement.csv"

# Tiers ORDONNÉS (du plus bas au plus haut). L'ordre porte du sens métier.
SEGMENTS = ["basic", "plus", "premium", "private"]
WEIGHTS = [42, 33, 17, 8]
MISSING_RATE = 0.05  # ~5 % de clients non segmentés (valeur vide)


def n_rows() -> int:
    """Nombre de lignes du dataset brut (pour aligner le complément)."""
    with RAW.open(encoding="utf-8") as f:
        return sum(1 for _ in f) - 1  # -1 pour l'en-tête


def main() -> None:
    rng = random.Random(SEED)
    n = n_rows()
    rows: list[str] = []
    for _ in range(n):
        if rng.random() < MISSING_RATE:
            rows.append("")  # manquant explicite (client non segmenté)
        else:
            rows.append(rng.choices(SEGMENTS, weights=WEIGHTS)[0])

    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["customer_segment"])
        writer.writerows([[v] for v in rows])

    n_missing = rows.count("")
    print(f"→ {OUT.name} : {n} lignes ({n_missing} manquants ~{n_missing/n:.0%})")


if __name__ == "__main__":
    main()