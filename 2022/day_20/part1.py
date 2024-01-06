"""
Time: about an hour and a half.

Reflections: This took me a lot longer than I would've liked. I was plagued by
off-by-one errors and index update issues. Not having pen and paper around while
working on this was difficult. After staring in space for an hour, I finally
found a piece of receipt paper on which to doodle, and that helped me to
figure it out in a few minutes... Important lesson.
"""

def update_dict(dict_nums, key, original_index, new_index):
    if original_index == new_index:
        return dict_nums

    for k, v in dict_nums.items():
        if k == key:
            dict_nums[k] = new_index
        # Who needs to be moved? Those effected are the ones between original
        # index and new index. But we don't know which number is bigger, so we
        # check both cases.
        elif new_index < original_index and new_index <= v < original_index:
            # The number is being moved down, so numbers inbetween move up.
            dict_nums[k] += 1
        elif original_index < new_index and original_index < v <= new_index:
            # The number is being moved up, so numbers inbetween move down.
            dict_nums[k] -= 1

    return dict_nums


def mix_numbers(nums, dict_nums):
    for i, n in enumerate(nums):
        original_index = dict_nums[(n, i)]
        new_index = (original_index + n) % (len(nums) - 1)
        if new_index == 0:
            new_index = len(nums) - 1
        dict_nums = update_dict(dict_nums, (n, i), original_index, new_index)

        # Sort dict_nums on their values. For debugging.
        # dict_reverse = {v: k for k, v in dict_nums.items()}
        # new_list = [dict_reverse[i][0] for i in range(len(nums))]
        # print(new_list)

    return dict_nums



def get_dict_nums(nums):
    dict_nums = {}
    for i, n in enumerate(nums):
        # Need to be keyed on value and original index because values are not
        # unique.
        dict_nums[(n, i)] = i
        if n == 0:
            zero_ind = i

    return dict_nums, (0, zero_ind)


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    nums = [int(line) for line in lines]
    assert nums.count(0) == 1

    dict_nums, key_zero = get_dict_nums(nums)
    # Update dict_nums with the mixing steps.
    dict_nums = mix_numbers(nums, dict_nums)
    ind_zero = dict_nums[key_zero]

    i1 = (ind_zero + 1000) % len(nums)
    i2 = (ind_zero + 2000) % len(nums)
    i3 = (ind_zero + 3000) % len(nums)

    v = [k[0] for k, v in dict_nums.items() if v in [i1, i2, i3] ]
    return sum(v)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 3


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
