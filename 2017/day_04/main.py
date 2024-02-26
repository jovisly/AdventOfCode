from collections import Counter

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

tot = 0
for line in lines:
    ws = line.split(" ")
    cnts = Counter(ws)
    if max(cnts.values()) == 1:
        tot += 1

print("Part 1:", tot)



def has_anagram(ws):
    for i in range(len(ws)):
        for j in range(i + 1, len(ws)):
            wi = ws[i]
            wj = ws[j]
            if sorted(list(wi)) == sorted(list(wj)):
                return True
    return False



tot = 0
for line in lines:
    ws = line.split(" ")
    if has_anagram(ws) == False:
        tot += 1

print("Part 2:", tot)
