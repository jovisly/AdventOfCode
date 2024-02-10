from collections import Counter
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


def parse_line(line):
    comps = line.split("-")
    data = comps[:-1]
    id = int(comps[-1].split("[")[0])
    checksum = comps[-1].split("[")[-1][:-1]
    return id, "".join(data), checksum


def get_checksum(chars):
    cnts = Counter(chars)
    freqs = [v[0] for v in sorted(cnts.items(), key=lambda kv: (-kv[1], kv[0]))]
    return "".join(freqs[:5])


tot = 0
for line in lines:
    id, chars, cs = parse_line(line)
    if get_checksum(chars) == cs:
        tot += id

print(tot)
