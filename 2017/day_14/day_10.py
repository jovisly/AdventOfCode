# ... From Day 10 ...
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

def get_ascii(input_str):
    return [ord(c) for c in list(input_str)] + [17, 31, 73, 47, 23]

def get_hex(arr):
    x = 0
    for a in arr:
        x = x ^ a
    return hex(x)[2:]


def get_bin(d):
    b = format(int(d, 16), "b")
    if len(b) < 4:
        b = "0" * (4 - len(b)) + b

    assert len(b) == 4
    return b


def get_full_seq(input_str):
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
    b = ""
    for a in sub_arrs:
        h = get_hex(a)
        if len(h) == 1:
            h = "0" + h
        for sub_h in list(h):
            b += get_bin(sub_h)

    assert len(b) == 128
    return b
