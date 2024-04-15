# Problem type:
# ~~~~~~~ But it worked for test case T_T ~~~~~~~
# oof this one took me quite some time. My first attempt worked for test case
# but fails for the actual dataset. Turns out I understood the problem completely
# wrong. Had to think it over a few days to implement an alternative solution
# which also took some time. Quite a toughie for me.

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

class Node:
    def __init__(self, id, n_c, n_m, parent):
        self.id = id
        self.n_c = n_c
        self.n_m = n_m
        self.children = []
        self.metas = []
        self.parent = parent
        self.value = 0

    def get_value_by_sum(self):
        """For node without children."""
        self.value = sum(self.metas)

    def get_value_by_children(self, dict_nodes, debug=False):
        """For node with children."""
        v = 0
        for m in self.metas:
            if debug is True:
                print("m:", m)
            i = m - 1
            if i >= 0 and i < len(self.children):
                c = self.children[i]
                if debug is True:
                    print(" c:", c)
                v += dict_nodes[c].value
        self.value = v


nums = lines[0].split(" ")
nums = [int(n) for n in nums]

curr_id = 1
curr_parent = None
dict_nodes = {}

while len(nums) > 0:
    # Do we have a parent, and if so, check if the parent is ready to take meta.
    if curr_parent is not None:
        parent_node = dict_nodes[curr_parent]
        if len(parent_node.children) == parent_node.n_c:
            metas = nums[:parent_node.n_m]
            nums = nums[parent_node.n_m:]
            parent_node.metas = metas
            # Also ready to get its value.
            parent_node.get_value_by_children(dict_nodes)

            # And go back one level higher if possible.
            curr_parent = parent_node.parent
            continue

    # If we haven't encountered above, then we can take a new node.
    # Assign the first two numbers.
    n_c = nums[0]
    n_m = nums[1]
    nums = nums[2:]
    new_node = Node(id=curr_id, n_c=n_c, n_m=n_m, parent=curr_parent)
    if curr_parent is not None:
        dict_nodes[curr_parent].children.append(curr_id)

    # No more child means this node is a terminal node. Then meta values are
    # immediately after.
    if n_c == 0:
        metas = nums[:new_node.n_m]
        nums = nums[new_node.n_m:]
        new_node.metas = metas
        new_node.get_value_by_sum()
        # Return to the parent node.
        curr_parent = new_node.parent
    else:
        # Otherwise this node has children.
        curr_parent = new_node.id

    dict_nodes[curr_id] = new_node
    curr_id += 1


total = 0
for n in dict_nodes.values():
    # print("-" * 80)
    # print(n.__dict__)
    total += sum(n.metas)

print("Part 1:", total)

# Need to run it again for the head node.
dict_nodes[1].get_value_by_children(dict_nodes, debug=False)
print("Part 2:", dict_nodes[1].value)
