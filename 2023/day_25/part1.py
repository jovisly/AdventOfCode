import networkx as nx
from networkx.algorithms.community import girvan_newman

def get_node(line):
    source, targets = line.split(":")
    targets = targets.split(" ")
    targets = [t.strip() for t in targets if t != ""]
    return source, targets


def get_dict_graph(lines):
    graph = {}
    for line in lines:
        source, targets = get_node(line)
        graph[source] = targets
    return graph


def convert_to_graph(dict_graph):
    G = nx.DiGraph()
    for node, edges in dict_graph.items():
        G.add_edges_from((node, edge) for edge in edges)
    return G


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    G = convert_to_graph(get_dict_graph(lines))

    # Find communities.
    # https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm
    # https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.centrality.girvan_newman.html
    comp = girvan_newman(G)
    first_pair = tuple(sorted(c) for c in next(comp))
    assert len(first_pair) == 2

    return len(first_pair[0]) * len(first_pair[1])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 54


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
