filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]
nums = line.split(",")
nums = [int(n) for n in nums]

nums[1] = 12
nums[2] = 2

op_ind = 0
while True:
    # print("op_ind:", op_ind)
    op = nums[op_ind]
    if op == 1 or op == 2:
        ind1 = nums[op_ind + 1]
        num1 = nums[ind1]
        ind2 = nums[op_ind + 2]
        num2 = nums[ind2]
        if op == 1:
            num3 = num1 + num2
        else:
            num3 = num1 * num2
        ind3 = nums[op_ind + 3]
        nums[ind3] = num3
    elif op == 99:
        break
    else:
        print("SOMETHING IS WRONG:", op)
        break
    op_ind += 4

print("Part 1:",  nums[0])
# 250646 is too low -- turns out there's this line:
# "replace position 1 with the value 12 and replace position 2 with the value 2,"
# which only showed up after all the test cases.

# Reset for part 2 -- we just tried out some numbers and got a pattern.
a = int((19690720 - 250646) / 216000)
b = 19690720 - (a * 216000 + 250646)
print("Part 2:", 100 * a + b)

exit()
print(a, b)

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
line = lines[0]
nums = line.split(",")
nums = [int(n) for n in nums]

# This number x 216000 on the result. 250646 is the min.
nums[1] = 90
# This number simply increments the result
nums[2] = 74

op_ind = 0
while True:
    # print("op_ind:", op_ind)
    op = nums[op_ind]
    if op == 1 or op == 2:
        ind1 = nums[op_ind + 1]
        num1 = nums[ind1]
        ind2 = nums[op_ind + 2]
        num2 = nums[ind2]
        if op == 1:
            num3 = num1 + num2
        else:
            num3 = num1 * num2
        ind3 = nums[op_ind + 3]
        nums[ind3] = num3
    elif op == 99:
        break
    else:
        print("SOMETHING IS WRONG:", op)
        break
    op_ind += 4

print("Part 2:")
print(nums)
