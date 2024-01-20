def has_three_vowels(input):
    vowels = "aeiou"
    count = 0
    for c in input:
        if c in vowels:
            count += 1
    return count >= 3


def has_two_in_a_row(input):
    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
            return True
    return False


def has_no_excluded_pairs(input):
    excluded_pairs = ["ab", "cd", "pq", "xy"]
    for pair in excluded_pairs:
        if pair in input:
            return False
    return True


def all_conditions(input):
    return has_three_vowels(input) and has_two_in_a_row(input) and has_no_excluded_pairs(input)


def has_sandwich(input):
    for i in range(len(input) - 2):
        if input[i] == input[i + 2]:
            return True
    return False


def has_double_pair(input):
    for i in range(len(input) - 1):
        pair = input[i:i + 2]
        if pair in input[i + 2:]:
            return True
    return False


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    num = len([
        line for line in lines if all_conditions(line)
    ])
    print("Part 1:", num)

    num = len([
        line for line in lines if has_sandwich(line) and has_double_pair(line)
    ])
    print("Part 2:", num)

    return 0




if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)
