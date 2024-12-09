from tqdm import tqdm

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

line = lines[0]


def expand_line(line):
    index = 0
    expanded_line = []
    # Keep track of the size of each file.
    dict_size = {}
    # Keep track of the spaces available.
    available_spaces = []
    for i in range(len(line)):
        if i % 2 == 0:
            # This is a file.
            size = int(line[i])
            expanded_line += [str(index)] * size
            dict_size[str(index)] = size
            index += 1
        else:
            # This is space.
            size = int(line[i])
            if size > 0:
                expanded_line += ["."] * size
                available_spaces.append(size)

    return expanded_line, dict_size, available_spaces


expanded_line, dict_size, available_spaces = expand_line(line)

# print(expanded_line)
# print(dict_size)
# print(available_spaces)


def get_checksum(line):
    cs = 0
    for i, v in enumerate(line):
        if v != ".":
            d = int(v)
            cs += d * i
    return cs


def collapse_line(blocks, dict_size):
    """Collapse line by moving file IDs to earlier spaces, only if enough continuous space is available."""

    # Create a dictionary of available spaces and their lengths
    free_spaces = {}
    start = None
    length = 0
    for i, b in enumerate(blocks):
        if b == ".":
            if start is None:
                start = i
            length += 1
        elif start is not None:
            free_spaces[start] = length
            start = None
            length = 0
    if start is not None:
        free_spaces[start] = length

    # Process files from right to left
    blocks = list(blocks)  # Make a copy to modify
    processed_files = set()

    for i in tqdm(range(len(blocks) - 1, -1, -1)):
        if blocks[i] == "." or blocks[i] in processed_files:
            continue

        # Count size of current file
        file_id = blocks[i]
        file_size = dict_size[file_id]
        processed_files.add(file_id)

        # Find available spaces before this position
        candidates = [(pos, size) for pos, size in free_spaces.items()
                     if pos < i and size >= file_size]

        if not candidates:
            continue

        # Move to leftmost available space
        target_pos, space_size = min(candidates, key=lambda x: x[0])

        # Move the file
        for j in range(file_size):
            blocks[target_pos + j] = file_id
            blocks[i - j] = "."

        # Update free spaces
        del free_spaces[target_pos]
        if space_size > file_size:
            free_spaces[target_pos + file_size] = space_size - file_size

    return blocks


collapsed_line = collapse_line(expanded_line, dict_size)
# print(collapsed_line)

print("Part 2:", get_checksum(collapsed_line))
