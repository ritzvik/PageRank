import csv
import sys

import numpy as np

n = int(sys.argv[1])

with sys.stdin as f:
    reader = csv.reader(f, delimiter=" ")
    for src, dst in reader:
        print("{:04d}\t{:04d}".format(int(src) - 1, int(dst) - 1))
