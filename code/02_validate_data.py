#!/usr/bin/env python3

import csv
import math
from pathlib import Path


REPO_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_DIR / "data" / "raw"


def read_pedigree(path):
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return rows


def read_matrix(path):
    with path.open(encoding="utf-8") as handle:
        header = handle.readline().strip().split()
        labels = [item.strip('"') for item in header]
        row_labels = []
        values = []
        for line in handle:
            fields = line.strip().split()
            row_labels.append(fields[0].strip('"'))
            values.append([float(item) for item in fields[1:]])
    return labels, row_labels, values


def main():
    pedigree = read_pedigree(DATA_DIR / "Pedigree.txt")
    genotype_ids = [row["genotype"] for row in pedigree]
    genotype_set = set(genotype_ids)

    assert len(genotype_ids) == len(genotype_set), "Duplicate genotype identifiers"
    assert all(all(row[field] != "" for field in ("genotype", "female", "male")) for row in pedigree)

    parent_ids = {
        parent
        for row in pedigree
        for parent in (row["female"], row["male"])
        if parent != "0"
    }
    assert parent_ids <= genotype_set, "Parent identifiers absent from genotype column"
    assert all(row["genotype"] not in (row["female"], row["male"]) for row in pedigree)

    columns, rows, matrix = read_matrix(DATA_DIR / "Amatrix.txt")
    n = len(columns)
    assert n == 610, f"Expected 610 matrix columns, found {n}"
    assert len(rows) == n and all(len(row) == n for row in matrix), "Matrix is not square"
    assert rows == columns, "Row and column identifiers differ"
    assert len(set(rows)) == n, "Duplicate matrix identifiers"
    assert set(rows) <= genotype_set, "Matrix identifiers absent from pedigree"
    assert genotype_ids[:n] == rows, "Matrix targets do not match first pedigree records"

    max_asymmetry = 0.0
    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            assert math.isfinite(value), "Non-finite matrix value"
            max_asymmetry = max(max_asymmetry, abs(value - matrix[j][i]))
    assert max_asymmetry <= 1e-12, f"Matrix asymmetry exceeds tolerance: {max_asymmetry}"

    print(f"Pedigree records: {len(pedigree)}")
    print(f"Matrix dimensions: {n} x {n}")
    print(f"Maximum asymmetry: {max_asymmetry:.3g}")
    print("Validation completed successfully.")


if __name__ == "__main__":
    main()

