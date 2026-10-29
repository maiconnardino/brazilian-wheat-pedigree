# Brazilian wheat pedigree data

This repository contains pedigree records and a numerator additive relationship matrix associated with the article:

> *A century of wheat breeding in Brazil: origin and pedigree-based additive relationships of cultivars*

The study describes 612 wheat cultivars released in Brazil between 1920 and 2024. The pedigree-based relationship analyses reported in the article used 569 cultivars with sufficient pedigree information. The repository currently contains the reconstructed pedigree and the supplied 610 × 610 relationship matrix. The exact 569-cultivar analysis subset and the cultivar metadata used for comparisons by release period and breeding organization will be added after final reconciliation with the analytical dataset.

## Repository contents

- `data/raw/Pedigree.txt`: tab-delimited pedigree with one genotype and its two recorded parents per row.
- `data/raw/Amatrix.txt`: numerator additive relationship matrix for 610 target genotypes.
- `code/01_rebuild_additive_matrix.R`: rebuilds the full additive relationship matrix with AGHmatrix, extracts the 610 target genotypes, and verifies agreement with the supplied matrix.
- `code/02_validate_data.py`: checks the pedigree and relationship-matrix structure and writes a validation summary.
- `docs/data_dictionary.md`: field definitions and interpretation.
- `docs/validation_report.md`: checks performed on the deposited files.

## Data overview

The pedigree file contains 3,172 unique genotypes. The first 610 records are the target genotypes represented in `Amatrix.txt`; the remaining records are ancestors required to reconstruct their genealogies. Unknown parents are coded as `0`.

`Amatrix.txt` is a symmetric 610 × 610 numerator additive relationship matrix. Rows and columns use the same unique genotype identifiers. Diagonal elements represent self-relationships and must be excluded when calculating cultivar-level mean additive relationships.

## Reproducing the supplied matrix

The R script requires the `AGHmatrix` package.

```r
install.packages("AGHmatrix")
source("code/01_rebuild_additive_matrix.R")
```

The script constructs the full numerator additive relationship matrix from `Pedigree.txt`, extracts the target genotypes in the order supplied by `Amatrix.txt`, and checks numerical agreement.

## Important scope note

The article distinguishes between:

- 612 cultivars in the historical dataset;
- 569 cultivars included in additive relationship analyses; and
- 43 cultivars retained only for historical and descriptive analyses because pedigree information was insufficient.

The current pedigree file includes 610 target genotypes, so the deposited matrix is a broader source matrix rather than the final 569-cultivar analytical subset. The inclusion list and cultivar metadata must be deposited before this repository can reproduce all analyses reported in the article.

## Citation

Please cite the accompanying article. A complete bibliographic reference and DOI will be added when available. Citation metadata are also provided in `CITATION.cff`.

## Contact

Maicon Nardino, Universidade Federal de Viçosa, Brazil.

