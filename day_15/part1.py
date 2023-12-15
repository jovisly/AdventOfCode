def get_hash(input):
    val = 0
    for char in list(input):
        val += ord(char)
        val = 17 * val
        val = val % 256

    return val



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    segs = lines[0].split(",")
    return sum([get_hash(seg) for seg in segs])


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 1320


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)


