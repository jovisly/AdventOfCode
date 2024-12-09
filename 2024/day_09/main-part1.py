"""
Reflections: Hardest question so far this year. Two days ago, for the operations question,
I was so glad that the test set had an example where the order of operations mattered.
That example was what allowed me to figure out what was wrong with my implementation. So
I thought, wow imagine if the test set doesn't have such example. I don't know how long
then it would've taken me to figure it out.

That scenario played out today, with some extra kick. For a long, long, long time, I
did not realize when file IDs have more than one digit, they should be treated together
during all the moving operations. So I kept having things that work for test set but not
for the actual data.

Then we had some typical Python array optimization problem. Adding a set helped.

For Part 2, there's gotta be a better way, but I just did the really really spelled-out
and tedious method. At least it is a lot faster.
"""
from tqdm import tqdm

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

line = lines[0]

def expand_line(line):
    index = 0
    expanded_line = []
    for i in range(len(line)):
        if i % 2 == 0:
            # This is a file.
            size = int(line[i])
            expanded_line += [str(index)] * size
            index += 1
        else:
            # This is space.
            size = int(line[i])
            expanded_line += ["."] * size

    return expanded_line


expanded_line = expand_line(line)


def collapse_line(blocks):
    """Collapse line by moving file IDs to earlier spaces."""

    # Indicies of spaces so we don't have to search list.
    spaces = set([i for i, b in enumerate(blocks) if b == "."])

    # Process each position from right to left
    for current_pos in tqdm(range(len(blocks) - 1, -1, -1)):
        # Skip if it's a dot
        if blocks[current_pos] == ".":
            continue

        # Found a number, find first available dot before it
        number = blocks[current_pos]
        # Find the first available dot before it
        space_pos = min(spaces)
        if space_pos < current_pos:
            # Move number to this dot position
            blocks[space_pos] = number
            blocks[current_pos] = "."
            spaces.remove(space_pos)
            spaces.add(current_pos)
            continue

    # Remove trailing dots
    while blocks and blocks[-1] == ".":
        blocks.pop()

    return blocks

collapsed_line = collapse_line(expanded_line)


# Then get the checksum.
def get_checksum(line):
    cs = 0
    for i, v in enumerate(line):
        d = int(v)
        cs += d * i
    return cs


checksum = get_checksum(collapsed_line)


print("Part 1:", checksum)

