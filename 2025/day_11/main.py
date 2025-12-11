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

# Part 2: Same approach doesn't work (too slow).
# Try networkx
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.simple_paths.all_simple_paths.html
import networkx as nx

def get_graph(dict_device):
    G = nx.DiGraph()
    for node, neighbors in dict_device.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G


filename = "input.txt"
# filename = "input-test2.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_device = process_lines(lines)
graph = get_graph(dict_device)

start = "svr"
end = "out"

# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.dag.ancestors.html
can_reach_out = nx.ancestors(graph, end)
print("num nodes can reach out:", len(can_reach_out))
# print("can_reach_out:", can_reach_out)

dict_device_reduced = {k: v for k, v in dict_device.items() if k in can_reach_out or k == end}
graph_reduced = get_graph(dict_device_reduced)
print("built reduced graph")

all_paths = list(nx.all_simple_paths(graph_reduced, start, end))
print("found all paths")

reduced_paths = [
    p for p in all_paths if "dac" in p and "fft" in p
]

print("Part 2:", len(reduced_paths))
