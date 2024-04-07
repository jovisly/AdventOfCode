# Problem type:
# ~~~~~~~~~~~~ string parsing ~~~~~~~~~~~~
# At a glance I thought this one is like 2015 Day 19 which really scared me! But
# it's not like that one at all, fortunately.
filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
chain = lines[0]


def is_cancel(a, b):
    if a != b and a.lower() == b.lower():
        return True
    else:
        return False


def do_reaction(input_str):
    canceled_chars = []
    for i in range(1, len(input_str)):
        j = i - 1
        if is_cancel(input_str[j], input_str[i]) == True:
            # Only add them if they are not already in the list.
            if i not in canceled_chars and j not in canceled_chars:
                canceled_chars += [j, i]

    output_str = "".join([c for i, c in enumerate(list(input_str)) if i not in canceled_chars])
    return output_str

# For testing.
# chain = "dabAcCaCBAcCcaDA"
while True:
    l_prev = len(chain)
    chain = do_reaction(chain)
    l_next = len(chain)
    if l_prev == l_next:
        break

print("Part 1:", len(chain))


# First we need to get unique parts.
parts = set([c.lower() for c in list(chain)])


def get_reacted_length(chain):
    while True:
        l_prev = len(chain)
        chain = do_reaction(chain)
        l_next = len(chain)
        if l_prev == l_next:
            return len(chain)

min_l = len(chain)
for p in parts:
    new_chain = chain.replace(p.lower(), "").replace(p.upper(), "")
    l = get_reacted_length(new_chain)
    if l < min_l:
        min_l = l

print("Part 2:", min_l)
