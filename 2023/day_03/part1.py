

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


def has_neighboring_symbols(neighboring_line, digits):
    """Returns a boolean for whether there are any symbols next to digits.

    Given a neighboring line, and the digits in the format of (467, 0, 2),
    identify if there is a symbol between the indices 0 and 3.
    """
    list_chars = list(neighboring_line)
    is_char_a_neighboring_symbol = [
        True
        if not char.isdigit() and char != "."
        and index >= digits[1] - 1 and index <= digits[2] + 1
        else False
        for index, char in enumerate(list_chars)
    ]
    return any(is_char_a_neighboring_symbol)


def has_neighboring_symbols_this_line(this_line, digits):
    inds = [digits[1] - 1, digits[2] + 1]
    inds = [ind for ind in inds if ind >= 0 and ind < len(this_line)]
    chars = list(this_line)
    is_symbol = [
        True if not char.isdigit() and char != "." and (ind in inds) else False
        for ind, char in enumerate(chars)
    ]
    return any(is_symbol)


def has_neighboring_symbols_all_lines(neighboring_lines, this_line, digits):
    arr_output = [
        has_neighboring_symbols(l, digits) for l in neighboring_lines
    ]
    return any(arr_output) or has_neighboring_symbols_this_line(this_line, digits)



def get_sum_valid_digits(lines, line_num):
    """Given all the lines, and one of the line, get the valid digits."""
    line =  lines[line_num]
    arr_digits = get_digits(line)

    neighboring_lines_indices = [line_num - 1, line_num + 1]
    # Only accept the valid line numbers.
    neighboring_lines_indices = [l for l in neighboring_lines_indices if l >= 0 and l < len(lines)]
    neighboring_lines = [lines[i] for i in neighboring_lines_indices]

    sum = 0
    for digits in arr_digits:
        is_valid = has_neighboring_symbols_all_lines(
            neighboring_lines, lines[line_num], digits
        )
        if is_valid:
            sum += digits[0]

    return sum


def get_total(filename):
    total = 0
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for index, _ in enumerate(lines):
            total += get_sum_valid_digits(lines, index)
    return total


def mini_test():
    filename = "input-test.txt"
    assert get_total(filename) == 4361

    filename = "input-test2.txt"
    assert get_total(filename) == 7 + 592


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = get_total(filename)

    print(total)
