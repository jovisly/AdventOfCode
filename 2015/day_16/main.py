CONDITIONS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def get_dict_aunts(lines):
    dict_aunts = {}
    for line in lines:
        els = line.split(" ")
        id = int(els[1][:-1])
        els = line.split("Sue " + str(id))[1][2:]
        els = els.split(", ")
        dict_aunts[id] = {}
        for e in els:
            name = e.split(": ")[0]
            q = int(e.split(": ")[1])
            dict_aunts[id][name] = q
    return dict_aunts



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_aunts = get_dict_aunts(lines)

    sat_id = None
    for id, dict_cond in dict_aunts.items():
        list_conditions = list(dict_cond)
        sat = True
        for c in list_conditions:
            if c in CONDITIONS:
                correct_val = CONDITIONS[c]
                if dict_cond[c] != correct_val:
                    sat = False

        if sat == True and sat_id is None:
            sat_id = id
        elif sat == True and sat_id is not None:
            print("WARNING: MULTIPLE ID SATISFIES...")

    print("Part 1:", sat_id)

    # Part 2
    sat_id = None
    for id, dict_cond in dict_aunts.items():
        list_conditions = list(dict_cond)
        sat = True
        for c in list_conditions:
            if c in CONDITIONS:
                correct_val = CONDITIONS[c]
                if c == "cats" or c == "trees":
                    # Directionality of inequality is a bit confusing. I just
                    # tried all four possibilities until I get unique solution,
                    # and as crazy as that sounds, it worked.
                    if dict_cond[c] <= correct_val:
                        sat = False
                elif c == "pomeranians" or c == "goldfish":
                    if dict_cond[c] >= correct_val:
                        sat = False
                else:
                    if dict_cond[c] != correct_val:
                        sat = False

        if sat == True and sat_id is None:
            sat_id = id
        elif sat == True and sat_id is not None:
            print("WARNING: MULTIPLE ID SATISFIES...")

    print("Part 2:", sat_id)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


