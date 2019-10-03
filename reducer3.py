import sys

current_i = None
vsum = 0.0
n = int(sys.argv[1])

for line in sys.stdin:
    line = line.strip()
    i, vec_i = line.split(" ")
    i, vec_i = int(i), float(vec_i)
    if current_i is None:
        vsum = vec_i
        current_i = i
    elif i == current_i:
        vsum += vec_i
    else:
        print("{:04d} {}\n".format(current_i, vsum), end="")
        vsum = vec_i
        current_i = i

print("{:04d} {}\n".format(n, vsum), end="")
