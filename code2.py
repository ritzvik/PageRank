import csv
import sys

import numpy as np
from numpy.testing import assert_allclose

damping = 0.85
max_iter = 10
tol = 1e-7


with open(sys.argv[1], "r") as f:
    reader = csv.reader(f, delimiter=" ")
    n = int(sys.argv[2])
    print(n)
    A = np.zeros((n, n), dtype=float)
    for src, dst in reader:
        A[int(dst) - 1][int(src) - 1] = 1.0
    for i in range(n):
        if np.all(A[:, i] == 0.0):
            A[:, i] = 1.0 / n
        else:
            A[:, i] = A[:, i] / np.sum(A[:, i])

M = damping * A + ((1 - damping) / n) * np.ones((n, n), dtype=float)
M_ = np.zeros((n + 1, n + 1), dtype=float)
M_.fill((1 - damping) / n)
M_[n, :].fill(0)
M_[n, n] = 1.0
M_[:n, :n] = damping * A

x = np.ones((n,), dtype=float) / n
x_trail = np.copy(x)
y = np.ones((n + 1,), dtype=float) / n
y[n] = 1.0
y_trail = np.copy(y)

for _ in range(max_iter):
    x = np.inner(M, x_trail)
    y = np.inner(M_, y_trail)
    if np.max(np.abs(x - x_trail)) <= tol:
        break
    x_trail = x
    y_trail = y

assert_allclose(x, y[:-1], rtol=0.0, atol=1e-8)

print(x)
