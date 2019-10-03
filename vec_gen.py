import sys

with open(sys.argv[1], "w") as f:
    n = int(sys.argv[2])
    for i in range(n):
        f.write("{:04d} {}\n".format(i, 1.0 / n))
    f.write("{:04d} {}\n".format(n, 1.0))
