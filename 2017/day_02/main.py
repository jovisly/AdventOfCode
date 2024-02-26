filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

tot = 0
for line in lines:
    nums = line.split(" ")
    nums = line.split("\t")
    nums = [int(n) for n in nums if n]
    tot += max(nums) - min(nums)

print("Part 1:", tot)


def find_division_res(nums):
    for n in nums:
        for m in nums:
            if n != m:
                if n / m == int(n/m):
                    # print(f"n: {n} and m: {m}")
                    return n // m
    raise Exception("No result found:", nums)
    return 0


tot = 0
for line in lines:
    nums = line.split(" ")
    nums = line.split("\t")
    nums = [int(n) for n in nums if n]
    tot += find_division_res(nums)

print("Part 2:", tot)
# 109 is too low.
