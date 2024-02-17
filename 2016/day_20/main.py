MIN = 0
MAX = 9
filename = "input-test.txt"

MIN = 0
MAX = 4294967295
filename = "input.txt"

lines = open(filename, encoding="utf-8").read().splitlines()

list_allowed = [(MIN, MAX)]
# print("list_allowed", list_allowed)

for line in lines:
    lower, upper = line.split("-")
    lower = int(lower)
    upper = int(upper)

    updated_allowed = []
    for allowed in list_allowed:
        this_lower, this_upper = allowed
        # Debugging these conditions took forever...
        if this_lower < lower and this_upper > upper:
            # Condition 6
            # print("flag 6")
            updated_allowed.append((this_lower, lower - 1))
            updated_allowed.append((upper + 1, this_upper))
        elif this_lower >= lower and this_upper <= upper:
            # Condition 5
            # The entire enage is not included so do not append.
            # print("flag 5")
            pass
        elif this_upper < lower and this_lower < lower:
            # Condition 1
            # print("flag 1")
            updated_allowed.append(allowed)
        elif this_upper > upper and this_lower > upper:
            # Condition 2
            # print("flag 2")
            updated_allowed.append(allowed)
        elif this_upper >= lower and this_lower < lower:
            # Condition 3
            # print("flag 3")
            updated_allowed.append((this_lower, lower - 1))
        elif this_lower <= upper and this_upper > upper:
            # Condition 4
            # print("flag 4")
            updated_allowed.append((upper + 1, this_upper))
        else:
            print("Flag x?", allowed, (lower, upper))

    list_allowed = updated_allowed
    # print("list_allowed", list_allowed)

print(list_allowed[0][0])

tot = 0
for allowed in list_allowed:
    lower, upper = allowed
    tot += upper - lower + 1

print(tot)
