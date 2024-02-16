# Probably can use lcm but bruteforce is fast enough.
filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

list_d = []
for line in lines:
    segs = line.split(" ")
    num_pos = int(segs[3])
    start_pos = int(segs[-1][:-1])
    list_d.append((num_pos, start_pos))


PART2 = False
if PART2 == True:
    list_d.append((11, 0))


def test_drop_time(t_drop):
    t = t_drop
    success = True
    for d in list_d:
        t += 1
        num_pos, start_pos = d
        curr_pos = (start_pos + t) % num_pos
        if curr_pos != 0:
            success = False
    return success


# We will just try to do the dropping from time t = 0 onward.
t_drop = 0
while True:
    out = test_drop_time(t_drop)
    if out == True:
        print(t_drop)
        exit()
    t_drop += 1

