from part1 import get_dict_blobs

TOTAL_SIZE = 70000000
REQUIRED_SIZE = 30000000


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_blobs = get_dict_blobs(lines)

    curr_size = dict_blobs["/home"].size
    good_sizes = []
    for _, v in dict_blobs.items():
        if v.type == "d":
            new_size = curr_size - v.size
            if TOTAL_SIZE - new_size >= REQUIRED_SIZE:
                good_sizes.append(v.size)

    return min(good_sizes)



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 24933642


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
