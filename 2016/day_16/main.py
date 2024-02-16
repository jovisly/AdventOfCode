# For testing.
IN = "10000"
L = 20


IN = "11100010111110100"
L = 272
# For part 2
L = 35651584

def get_next(input_str):
    a = input_str
    b = a[::-1]
    b = "".join(["1" if c == "0" else "0" for c in list(b)])
    return a + "0" + b

print(get_next("1"))
print(get_next("0"))
print(get_next("11111"))
print(get_next("111100001010"))
print(get_next("110101"))


def get_checksum(input_str):
    cs = input_str[:L]
    while len(cs) % 2 == 0:
        new_cs = ""
        for i in range(0, len(cs), 2):
            j = i + 1
            c1 = cs[i]
            c2 = cs[j]
            if c1 == c2:
                new_cs += "1"
            else:
                new_cs += "0"
        cs = new_cs
    return cs


print(get_checksum("110010110100"))

s = IN
while True:
    s = get_next(s)
    if len(s) >= L:
        s = get_checksum(s)
        print(s)
        exit()
