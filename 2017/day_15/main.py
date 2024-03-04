# Problem type:
# ~~~~~~~~~~~~ much forgiving ~~~~~~~~~~~~
# Bruteforce takes about 1 min for part 1. Was expecting part 2 to actually
# require some clever implementation instead of bruteforce, but it's actually
# pretty nice in reducing the number of rounds needed.

from tqdm import tqdm

# For testing
init_a = 65
init_b = 8921
# actual data
init_a = 873
init_b = 583

mul_a = 16807
mul_b = 48271
div = 2147483647

def get_bin(n, length=16):
    b = bin(n)[2:]
    if len(b) < length:
        d = length - len(b)
        b = "0" * length + b
    b = b[-length:]
    assert len(b) == length
    return b


a = init_a
b = init_b
tot = 0
for _ in tqdm(range(40 * 10**6)):
    a = a * mul_a % div
    b = b * mul_b % div
    if get_bin(a) == get_bin(b):
        tot += 1

# Takes about 1 min.
print("Part 1:", tot)

def get_next_val(val, mul, mod, div=div):
    next_val = (val * mul) % div
    while next_val % mod != 0:
        next_val = (next_val * mul) % div
    return next_val

a = init_a
b = init_b
tot = 0
for i in tqdm(range(5 * 10**6)):
    a = get_next_val(a, mul_a, mod=4)
    b = get_next_val(b, mul_b, mod=8)
    # print()
    # print("a", a)
    # print("b", b)
    if get_bin(a) == get_bin(b):
        # print("i", i)
        tot += 1

print("Part 2:", tot)
