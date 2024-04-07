# Problem type:
# ~~~~~~~~~~~~ bug fest ~~~~~~~~~~~~
from collections import defaultdict
from tqdm import tqdm

PADDING = 10

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def get_xy(line):
    segs = line.split(", ")
    segs = [int(s) for s in segs]
    return segs[0], segs[1]


def get_closest(xy, list_xy):
    dict_dist = {}
    for ind, pos_xy in enumerate(list_xy):
        dist = abs(xy[0] - pos_xy[0]) + abs(xy[1] - pos_xy[1])
        dict_dist[ind] = dist

    min_val = min(dict_dist.values())
    min_ind = [k for k, v in dict_dist.items() if v == min_val]
    if len(min_ind) > 1:
        return None
    else:
        return min_ind[0]


list_xy = [get_xy(line) for line in lines]
min_x = min([xy[0] for xy in list_xy])
max_x = max([xy[0] for xy in list_xy])

min_y = min([xy[1] for xy in list_xy])
max_y = max([xy[1] for xy in list_xy])

dict_cnt = defaultdict(int)
disq = set()

for x in tqdm(range(min_x - PADDING, max_x + PADDING + 1)):
    for y in range(min_y - PADDING, max_y + PADDING + 1):
        closest_ind = get_closest((x, y), list_xy)
        if closest_ind is not None:
            if x == min_x - PADDING or x == max_x + PADDING or y == min_y - PADDING or y == max_y + PADDING:
                disq.add(closest_ind)
            else:
                dict_cnt[closest_ind] += 1

new_dict = {k: v for k, v in dict_cnt.items() if k not in disq}
max_val = max(new_dict.values())
print("Part 1:", max_val)


def is_close(xy, list_xy):
    dist_thresh = 10000 if filename == "input.txt" else 32
    dist_sum = 0
    for ind, pos_xy in enumerate(list_xy):
        dist = abs(xy[0] - pos_xy[0]) + abs(xy[1] - pos_xy[1])
        dist_sum += dist
    if dist_sum >= dist_thresh:
        return False
    else:
        return True


num = 0
for x in tqdm(range(min_x - PADDING, max_x + PADDING + 1)):
    for y in range(min_y - PADDING, max_y + PADDING + 1):
        if is_close((x, y), list_xy):
            num += 1

print("Part 2:", num)
