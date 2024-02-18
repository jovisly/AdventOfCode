"""
Oof this one took a few hours. I mistakenly thought I can heapq out of it, but I
couldn't get the search to be efficient enough. Then I gave up on that approach
and look for something simpler: based on the example, there's only one node with
enough capacity. So I tried to just measure distance. That gave me an answer too
low. Then I realized there's a "wall". But still the answer was wrong. It took me
a long while to realize that the example did not require an important mechanism
of "having the high capacity node" follow around to move the target (where the
5x comes from). I suppose this one, and day 11, are the toughies of 2016 (so far).
"""
import copy
import heapq
from utils import get_neighbors

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

files = [line for line in lines if line.startswith("/dev/grid/node")]

dict_nodes = {}
max_x = 0
max_y = 0
for file in files:
    segs = file.split(" ")
    segs = [s for s in segs if s]
    used = int(segs[2][:-1])
    avail = int(segs[3][:-1])
    name = segs[0]
    node_id = name.split("/")[-1]
    x = int(node_id.split("-")[-2][1:])
    y = int(node_id.split("-")[-1][1:])
    dict_nodes[(x, y)] = {"used": used, "avail": avail}
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

print("** num nodes:", len(dict_nodes))
print("** max x:", max_x)
print("** max y:", max_y)

REQUIRED_SPACE = dict_nodes[(max_x, 0)]["used"]
print("** size needed:", REQUIRED_SPACE)

def get_simple_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x2-x1) + abs(y2-y1)


# We can see there is only ONE NODE that can accomodate the target node. That's
# why we get stuck because it'd take several steps before we move it close to
# target node. so we need to prioritize getting it close to the target.
print("** node(s) with available size:")
list_nodes = []
for k, v in dict_nodes.items():
    if v["avail"] >= dict_nodes[(max_x, 0)]["used"]:
        print("  ", k, v)
        list_nodes.append(k)

# There should only be 1.
good_node = list_nodes[0]

GOAL = (0, 0)
START = (max_x, 0)
TARGET = START
print("GOAL:", GOAL)
print("TARGET:", TARGET)
print("GOOD NODE:", good_node)

# Basically we can argue that the number of steps will be:
# * [dist1]: num of steps to move the good node to right next to TARGET
# * [1]: plus 1 to move data into good node, which makes TARGET empty
# * [dist2]: plus num of steps to move TARGET (which is now empty) to GOAL -- it might not be a straight line if goal is in the way.
# * [1] plus 1 to move the data into GOAL.

# dist1 has two options: to (max_x-1, 0), or (max_x, 1). we can try them both.
dist1 = get_simple_dist(good_node, (max_x - 1, 0))
dist2 = get_simple_dist(TARGET, GOAL) + 2
dist3 = get_simple_dist((max_x - 1, 0), (1, 0))
print(f"dist1: {dist1}, dist2: {dist2}, dist3: {dist3}")
tot = dist1 + dist2 + 2 + dist3
# There is actually a dist3 not in the test data set: we need to move the target
# data to right next to the GOAL.
print("tot option 1:", tot)

# 119 is too low. 120 is too low. 130 is too low. 235 def wrong.

# I'm suspecting that there are nodes on the way that can't be accomodated by
# 92, which is the largest capacity.
print("=====")
list_too_big = []
for k, v in dict_nodes.items():
    if v["used"] > dict_nodes[good_node]["avail"]:
        print("Too big:", k, v)
        list_too_big.append(k)

# Ok funnily this feels like a good RL question now because we basically have
# obstacles.

# Let's visualize it.
for y in range(max_y + 1):
    v = ""
    for x in range(max_x + 1):
        if (x, y) == good_node:
            v += "_"
        elif (x, y) in list_too_big:
            v += "#"
        elif (x, y) == GOAL:
            v += "G"
        elif (x, y) == TARGET:
            v += "T"
        else:
            v += "."
    print(v)

# Ok i see i'm missing the part where the good node needs to follow the target
# data until its destination. this part multiplies by 5 because the good node
# needs to shuffle around it.
# dist1: moving the good node up while avoiding the wall. ends at (7,0)
dist1 = 9 + 3 + 2 + 3 + 6
# dist2: move the good note to right next to target
dist2 = 28
# dist3: move the target and empty note together to get the target right next to
# end.
dist3 = 35 * 5
# Add one last move to move target to goal.
print(dist1 + dist2 + dist3 + 1)

# All the stuff below is for priority queue which didn't work out.
exit()
def get_path_str(source, target, prev_path=""):
    xs, ys = source
    xt, yt = target
    new_path = f"({xs},{ys})-({xt},{yt})"
    if len(prev_path) > 0:
        return prev_path + "|" + new_path
    else:
        return new_path


