FILENAME = "input.txt"


def get_dict_counts(input_string):
    """Format, e.g., '1 red, 2 green, 6 blue'.

    Returns: {'red': 1, 'green': 2, 'blue': 6}
    """
    counts = input_string.split(",")
    counts = [c.strip() for c in counts]

    dict_counts = {}
    for c in counts:
        arr = c.split(" ")
        dict_counts[arr[1]] = int(arr[0])

    return dict_counts



def get_draws(input_string):
    """Format: e.g., '6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'."""
    arr_draws = input_string.split(";")
    arr_draws = [d.strip() for d in arr_draws]
    return [get_dict_counts(draw) for draw in arr_draws]



def get_power(input_string):
    arr = input_string.split(":")
    draws = get_draws(arr[1])

    dict_consolidated = {}
    for draw in draws:
        for color, count in draw.items():
            if color not in dict_consolidated:
                dict_consolidated[color] = count
            elif dict_consolidated[color] < count:
                dict_consolidated[color] = count


    power = 1
    for count in dict_consolidated.values():
        power *= count

    return power


def mini_test():
    input_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert get_power(input_string) == 48

    input_string = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    assert get_power(input_string) == 12

    input_string = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    assert get_power(input_string) == 1560

    input_string = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    assert get_power(input_string) == 630

    input_string = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    assert get_power(input_string) == 36





if __name__ == "__main__":
    mini_test()

    total = 0
    with open(FILENAME, 'r') as file:
        for line in file:
            total += get_power(line)

    print(total)
