"""
Time: ~15 minutes

Reflections: For part 1, it was helpful to ignore the JSON / dictionary aspect
of the input string and just do regular expression to extract and sum the numbers.
Part 2 reminds me a lot of recursively parsing SQL queries (e.g., the logical
operators). I don't think my solution is too elegant but glad it got the right
answer.
"""
import re
from ast import literal_eval


def extract_numbers(string):
    pattern = r'(-?\d+)'
    numbers = re.findall(pattern, string)
    return [int(num) for num in numbers]



def has_red_value(input_dict):
    if "red" in input_dict.values():
        return True
    else:
        return False


def remove_red_objects(data):
    if isinstance(data, dict):
        if has_red_value(data):
            data = {}
        else:
            data = {
                key: remove_red_objects(value) for key, value in data.items()
                if value != "red"
            }
    elif isinstance(data, list):
        data = [remove_red_objects(item) for item in data]
    return data


def solve(filename):
    line = open(filename, encoding="utf-8").read().splitlines()[0]
    nums = extract_numbers(line)
    print("Part 1:", sum(nums))

    orig = literal_eval(line)
    new = remove_red_objects(orig)
    # Turn into string.
    new = str(new)
    nums = extract_numbers(new)
    print("Part 2:", sum(nums))



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


