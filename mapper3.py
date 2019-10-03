import sys

import numpy as np

vecs = list()
with open(sys.argv[1], "r") as f:
    for line in f:
        vecs.append(float(line.strip().split(" ")[1]))
vecs = np.array(vecs)

for line in sys.stdin:
    line = line.strip()
    i, j, v = line.split(" ")
    i, j, v = int(i), int(j), float(v)
    vec_i = vecs[j] * v
    print("{:04d} {}".format(i, vec_i))
