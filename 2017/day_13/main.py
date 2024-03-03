# Problem type:
# ~~~~~~~~~~~~ thinker ~~~~~~~~~~~~
filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_scan = {}
for line in lines:
    segs = line.split(": ")
    dict_scan[int(segs[0])] = {"tot": int(segs[1]), "pos": 0, "dir": 1}

min_gate = min(list(dict_scan))
max_gate = max(list(dict_scan))

# print("dict_scan", dict_scan)

s = 0
for curr_gate in range(min_gate, max_gate + 1):
    if curr_gate in dict_scan and dict_scan[curr_gate]["pos"] == 0:
        # print("** curr_gate:", curr_gate, dict_scan[curr_gate]["tot"])
        s += curr_gate * dict_scan[curr_gate]["tot"]

    # Move scans. They go back and forth.
    for k, v in dict_scan.items():
        new_pos = v["pos"] + v["dir"]
        # Reached end. Go the other way.
        if new_pos == v["tot"] - 1:
            dict_scan[k]["dir"] = -1
        elif new_pos == 0:
            dict_scan[k]["dir"] = 1
        dict_scan[k]["pos"] = new_pos
    # print(" --- updated dict scan: dict_scan", dict_scan)

print("Part 1:", s)

# Part 2, let's try to bruteforce but maybe we need LCM. Indeed too slow. There
# is some mod relationship we can use which is probably faster than dictionary
# updates.
def get_dict_scan():
    lines = open(filename, encoding="utf-8").read().splitlines()

    dict_scan = {}
    for line in lines:
        segs = line.split(": ")
        # Only need to keep the periodicity and since we are going back and forth,
        # the actual periodicity is 2 * n - 2
        dict_scan[int(segs[0])] = int(segs[1]) * 2 - 2

    min_gate = min(list(dict_scan))
    max_gate = max(list(dict_scan))
    return dict_scan, min_gate, max_gate



def is_caught(dict_scan, min_gate, max_gate, delay):
    # See if we can get through.
    for curr_gate in range(min_gate, max_gate + 1):
        pos_with_delay = curr_gate + delay
        if (curr_gate in dict_scan) and pos_with_delay % dict_scan[curr_gate] == 0:
            return True
    return False


delay = -1
dict_scan, min_gate, max_gate = get_dict_scan()
while True:
    delay += 1
    if delay % 10000 == 0:
        print("  ... curr delay:", delay)
    if not is_caught(dict_scan, min_gate, max_gate, delay):
        break

print("Part 2:", delay)

exit()

def update_dict_scan(dict_scan):
    for k, v in dict_scan.items():
        new_pos = v["pos"] + v["dir"]
        # Reached end. Go the other way.
        if new_pos == v["tot"] - 1:
            dict_scan[k]["dir"] = -1
        elif new_pos == 0:
            dict_scan[k]["dir"] = 1
        dict_scan[k]["pos"] = new_pos
    return dict_scan


def is_caught(delay):
    # First do the delay.
    dict_scan, min_gate, max_gate = get_dict_scan()
    for _ in range(delay):
        dict_scan = update_dict_scan(dict_scan)

    # Then see if we can get through.
    for curr_gate in range(min_gate, max_gate + 1):
        if curr_gate in dict_scan and dict_scan[curr_gate]["pos"] == 0:
            return True
        dict_scan = update_dict_scan(dict_scan)
    return False


delay = -1
while True:
    delay += 1
    if delay % 100 == 0:
        print("  ... curr delay:", delay)
    if not is_caught(delay):
        break

print("Part 2:", delay)
