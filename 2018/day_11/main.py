# Problem type:
# ~~~~~~~ Oof I need to learn a new thing ~~~~~~~
# And the new thing is called Summed Area Table.

SERIAL_NUM = 18
SERIAL_NUM = 7689
# SERIAL_NUM = 42

def get_hundredth(num):
    s = str(num)
    if len(s) >= 3:
        return int(s[-3])
    else:
        return 0


def get_val(x, y, serial_num=SERIAL_NUM):
    rack_id = 10 + x
    power = rack_id * y
    power += serial_num
    power *= rack_id
    power = get_hundredth(power)
    return power - 5


dict_grid = {}
for x in range(1, 300 + 1):
    for y in range(1, 300 + 1):
        dict_grid[(x, y)] = get_val(x, y)


# Now get the biggest sum.
biggest_sum = 0
biggest_pos = None
for x in range(1, 300 + 1):
    for y in range(1, 300 + 1):
        list_vals = [
            (x, y), (x, y + 1), (x, y + 2),
            (x + 1, y), (x + 1, y + 1), (x + 1, y + 2),
            (x + 2, y), (x + 2, y + 1), (x + 2, y + 2),
        ]
        list_vals = [v for v in list_vals if v in dict_grid]
        if len(list_vals) == 9:
            s = sum([dict_grid[v] for v in list_vals])
            if s > biggest_sum:
                biggest_sum = s
                biggest_pos = list_vals[0]

print("Part 1:", biggest_pos)

# Part 2.
from tqdm import tqdm
from collections import defaultdict

dict_sat = defaultdict(int)
# define a dict for summed area table:
# https://en.wikipedia.org/wiki/Summed-area_table
for x in range(1, 300 + 1):
    for y in range(1, 300 + 1):
        dict_sat[(x, y)] = (
            dict_grid[(x, y)]
            + dict_sat[(x-1, y)]
            + dict_sat[(x, y-1)]
            - dict_sat[(x-1, y-1)]
            )


def get_sum(x1, y1, x2, y2):
    return (
        dict_sat[(x2, y2)]
        - dict_sat[(x1, y2)]
        - dict_sat[(x2, y1)]
        + dict_sat[(x1, y1)]
    )


biggest_sum = 0
biggest_ans = None


for n in tqdm(range(1, 300 + 1)):
    for x in range(1, 302 - n):
        for y in range(1, 302 - n):
            s = get_sum(x-1, y-1, x+n-1, y+n-1)
            if s > biggest_sum:
                biggest_sum = s
                biggest_ans = (x, y, n)

print("Part 2:", biggest_sum, biggest_ans)



# v2. Still too slow.
exit()
import heapq

biggest_sum = 0
biggest_ans = None

queue = [[pos] for pos in dict_grid.keys()]
prev_len = len(queue)

while len(queue) > 0:
    if len(queue) != prev_len:
        print("QUEUE LENGTH:", len(queue))
        prev_len = len(queue)
    list_vals = queue.pop()
    len_vals = len(list_vals)
    list_vals = [v for v in list_vals if v in dict_grid]
    n = len_vals**0.5
    if len(list_vals) == len_vals and int(n) == n:
        s = sum([dict_grid[v] for v in list_vals])
        if s > biggest_sum:
            biggest_sum = s
            biggest_ans = str(list_vals[0][0]) + "," +  str(list_vals[0][1]) + "," + str(int(len_vals**0.5))

            print("Updating new sum to", biggest_sum, biggest_ans)

        # Expand the square.
        m = int(n) + 1
        min_x = list_vals[0][0]
        min_y = list_vals[0][1]
        list_vals += [(min_x + m, min_y + i) for i in range(1, m)] + [(min_x + i, min_y + m) for i in range(1, m)] + [(min_x + m, min_y + m)]
        queue.append(list_vals)

print("Part 2:", biggest_sum, biggest_ans)

exit()

# v1. way too slow.
def get_coords(x, y, n):
    return [(x + i, y + j) for i in range(n) for j in range(n)]

biggest_sum = 0
biggest_pos = None
biggest_n = None

queue = [(pos[0], pos[1], 1) for pos in dict_grid.keys()]

prev_len = len(queue)

while len(queue) > 0:
    if len(queue) != prev_len:
        print("QUEUE LENGTH:", len(queue))
        prev_len = len(queue)
    x, y, n = heapq.heappop(queue)
    list_vals = get_coords(x, y, n)
    len_vals = len(list_vals)
    list_vals = [v for v in list_vals if v in dict_grid]
    if len(list_vals) == len_vals:
        s = sum([dict_grid[v] for v in list_vals])
        if s > biggest_sum:
            biggest_sum = s
            biggest_pos = list_vals[0]
            biggest_n = n
            print("Updating new sum to", biggest_sum)
        # Also add a new queue.
        heapq.heappush(queue, (x, y, n + 1))


print("Part 2:", biggest_sum, biggest_pos)
