import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

instructions = lines[0].split(", ")

curr = ((0, 0), "U")
visited = set()
first_location = None
for instruction in instructions:
    dir = instruction[0]
    steps = int(instruction[1:])

    next_pos, curr_dir = curr
    next_dir = utils.turn(curr_dir, dir)

    for _ in range(steps):
        next_pos = utils.move_to_dir(next_pos, next_dir)
        if next_pos in visited and first_location is None:
            first_location = next_pos

        visited.add(next_pos)

    curr = (next_pos, next_dir)


pos, _ = curr
print(sum([abs(p) for p in pos]))
print(sum([abs(p) for p in first_location]))

