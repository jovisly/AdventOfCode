import math
import networkx as nx
import utils

IS_TEST = False

if IS_TEST:
    filename = "input-test.txt"
    num_connections = 10
else:
    filename = "input.txt"
    num_connections = 1000

lines = open(filename, encoding="utf-8").read().splitlines()

def get_pos(pos_str: str) -> tuple[int, int, int]:
    return tuple(int(x) for x in pos_str.split(","))


def get_dict_pos(lines: list[str]) -> dict[str, tuple[int, int, int]]:
    return {
        pos: get_pos(pos) for pos in lines
    }

def get_dist(pos1: tuple[int, int, int], pos2: tuple[int, int, int]) -> int:
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 + (pos1[2] - pos2[2])**2)


def get_all_dist(dict_pos: dict[str, tuple[int, int, int]]) -> dict[str, int]:
    dict_dist = {}
    for pos1_name, pos1_val in dict_pos.items():
        for pos2_name, pos2_val in dict_pos.items():
            if pos1_name != pos2_name:
                dist = get_dist(pos1_val, pos2_val)
                # Sort the names to get unique key.
                names = sorted([pos1_name, pos2_name])
                key = ":".join(names)
                dict_dist[key] = dist

    return dict_dist

dict_pos = get_dict_pos(lines)
dict_dist = get_all_dist(dict_pos)

# Filter the dictionary down to the N shortest distances.
shortest_distances = sorted(dict_dist.values())[:num_connections]
dict_dist_shortest_n = {k: v for k, v in dict_dist.items() if v in shortest_distances}

# print(dict_dist)
# print(len(dict_dist))

G = nx.Graph()
G.add_nodes_from(list(dict_pos.keys()))
G.add_edges_from([tuple(k.split(":")) for k in dict_dist_shortest_n.keys()])
num_clusters = nx.number_connected_components(G)
cluster_sizes = [len(component) for component in nx.connected_components(G)]
cluster_sizes_sorted = sorted(cluster_sizes, reverse=True)
top_3 = cluster_sizes_sorted[:3]


print("Part 1:", top_3[0] * top_3[1] * top_3[2])


# Keep connecting until we have 1 cluster.
shortest_distances = sorted(dict_dist.values())
G.add_nodes_from(list(dict_pos.keys()))

G = nx.Graph()
out = 0
for dist in shortest_distances:
    # print("DIST:", dist)
    pair = [k for k, v in dict_dist.items() if v == dist][0]
    # print("pair:", pair)
    # print("pair.split(:):", tuple(pair.split(":")))
    G.add_edges_from([tuple(pair.split(":"))])
    num_clusters = nx.number_connected_components(G)
    cluster_sizes = [len(component) for component in nx.connected_components(G)]

    n1, n2 =pair.split(":")
    x1 = int(n1.split(",")[0])
    x2 = int(n2.split(",")[0])

    if num_clusters == 1 and cluster_sizes[0] == len(dict_pos):
        out = x1 * x2
        break

print("Part 2:", out)