def get_dist(path, dict_nodes):
    """Given path traveled so far, identify how much more to go.

    We also return how far is available space to the data we want.
    """
    xs, ys = START

    # Identify how far is available space.
    nodes_with_space = [
        k for k, v in dict_nodes.items() if v["avail"] >= REQUIRED_SPACE
    ]

    # Easy if we haven't moved the data at all.
    if f"({xs},{ys})" not in path:
        # There should only be 1 but we can take min.
        dist_to_space = min([
            abs(xs - n[0]) + abs(ys - n[1])
            for n in nodes_with_space
        ])
        return max_x, dist_to_space

    # If we have moved the data, then it gets trickier.
    steps = path.split("|")
    curr_pos = START
    for step in steps:
        s, e = step.split("-")
        s = eval(s)
        e = eval(e)
        if s == curr_pos:
            curr_pos = e

    dist_to_goal = abs(curr_pos[0] - GOAL[0]) + abs(curr_pos[1] - GOAL[1])
    dist_to_space = min([
        abs(curr_pos[0] - n[0]) + abs(curr_pos[1] - n[1])
        for n in nodes_with_space
    ])

    # Just do a simple manhattan / taxicab distance.
    return (dist_to_goal, dist_to_space)


path = f"(2,2)-(1,2)|({max_x},0)-({max_x},1)|(4,5)-(5,5)|({max_x},1)-({max_x},2)"
# assert get_dist(path, dict_nodes)[0] == 2 + max_x

# Create the starting queue where, for each node, we see if we can move its data
# to a neighbor. Each queue has the structure of (num_steps, dist_to_goal)
queue = []
visited = set()
for k, v in dict_nodes.items():
    if v["used"] == 0:
        continue
    neighbors = get_neighbors(k)
    # Filter for only neighbors that can accomodate incoming data.
    neighbors = [
        n for n in neighbors
        if n in dict_nodes and dict_nodes[n]["avail"] >= v["used"]
    ]
    for n in neighbors:
        path = get_path_str(k, n)
        out = get_dist(path, dict_nodes)
        dist_to_goal, dist_to_space = get_dist(path, dict_nodes)
        queue.append((dist_to_space, 1, dist_to_goal, path))
        visited.add(path)

# print("*" * 20)
# print("QUEUE:", queue)
# print("*" * 20)

def get_curr_dict_nodes(dict_nodes, path):
    """Create an updated dict_nodes given a path."""
    dict_copy = copy.deepcopy(dict_nodes)
    steps = path.split("|")
    for step in steps:
        s, e = step.split("-")
        s = eval(s)
        e = eval(e)
        # Move data from s to e.
        data = dict_copy[s]["used"]
        dict_copy[s]["used"] = 0
        dict_copy[s]["avail"] += data
        # Hopefully this doesn't happen.
        if dict_copy[e]["used"] + data > dict_copy[e]["avail"]:
            raise ValueError("Exceeded node availability:", step, data, dict_copy[e])
        dict_copy[e]["used"] += data
        dict_copy[e]["avail"] -= data
    return dict_copy


exit()
min_dist = max_x + 1
min_dist_to_space = max_x + 1
max_steps = 0
# The actual search loop.
while len(queue) > 0:
    curr_dist_to_space, curr_cost, curr_dist, curr_path = heapq.heappop(queue)
    print("curr_dist_to_space:", curr_dist_to_space)
    if curr_dist < min_dist:
        min_dist = curr_dist
        print("New min distance:", min_dist)

    if curr_dist_to_space < min_dist_to_space:
        min_dist_to_space = curr_dist
        print("New min distance to space:", min_dist_to_space)

    if curr_cost > max_steps:
        print("New max steps:", curr_cost, len(queue))
        max_steps = curr_cost

    # print("=" * 20)
    # print("curr_dist:", curr_dist, curr_path)
    # If curr_dist is zero, then we are done.
    if curr_dist == 0:
        print("******* Found! Number of steps is:", curr_cost)
        exit()

    curr_dict_nodes = get_curr_dict_nodes(dict_nodes, curr_path)
    # print("curr_dict_nodes:", curr_dict_nodes)
    # Search for the next set of available moves.
    for k, v in curr_dict_nodes.items():
        if v["used"] == 0:
            continue
        neighbors = get_neighbors(k)
        neighbors = [
            n for n in neighbors
            if n in curr_dict_nodes and curr_dict_nodes[n]["avail"] >= v["used"]
        ]
        for n in neighbors:
            path = get_path_str(k, n, prev_path=curr_path)
            if path not in visited:
                dist_to_goal, dist_to_space = get_dist(path, curr_dict_nodes)
                heapq.heappush(queue, (dist_to_space, curr_cost + 1, dist_to_goal, path))
                visited.add(path)


# This search loop works for test data but extremely slow for the actual dataset,
# presumably because there wasn't much space near the starting point, so we can't
# use distance to prioritize until much later.
