import csv
import sys

import numpy as np
from numpy.testing import assert_allclose

damping = 0.85  # damping factor
max_iter = 10  # maximum iterations
tol = 1e-7  # maximum tolerance between pagerank results of two consequtive iterations


with open(sys.argv[1], "r") as f:
    reader = csv.reader(f, delimiter=" ")
    n = int(sys.argv[2])
    print(n)
    A = np.zeros((n, n), dtype=float)
    # src = source, dst = destination
    for src, dst in reader:
        # populate the A matrix in index (dst, src)
        A[int(dst) - 1][int(src) - 1] = 1.0
    for i in range(n):
        # handle dangling nodes
        if np.all(A[:, i] == 0.0):
            A[:, i] = 1.0 / n
        else:
            A[:, i] = A[:, i] / np.sum(A[:, i])

# create M matrix from A, incorporating damping factor
M = damping * A + ((1 - damping) / n) * np.ones((n, n), dtype=float)

# create initial pagerank
x = np.ones((n,), dtype=float) / n
x_trail = np.copy(x)

for _ in range(max_iter):
    # print(x)
    x = np.inner(M, x_trail)
    if np.max(np.abs(x - x_trail)) <= tol:
        break
    x_trail = x


print(x)
