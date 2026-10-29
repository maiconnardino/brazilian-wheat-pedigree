/opt/homebrew/Library/Homebrew/cmd/shellenv.sh: line 18: /bin/ps: Operation not permitted
# Data dictionary

## `Pedigree.txt`

Tab-delimited text file with 3,172 data rows.

| Field | Type | Description |
| --- | --- | --- |
| `genotype` | text | Unique genotype identifier. The first 610 identifiers are the target genotypes represented in `Amatrix.txt`; subsequent identifiers are ancestors used in pedigree reconstruction. |
| `female` | text | Recorded female parent identifier. `0` indicates an unknown or unavailable parent. |
| `male` | text | Recorded male parent identifier. `0` indicates an unknown or unavailable parent. |

All nonzero parent identifiers are present in the `genotype` column. Genotype identifiers are normalized for computational use and may omit spaces, punctuation, or diacritics found in cultivar names.

## `Amatrix.txt`

Whitespace-delimited square matrix with quoted genotype identifiers in the header and first column.

Each element \(A_{ij}\) is the numerator additive relationship between genotypes \(i\) and \(j\), reconstructed from the recorded pedigree. The matrix has 610 rows and 610 columns. Row and column identifiers are identical and in the same order.

Diagonal values \(A_{ii}\) are self-relationships. For the cultivar-level means described in the article, diagonal values must be excluded:

\[
\bar{A}_i = \frac{\sum_{j \ne i} A_{ij}}{n-1}.
\]

The article uses \(n=569\) for the final analytical subset. The present 610 × 610 file must therefore not be used to reproduce those means until the 569-cultivar inclusion list is deposited.

