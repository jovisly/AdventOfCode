from collections import Counter

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

num_chars = len(lines[0])
msg = ""
msg2 = ""
for i in range(num_chars):
    chars = [line[i] for line in lines]
    cnts = Counter(chars)
    max_cnt = max(cnts.values())
    char = [k for k, v in cnts.items() if v == max_cnt]
    if len(char) > 1:
        print("More than 1 top:", char)

    msg += char[0]

    # Part 2.
    min_cnt = min(cnts.values())
    char = [k for k, v in cnts.items() if v == min_cnt]
    if len(char) > 1:
        print("More than 1 min:", char)
    msg2 += char[0]

print(msg)
print(msg2)

