def get_digits(input_string):
    """Given one line, identify the digits and their indices.

    Example input: "467..114..", which should return [(467, 0, 2), (114, 5, 7)].
    """
    digits = []
    curr_digit = None
    for i in range(len(input_string)):
        if input_string[i].isdigit() and curr_digit is None:
            curr_digit = (input_string[i], i, i)
        elif input_string[i].isdigit() and curr_digit is not None:
            curr_digit = (curr_digit[0] + input_string[i], curr_digit[1], i)
        else:
            # Reset.
            if curr_digit is not None:
                digits.append((int(curr_digit[0]), curr_digit[1], curr_digit[2]))
                curr_digit = None

    # If we have something, dump it.
    if curr_digit is not None:
        digits.append((int(curr_digit[0]), curr_digit[1], curr_digit[2]))
        curr_digit = None

    return digits


def get_digits_for_all_lines(lines):
    """Returns all lines with digits.

    Return format: A array with digits. E.g., [[(467, 0, 2), (114, 5, 7)], ...]
    """
    arr_digits = []
    for line in lines:
        arr_digits.append(get_digits(line))
    return arr_digits



def get_neighboring_digits_for_star_one_line(line_digits, ind_min, ind_max):
    arr_digits = []
    for digit in line_digits:
        if (digit[2] >= ind_min and digit[1] <= ind_max) or (digit[1] <= ind_max and digit[2] >= ind_min):
            arr_digits.append(digit[0])

    return arr_digits



def get_neighboring_digits_for_star(line_num, star_index, arr_digits):
    """Given star location, identify all the neighboring digits.

    Returns a list of digits if there are two digits, otherwise [0, 0].
    """
    neighboring_digits = []
    # Previous line.
    if line_num > 0:
        neighboring_line_ind = line_num - 1
        neighboring_digits += get_neighboring_digits_for_star_one_line(arr_digits[neighboring_line_ind], star_index - 1, star_index + 1)

    # Next line.
    if line_num < len(arr_digits) - 1:
        neighboring_line_ind = line_num + 1
        neighboring_digits += get_neighboring_digits_for_star_one_line(arr_digits[neighboring_line_ind], star_index - 1, star_index + 1)

    # This line.
    neighboring_digits += get_neighboring_digits_for_star_one_line(arr_digits[line_num], star_index - 1, star_index - 1)
    neighboring_digits += get_neighboring_digits_for_star_one_line(arr_digits[line_num], star_index + 1, star_index + 1)

    if len(neighboring_digits) == 2:
        return neighboring_digits
    else:
        return [0, 0]



def get_sum_gear_ratio(filename):
    total = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        arr_digits = get_digits_for_all_lines(lines)

        for line_num, line in enumerate(lines):
            chars = list(line)
            ind_stars = [ind for ind, c in enumerate(chars) if c == "*"]
            for ind in ind_stars:
                neighbors = get_neighboring_digits_for_star(line_num, ind, arr_digits)
                total += neighbors[0] * neighbors[1]

    return total



def mini_test():
    filename = "input-test.txt"
    assert get_sum_gear_ratio(filename) == 467835



if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = get_sum_gear_ratio(filename)
    print(total)
