import sys

damping = 0.85

n = int(sys.argv[1])

for line in sys.stdin:
    nums = line.strip().split(" ")
    src, dests = nums[0], nums[1:]
    src, dests = int(src), [int(d) for d in dests]
    n_dests = len(dests)

    if n_dests == 0:
        for i in range(n):
            print("{:04d} {:04d} {}".format(i, src, (damping / n)))
    else:
        for i in dests:
            print("{:04d} {:04d} {}".format(i, src, (damping / n_dests)))

    print("{:04d} {:04d} {}".format(src, n, (1 - damping) / n))

    if src == n - 1:
        print("{:04d} {:04d} {}".format(n, n, 1.0))
