def describe_csr_matrix(x):
    nrow, ncol = x.get_shape()
    sparsity = 100 * (1 - x.count_nonzero() / (nrow * ncol))
    description = "{:d} x {:d} sparse matrix with {:.2f}% of sparsity."

    return description.format(nrow, ncol, sparsity)
