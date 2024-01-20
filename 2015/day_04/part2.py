import hashlib


def solve(input):
    i = 1
    while True:
        combo = input + str(i)
        hashed = hashlib.md5(combo.encode("utf-8"))
        if hashed.hexdigest().startswith("000000"):
            return i
        i += 1


if __name__ == "__main__":
    input = "ckczppom"
    out = solve(input)
    print(out)
