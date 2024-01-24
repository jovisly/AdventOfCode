"""
Reflections: This took me a bit more than an hour. The most difficult part is
splitting an integer into n pieces.
"""
def parse_line(line):
    es = line.split(" ")
    cap = int(es[2][:-1])
    dur = int(es[4][:-1])
    fla = int(es[6][:-1])
    tex = int(es[8][:-1])
    cal = int(es[10])
    return {"cap": cap, "dur": dur, "fla": fla, "tex": tex, "cal": cal}


def get_score(list_ingredients, amounts, cal_limit=None):
    dict_ing = {k: 0 for k in list_ingredients[0].keys() if k != "cal"}
    total_cal = 0
    for ingredient, amount in zip(list_ingredients, amounts):
        for k, v in ingredient.items():
            if k != "cal":
                dict_ing[k] += amount * v
            else:
                total_cal += amount * v

    vals = list(dict_ing.values())
    vals = [v if v > 0 else 0 for v in vals]
    mult = 1
    for v in vals:
        mult *= v

    if cal_limit is not None:
        if total_cal != cal_limit:
            return 0
        else:
            return mult
    else:
        return mult


# This is the most difficult part of the problem...
def split_int(total, n_pieces):
    queue = [(t, ) for t in range(0, total + 1)]
    results = []
    while len(queue) > 0:
        curr = queue.pop(0)
        num_pieces = len(curr)
        if num_pieces == n_pieces:
            results.append(curr)
        else:
            available = total - sum(curr)
            # If we only one piece left, then no choice, use all of it.
            if num_pieces == n_pieces - 1:
                queue.append(curr + (available, ))
            else:
                # Otherwise, we can continue to try to split.
                for t in range(0, available + 1):
                    queue.append(curr + (t, ))

    return results


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    list_ingredients = [parse_line(line) for line in lines]

    all_possible_amounts = split_int(100, len(list_ingredients))
    max_score = 0
    for amounts in all_possible_amounts:
        score = get_score(list_ingredients, amounts)
        if score > max_score:
            max_score = score
    print("Part 1:", max_score)


    max_score = 0
    for amounts in all_possible_amounts:
        score = get_score(list_ingredients, amounts, cal_limit=500)
        if score > max_score:
            max_score = score
    print("Part 2:", max_score)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)



