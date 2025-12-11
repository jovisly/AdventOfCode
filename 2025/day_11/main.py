from collections import deque

filename = "input.txt"
filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def process_lines(lines):
    """Return a dictionary of input to list of outputs."""
    dict_device = {}
    for line in lines:
        i, os = line.split(":")
        i = i.strip()
        os = os.strip()
        os = os.split(" ")
        dict_device[i] = os

    return dict_device


dict_device = process_lines(lines)

start = "you"
end = "out"
queue = deque([(start, [start])])
all_paths = []

while queue:
    current, path = queue.popleft()

    if current == end:
        all_paths.append(path)
        continue

    neighbors = dict_device.get(current, [])
    for neighbor in neighbors:
        # No looping bac.
        if neighbor not in path:
            queue.append((neighbor, path + [neighbor]))

print("Part 1:", len(all_paths))




# Part 2: Same but just different start, plus we check paths at the end.

filename = "input.txt"
# filename = "input-test2.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_device = process_lines(lines)

start = "svr"
end = "out"
queue = deque([(start, [start])])
all_paths = []

while queue:
    current, path = queue.popleft()

    if current == end:
        all_paths.append(path)
        continue

    neighbors = dict_device.get(current, [])
    for neighbor in neighbors:
        # No looping bac.
        if neighbor not in path:
            queue.append((neighbor, path + [neighbor]))


# print("all_paths:", all_paths)
reduced_paths = [
    p for p in all_paths if "dac" in p and "fft" in p
]

print("Part 2:", len(reduced_paths))
