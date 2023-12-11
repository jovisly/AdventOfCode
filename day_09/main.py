def get_sum_last_ints(list_ints):
    this_list = list(list_ints)
    sum_last_ints = list_ints[-1]
    while not all([n == 0 for n in this_list]):
        new_list = []
        for i in range(len(this_list) - 1):
            new_list.append(this_list[i + 1] - this_list[i])

        this_list = list(new_list)
        sum_last_ints += this_list[-1]

    return sum_last_ints



def solve1(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    list_list_ints = [[int(n) for n in line.split()] for line in lines]
    list_sum_last_ints = [
        get_sum_last_ints(list_ints) for list_ints in list_list_ints
    ]

    return sum(list_sum_last_ints)


def solve2(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    list_list_ints = [[int(n) for n in line.split()] for line in lines]
    # For every list, revert its order.
    list_list_ints = [list(reversed(list_ints)) for list_ints in list_list_ints]
    list_sum_last_ints = [
        get_sum_last_ints(list_ints) for list_ints in list_list_ints
    ]

    return sum(list_sum_last_ints)



def mini_test():
    filename = "input-test.txt"
    assert solve1(filename) == 114
    assert solve2(filename) == 2


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve1(filename)
    print(total)

    total = solve2(filename)
    print(total)



