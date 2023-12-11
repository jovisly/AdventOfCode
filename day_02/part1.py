FILENAME = "input.txt"
DICT_BALLS = {"red": 12, "green": 13, "blue": 14}


def is_possible_one_color(input_string):
    """Format: e.g., '6 red'."""
    arr = input_string.split(" ")
    color = arr[1]
    count = int(arr[0])

    return DICT_BALLS[color] >= count


def is_possible_one_draw(input_string):
    """Format: e.g., '6 red, 1 blue, 3 green'."""
    counts = input_string.split(",")
    counts = [c.strip() for c in counts]
    arr_is_possible = [is_possible_one_color(c) for c in counts]
    return all(arr_is_possible)


def is_possble_one_game(input_string):
    """Format: e.g., '6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'."""
    arr_draws = input_string.split(";")
    arr_draws = [d.strip() for d in arr_draws]
    arr_is_possible = [is_possible_one_draw(d) for d in arr_draws]
    return all(arr_is_possible)


def parse_game(input_string):
    arr = input_string.split(":")
    game_id = int(arr[0][4:])
    is_possible = is_possble_one_game(arr[1])
    if is_possible:
        return game_id
    else:
        return 0


if __name__ == "__main__":
    total = 0
    with open(FILENAME, 'r') as file:
        for line in file:
            total += parse_game(line)

    print(total)

