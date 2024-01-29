"""
Reflections: 2015 has two days that were particularly difficult - day 19 and
the MTG day (22). Day 7 and Day 15 were mildly difficult. Others were all not
too bad!
"""
def get_next_ind(curr_ind):
    r, c = curr_ind
    if r == 1:
        return (c + 1, 1)
    else:
        return (r - 1, c + 1)


def get_next_val(curr_val):
    return (curr_val * 252533) % 33554393

def solve():
    dict_vals = {}
    curr_ind = (1, 1)
    curr_val = 20151125
    dict_vals[curr_ind] = curr_val
    # From input data.
    target = (2978, 3083)

    while True:
        curr_ind = get_next_ind(curr_ind)
        curr_val = get_next_val(curr_val)
        dict_vals[curr_ind] = curr_val

        if curr_ind == target:
            break

    print("Part 1:", dict_vals[target])
    print("Part 2:", "Snow begins to fall!")



if __name__ == "__main__":
    solve()


