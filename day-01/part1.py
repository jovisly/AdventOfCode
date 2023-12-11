FILENAME = "input.txt"


def get_calibration_value(input_string):
  """Get the first and last digits of the input string."""
  list_chars = list(input_string)
  digits = [int(char) for char in list_chars if char.isdigit()]
  first = digits[0]
  last = digits[-1]
  return first * 10 + last


if __name__ == "__main__":
  sum_calibration_value = 0
  with open(FILENAME, 'r') as file:
    for line in file:
      sum_calibration_value += get_calibration_value(line)

  print(sum_calibration_value)
