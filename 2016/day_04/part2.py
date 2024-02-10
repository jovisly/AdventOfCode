import utils
from part1 import parse_line

o_min = 97

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


for line in lines:
    id, _, _ = parse_line(line)
    encrypted = line.split("[")[0].replace(str(id), "")
    decrypted = ""
    for char in encrypted:
        if char == "-":
            decrypted += " "
        else:
            o = ord(char) - o_min
            o += id
            o = o % 26 + o_min
            c = chr(o)
            decrypted += c

    if "north" in decrypted:
        print(id, decrypted)
