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


# Part 2: Tried a few iterations...
def count_paths(start, end):
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
    return len(all_paths)


filename = "input.txt"
# filename = "input-test2.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_device = process_lines(lines)

# "svr" -> "dac" -> "fft" -> "out"
print("svr to dac")
a = count_paths("svr", "dac")
print("dac to fft")
b = count_paths("dac", "fft")
print("fft to out")
c = count_paths("fft", "out")

# "svr" -> "fft" -> "dac" -> "out"
print("svr to fft")
d = count_paths("svr", "fft")
print("fft to dac")
e = count_paths("fft", "dac")
print("dac to out")
f = count_paths("dac", "out")

print("Part 2:", a * b * c + d * e * f)
