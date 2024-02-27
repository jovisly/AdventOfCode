filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

# First pass; just get name and weight.
dict_d = {}
for line in lines:
    segs = line.split(" ")
    name = segs[0]
    weight = segs[1]
    weight = int(weight[1:-1])
    dict_d[name] = {"weight": weight, "parent": None, "children": []}


# Second pass; add parents.
for line in lines:
    segs = line.split(" ")

    if "->" in segs:
        parent = segs[0]
        children = []

        ind = segs.index("->")
        for i in range(ind + 1, len(segs)):
            name = segs[i]
            name = name.replace(",", "")
            dict_d[name]["parent"] = parent
            children.append(name)
        dict_d[parent]["children"] = children

no_parent = [k for k, v in dict_d.items() if v["parent"] is None]

print("Part 1:", no_parent)


# This answer comes from logging the program below. Which identified vrgxe as
# the source of inbalance. Then we can look up its original weight.
print("Part 2:", 1226 - 7)
exit()
parents = [k for k, v in dict_d.items() if len(v["children"]) > 0]


while len(parents) > 0:
    p = parents.pop()
    # Check if all the children do not have children.
    children = dict_d[p]["children"]
    # print("=" * 40)
    # print("parent:", p)
    # print("children:", children)
    # print([len(dict_d[c]["children"]) for c in children])
    # print("dict_d[ihnus]", dict_d["ihnus"])
    # for c in ['vrgxe', 'shnqfh', 'auzded', 'hkhsc', 'jwddn', 'mcxki', 'lhwyt']:
    #     print("--", c)
    #     print(dict_d[c])
    # print("=" * 40)
    if all([len(dict_d[c]["children"]) == 0 for c in children]):
        # Check that all children are balanced.
        weights = [dict_d[c]["weight"] for c in children]
        if all([w == weights[0] for w in weights]):
            # All match, then we weill say this parent is no longer a parent,
            # and has an effective weight of the total.
            dict_d[p]["children"] = []
            dict_d[p]["weight"] += sum(weights)
            parents = [k for k, v in dict_d.items() if len(v["children"]) > 0]
            # print("Remaining parents:", parents)
        else:
            # Otherwise, this node is not balanced. So let's raise an alert:
            print("Node is not balanced:", p, weights)
            print("children:", dict_d[p]["children"])
            break
    else:
        # This parent is not ready to be processed yet.
        parents = [p] + parents


