"""
Reflections: A nice chill network problem.
"""
from tqdm import tqdm
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


def sort_nodes(nodes):
    return tuple(sorted(nodes))


connections = set()
nodes = set()
for line in lines:
    a, b = line.split("-")
    connections.add(sort_nodes((a, b)))
    nodes.add(a)
    nodes.add(b)

connections_tri = set()
connections_tri_t = set()
for connection in tqdm(connections):
    a, b = connection
    for c in nodes:
        if c != a and c != b and sort_nodes((a, c)) in connections and sort_nodes((b, c)) in connections:
            connections_tri.add(sort_nodes((a, b, c)))
            if a.startswith("t") or b.startswith("t") or c.startswith("t"):
                connections_tri_t.add(sort_nodes((a, b, c)))


print("Part 1:", len(connections_tri_t))

import networkx as nx

def find_interconnected_groups(connections, nodes):
    G = nx.Graph()

    G.add_nodes_from(nodes)
    G.add_edges_from(connections)

    return list(nx.find_cliques(G))

cliques = find_interconnected_groups(connections, nodes)

# Get the largest clique.
largest_clique = max(cliques, key=len)

print("Part 2:", ",".join(sorted(largest_clique)))
