import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


def is_aba(str):
    return (str[0] == str[2] and str[0] != str[1]), f"{str[1]}{str[0]}{str[1]}"


def is_ssl(str):
    found = False
    last3 = ""
    in_bracket = False
    rev_for_out_bracket = set()
    rev_for_in_bracket = set()
    for ci in list(str):
        if ci == "[":
            in_bracket = True
            last3 = ""
            continue
        elif ci == "]":
            in_bracket = False
            last3 = ""
            continue

        last3 += ci
        last3 = last3[-3:]
        if len(last3) == 3:
            flag, rev = is_aba(last3)
            if flag == True:
                if in_bracket == True:
                    rev_for_out_bracket.add(rev)
                    if last3 in rev_for_in_bracket:
                        found = True
                else:
                    rev_for_in_bracket.add(rev)
                    if last3 in rev_for_out_bracket:
                        found = True

    # print("rev_for_in_bracket", rev_for_in_bracket)
    # print("rev_for_out_bracket", rev_for_out_bracket)
    return found


assert is_ssl("aba[bab]xyz") == True
assert is_ssl("xyx[xyx]xyx") == False
assert is_ssl("aaa[kek]eke") == True
assert is_ssl("zazbz[bzb]cdb") == True

tot = 0
for line in lines:
    if is_ssl(line):
        tot += 1

print("tot:", tot)
