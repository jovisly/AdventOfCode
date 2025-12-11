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
import networkx as nx

def get_graph(dict_device):
    G = nx.DiGraph()
    for node, neighbors in dict_device.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G

def count_paths(start, end, dict_device, graph):
    # Only consider nodes that can reach end.
    eligible = nx.ancestors(graph, end) | {end}

    if start not in eligible:
        return 0

    # Only count path; don't track them.
    path_counts = {start: 1}
    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()

        if current == end:
            continue

        neighbors = dict_device.get(current, [])
        for neighbor in neighbors:
            if neighbor in eligible:
                # Add paths: all paths to current also lead to neighbor
                if neighbor not in path_counts:
                    path_counts[neighbor] = 0

                path_counts[neighbor] += path_counts[current]

                # Add to queue if we haven't seen it yet
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return path_counts.get(end, 0)


filename = "input.txt"
# filename = "input-test2.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_device = process_lines(lines)
graph = get_graph(dict_device)

# "svr" -> "dac" -> "fft" -> "out"
print("svr to dac")
a = count_paths("svr", "dac", dict_device, graph)
print("dac to fft")
b = count_paths("dac", "fft", dict_device, graph)
print("fft to out")
c = count_paths("fft", "out", dict_device, graph)

# "svr" -> "fft" -> "dac" -> "out"
print("svr to fft")
d = count_paths("svr", "fft", dict_device, graph)
print("fft to dac")
e = count_paths("fft", "dac", dict_device, graph)
print("dac to out")
f = count_paths("dac", "out", dict_device, graph)

print("Part 2:", a * b * c + d * e * f)
