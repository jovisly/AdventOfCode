filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

nums = lines[0].split("\t")
nums = [int(n) for n in nums]
# nums = [0, 2, 7, 0]

def one_cycle(nums):
    max_num = max(nums)
    ind = nums.index(max_num)

    nums_copy = [n for n in nums]
    nums_copy[ind] = 0
    for i in range(ind + 1, ind + max_num + 1):
        i_mod = i % len(nums)
        nums_copy[i_mod] += 1
    return nums_copy


seen = set()
i = 0
while True:
    i += 1
    nums = one_cycle(nums)
    t_nums = tuple(nums)
    if t_nums in seen:
        print("Part 1:", i)
        break
    else:
        seen.add(t_nums)


# For part 2, let's use a dictionary so we can log its i-value
seen = {}
i = 0
while True:
    i += 1
    nums = one_cycle(nums)
    t_nums = tuple(nums)
    if t_nums in seen:
        print("Part 2:", i - seen[t_nums])
        break
    else:
        seen[t_nums] = i


