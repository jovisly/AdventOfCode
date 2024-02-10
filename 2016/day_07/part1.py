import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


def is_abba(str):
    beg = str[:2]
    end = str[-2:]
    return beg[::-1] == end and beg[0] != beg[1]


def is_tls(str):
    has_abba = False
    has_abba_in_brackets = False

    last4 = ""
    in_bracket = False
    for ci in list(str):
        if ci == "[":
            in_bracket = True
            last4 = ""
            continue
        elif ci == "]":
            in_bracket = False
            last4 = ""
            continue

        last4 += ci
        last4 = last4[-4:]
        if len(last4) == 4:
            if is_abba(last4):
                if in_bracket == True:
                    has_abba_in_brackets = True
                else:
                    has_abba = True


    return has_abba == True and has_abba_in_brackets == False


assert is_tls("abba[mnop]qrst") == True
assert is_tls("abcd[bddb]xyyx") == False
assert is_tls("aaaa[qwer]tyui") == False
assert is_tls("ioxxoj[asdfgh]zxcvbn") == True

tot = 0
for line in lines:
    if is_tls(line):
        tot += 1

print("tot:", tot)
