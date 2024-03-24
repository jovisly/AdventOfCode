# Problem type:
# ~~~~~~~~~~~~ string parsing ~~~~~~~~~~~~

from collections import defaultdict

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

state = lines[0].split(" ")[-1][:-1]
num = int(lines[1].split(" ")[-2])

lines = "\n".join(lines[3:])
lines = lines.split("\n\n")

# dict_states looks like
"""
{
    "a": {0: {"write": 1, "move": "l", "state": "b"}, 1: {"write": 1, "move": "l", "state": "b"}}
    ...
}
"""
dict_states = {}

for line in lines:
    sents = line.splitlines()
    s = sents[0].split(" ")[-1][:-1]
    sent_0_w = int(sents[2].split(" ")[-1][:-1])
    sent_0_m = sents[3].split(" ")[-1][:-1]
    sent_0_s = sents[4].split(" ")[-1][:-1]
    sent_1_w = int(sents[6].split(" ")[-1][:-1])
    sent_1_m = sents[7].split(" ")[-1][:-1]
    sent_1_s = sents[8].split(" ")[-1][:-1]
    dict_states[s] = {
        0: {"w": sent_0_w, "m": sent_0_m, "s": sent_0_s},
        1: {"w": sent_1_w, "m": sent_1_m, "s": sent_1_s},
    }


curr_pos = 0
curr_state = state
dict_reg = defaultdict(int)

for _ in range(num):
    v = dict_reg[curr_pos]
    ops = dict_states[curr_state][v]
    dict_reg[curr_pos] = ops["w"]
    if ops["m"] == "right":
        curr_pos += 1
    else:
        curr_pos -= 1
    curr_state = ops["s"]


print("Part 1:", sum(dict_reg.values()))

