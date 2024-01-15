def parse_card(line):
    """Parse one line to get two lists: winning numbers and actual numbers."""
    str_numbers = line.split(":")[1]
    arr_numbers = str_numbers.split("|")
    # Clean up white space and linebreaks.
    arr_numbers = [n.strip() for n in arr_numbers]
    winning_numbers = arr_numbers[0].split(" ")
    my_numbers = arr_numbers[1].split(" ")

    # Clean up numbers and return as int.
    winning_numbers = [int(n.strip()) for n in winning_numbers if n.strip() != ""]
    my_numbers = [int(n.strip()) for n in my_numbers if n.strip() != ""]

    return winning_numbers, my_numbers


def get_points(winning_numbers, my_numbers):
    num = 0
    for n in my_numbers:
        if n in winning_numbers:
            num += 1

    if num == 0:
        return 0
    else:
        return 2 ** (num - 1)


def get_total_points(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            winning_numbers, my_numbers = parse_card(line)
            points = get_points(winning_numbers, my_numbers)
            total += points

    return total



def mini_test():
    filename = "input-test.txt"
    assert get_total_points(filename) == 13


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = get_total_points(filename)

    print(total)
