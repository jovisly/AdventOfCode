import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

num = 0
for line in lines:
    l = line.strip()
    ns = l.split(" ")
    ns = [n.strip() for n in ns]
    ns = [int(n) for n in ns if n]
    if ns[0] + ns[1] > ns[2] and ns[1] + ns[2] > ns[0] and ns[2] + ns[0] > ns[1]:
        num += 1

print(num)
