/opt/homebrew/Library/Homebrew/cmd/shellenv.sh: line 18: /bin/ps: Operation not permitted
# Validation report

Validation performed on 28 October 2026.

## Pedigree file

- 3,172 records and three fields.
- 3,172 unique genotype identifiers.
- No duplicated rows or blank cells.
- 645 records have both parents coded as `0`.
- One record has one known and one unknown parent.
- Every nonzero parent identifier occurs in the genotype column.
- No genotype is recorded as its own female or male parent.

## Additive relationship matrix

- Dimensions: 610 × 610.
- Unique row and column identifiers.
- Row identifiers and column identifiers are identical and in the same order.
- All 610 identifiers occur in the pedigree file.
- No missing or non-finite values.
- Exactly symmetric at the stored numerical precision.
- Minimum value: 0.
- Maximum value: 1.53542896232102.
- Diagonal range: 1 to 1.53542896232102.

## Reproduction check

The full numerator additive relationship matrix was reconstructed from `Pedigree.txt` with `AGHmatrix::Amatrix` using diploid ploidy. After extraction of the 610 target genotypes, the maximum absolute difference from `Amatrix.txt` was approximately 5.11 × 10⁻15, consistent with floating-point rounding.

## Unresolved reconciliation

The article reports 612 historical cultivars, 569 cultivars in relationship analyses, and 43 cultivars with insufficient pedigree information. The supplied matrix contains 610 target genotypes. Therefore, a final inclusion table is required to identify the 569 analyzed cultivars and the 41 target genotypes in this matrix that were not included in the published relationship comparisons. The two historical cultivars absent from the 610-target pedigree extract must also be identified in the cultivar metadata.

