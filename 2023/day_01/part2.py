FILENAME = "input.txt"
DICT_STR_TO_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def find_left_and_right_most_number(input_string):
    ind_l, num_l, ind_r, num_r = 100, None, -100, None

    for k, v in DICT_STR_TO_NUM.items():
        found_ind_str_l = input_string.find(k)
        found_ind_num_l = input_string.find(str(v))

        found_ind_str_r = input_string.rfind(k)
        found_ind_num_r = input_string.rfind(str(v))

        if found_ind_str_l != -1 and found_ind_str_l < ind_l:
            ind_l = found_ind_str_l
            num_l = DICT_STR_TO_NUM[k]

        if found_ind_num_l != -1 and found_ind_num_l < ind_l:
            ind_l = found_ind_num_l
            num_l = v

        if found_ind_str_r != -1 and found_ind_str_r > ind_r:
            ind_r = found_ind_str_r
            num_r = DICT_STR_TO_NUM[k]

        if found_ind_num_r != -1 and found_ind_num_r > ind_r:
            ind_r = found_ind_num_r
            num_r = v

    return (num_l, num_r)



def get_calibration_value(input_string):
    num_l, num_r = find_left_and_right_most_number(input_string)
    return num_l * 10 + num_r


def mini_test():
    assert get_calibration_value("two1nine") == 29
    assert get_calibration_value("eightwothree") == 83
    assert get_calibration_value("abcone2threexyz") == 13
    assert get_calibration_value("xtwone3four") == 24
    assert get_calibration_value("4nineeightseven2") == 42
    assert get_calibration_value("zoneight234") == 14
    assert get_calibration_value("7pqrstsixteen") == 76
    assert get_calibration_value("vgchkqhxrbjnlqnvpml77twonejcv") == 71
    assert get_calibration_value("123fivefivefive") == 15



if __name__ == "__main__":
    mini_test()
    sum_calibration_value = 0
    with open(FILENAME, 'r') as file:
        for line in file:
            sum_calibration_value += get_calibration_value(line)

    print(sum_calibration_value)




