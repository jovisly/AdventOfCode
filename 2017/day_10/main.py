# Problem type:
# ~~~~~~~~~~~~ language comprehension (then chore) ~~~~~~~~~~~~

# Test data.
lengths = [3, 4, 1, 5]
size = 5
# Actual data.
lengths = [83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100]
size = 256

def one_op(pos, arr, skip_size, length):
    # print("=" * 30)
    # print(f"pos: {pos}, arr: {arr}, skip_size: {skip_size}, length: {length}")
    arr2 = arr + arr
    seg = arr2[pos:pos + length]
    seg = seg[::-1]
    new_arr = [a for a in arr]

    for i, a in enumerate(seg):
        mod_pos = (i + pos) % len(arr)
        new_arr[mod_pos] = a

    # print("new arr:", new_arr)
    return new_arr


arr = [i for i in range(size)]
skip_size = 0
pos = 0
# print("original arr", arr)
for length in lengths:
    arr = one_op(pos, arr, skip_size, length)
    pos += skip_size + length
    pos = pos % len(arr)
    skip_size += 1

print("Part 1:", arr[0] * arr[1])

# Part 2.
def get_ascii(input_str):
    return [ord(c) for c in list(input_str)] + [17, 31, 73, 47, 23]

def get_hex(arr):
    x = 0
    for a in arr:
        x = x ^ a
    return hex(x)[2:]


input_str = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"
# input_str = ""
# input_str = "AoC 2017"

lengths = get_ascii(input_str)
size = 256

arr = [i for i in range(size)]
skip_size = 0
pos = 0
for _ in range(64):
    for length in lengths:
        arr = one_op(pos, arr, skip_size, length)
        pos += skip_size + length
        pos = pos % len(arr)
        skip_size += 1


sub_arrs = [arr[n:n+16] for n in range(0, len(arr), 16)]
h = ""
for a in sub_arrs:
    h += get_hex(a)

print("Part 2:", h)
