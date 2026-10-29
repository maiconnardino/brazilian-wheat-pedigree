/opt/homebrew/Library/Homebrew/cmd/shellenv.sh: line 18: /bin/ps: Operation not permitted
#!/usr/bin/env Rscript

if (!requireNamespace("AGHmatrix", quietly = TRUE)) {
  stop("Package 'AGHmatrix' is required. Install it with install.packages('AGHmatrix').")
}

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg) == 1) {
  normalizePath(sub("^--file=", "", file_arg))
} else {
  normalizePath("code/01_rebuild_additive_matrix.R")
}

repo_dir <- dirname(dirname(script_path))
data_dir <- file.path(repo_dir, "data", "raw")
output_dir <- file.path(repo_dir, "data", "derived")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

pedigree <- read.delim(
  file.path(data_dir, "Pedigree.txt"),
  stringsAsFactors = FALSE,
  check.names = FALSE
)

supplied_A <- as.matrix(read.table(
  file.path(data_dir, "Amatrix.txt"),
  header = TRUE,
  row.names = 1,
  check.names = FALSE
))

full_A <- AGHmatrix::Amatrix(
  data = pedigree,
  ploidy = 2,
  verify = TRUE
)

target_ids <- rownames(supplied_A)
if (!all(target_ids %in% rownames(full_A))) {
  stop("At least one target genotype is absent from the reconstructed matrix.")
}

rebuilt_A <- full_A[target_ids, target_ids, drop = FALSE]
max_abs_difference <- max(abs(rebuilt_A - supplied_A))

write.table(
  rebuilt_A,
  file.path(output_dir, "Amatrix_rebuilt.txt"),
  quote = TRUE,
  sep = " ",
  col.names = NA
)

message("Rebuilt matrix dimensions: ", paste(dim(rebuilt_A), collapse = " x "))
message("Maximum absolute difference from supplied matrix: ",
        format(max_abs_difference, digits = 16))

if (max_abs_difference > 1e-12) {
  stop("The rebuilt matrix does not agree with the supplied matrix within tolerance.")
}

