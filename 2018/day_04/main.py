# Problem type:
# ~~~~~~~~~~~~ bug fest ~~~~~~~~~~~~
from collections import defaultdict

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
lines = sorted(lines)

def get_guard(line):
    return line.split("] ")[1].split(" ")[1][1:]

def get_minute(line):
    return int(line.split("] ")[0].split(":")[1])

dict_sleep = defaultdict(int)
for line in lines:
    if "Guard" in line:
        guard = get_guard(line)
        start, end = None, None
    elif "falls asleep" in line:
        start = get_minute(line)
    elif "wakes up" in line:
        end = get_minute(line)
        dict_sleep[guard] += end - start
    else:
        raise ValueError(f"Unexpected format: {line}")

max_sleep = max(dict_sleep.values())
max_sleep_guard = [g for g, s in dict_sleep.items() if s == max_sleep][0]

# Then we need to see which minute is the guard sleeping the most.
dict_sleep = defaultdict(int)
for line in lines:
    if "Guard" in line:
        guard = get_guard(line)
        start, end = None, None
    elif "falls asleep" in line:
        start = get_minute(line)
    elif "wakes up" in line:
        end = get_minute(line)
        if guard == max_sleep_guard:
            for t in range(start, end + 1):
                dict_sleep[t] += 1
    else:
        raise ValueError(f"Unexpected format: {line}")


max_sleep = max(dict_sleep.values())
max_sleep_min = [g for g, s in dict_sleep.items() if s == max_sleep][0]

print("Part 1:", int(max_sleep_guard) * max_sleep_min)

# For part 2, now we need to track, for each guard, how many times they've slept
# at a given minute.
dict_sleep = {}
max_sleep = 0
max_min = None
max_guard = None
for line in lines:
    if "Guard" in line:
        guard = get_guard(line)
        start, end = None, None
    elif "falls asleep" in line:
        start = get_minute(line)
    elif "wakes up" in line:
        end = get_minute(line)
        if guard not in dict_sleep:
            dict_sleep[guard] = defaultdict(int)

        for t in range(start, end + 1):
            dict_sleep[guard][t] += 1
            if dict_sleep[guard][t] > max_sleep:
                max_sleep = dict_sleep[guard][t]
                max_min = t
                max_guard = guard
    else:
        raise ValueError(f"Unexpected format: {line}")

print("Part 2:", int(max_guard) * max_min)
