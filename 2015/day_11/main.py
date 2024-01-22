"""
Time: 30 minutes.

Reflections: Quite a tedious one that requires constructing several conditions,
and also the base-26 calculation (helpful exercise though).
"""
MIN_CHAR = ord("a")
MAX_CHAR = ord("z")
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def no_confusing_letters(input):
    if "i" in input or "o" in input or "l" in input:
        return False
    return True


def has_two_pairs(input):
    l1 = input[1:]
    l2 = input[:-1]
    set_matches = set()
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            set_matches.add(l1[i])

    if len(set_matches) >= 2:
        return True
    return False


def has_straight(input):
    ords = [ord(c) for c in input]
    for i, o in enumerate(ords):
        if i <= 1:
            continue
        if ords[i - 1] == o - 1 and ords[i - 2] == o - 2:
            return True
    return False


def get_next_password(input):
    num = sum([26 ** i * (ALPHABET.index(c) + 1) for i, c in enumerate(input[::-1])])
    num += 1
    result = ''
    while num > 0:
        num, remainder = divmod(num - 1, 26)
        result = ALPHABET[remainder] + result
    return result


def mini_tests():
    assert has_two_pairs("aabb") == True
    assert has_two_pairs("aaa") == False
    assert has_two_pairs("aaaa") == False
    assert has_straight("zzabcde") == True
    assert has_straight("zzabade") == False


def solve(input):
    found = False
    next_password = input
    while found == False:
        next_password = get_next_password(next_password)
        if no_confusing_letters(next_password) and has_two_pairs(next_password) and has_straight(next_password):
            found = True

    print("Part 1:", next_password)

    found = False
    while found == False:
        next_password = get_next_password(next_password)
        if no_confusing_letters(next_password) and has_two_pairs(next_password) and has_straight(next_password):
            found = True

    print("Part 2:", next_password)



if __name__ == "__main__":
    mini_tests()

    input = "hxbxwxba"
    solve(input)


