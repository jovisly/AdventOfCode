filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

files = [line for line in lines if line.startswith("/dev/grid/node")]

parsed_files = []
for file in files:
    segs = file.split(" ")
    segs = [s for s in segs if s]
    used = int(segs[2][:-1])
    avail = int(segs[3][:-1])
    name = segs[0]
    parsed_files.append((name, used, avail))

# Get valid pairs.
tot = 0
for f1 in parsed_files:
    for f2 in parsed_files:
        n1, u1, a1 = f1
        n2, u2, a2 = f2
        if n1 != n2 and u1 > 0 and a2 >= u1:
            tot += 1

print(tot)
