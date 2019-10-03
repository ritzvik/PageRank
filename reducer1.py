import sys

n = int(sys.argv[1])
prevsrc = None

for line in sys.stdin:
    line = line.strip()
    src, dst = line.split("\t")
    src, dst = int(src), int(dst)
    if prevsrc is None:
        print("%d %d" % (src, dst), end=" ")
        prevsrc = src
    elif src == prevsrc:
        print(dst, end=" ")
    else:
        for s in range(prevsrc + 1, src):
            print("\n%d" % (s), end=" ")
        print("\n%d %d" % (src, dst), end=" ")
        prevsrc = src

for s in range(src + 1, n):
    print("\n%d" % (s), end=" ")

print("")
