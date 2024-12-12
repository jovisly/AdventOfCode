def map_dir(dir):
    if dir == "R":
        return (0, 1)
    elif dir == "L":
        return (0, -1)
    elif dir == "U":
        return (-1, 0)
    elif dir == "D":
        return (1, 0)
    else:
        raise ValueError(f"Unknown direction: {dir}")

DIRS4 = ["R", "L", "U", "D"]
DIRS8 = ["S", "W", "N", "E", "NE", "NW", "SE", "SW"]

def map_dir_8(dir):
    if dir == "E":
        return (0, 1)
    elif dir == "W":
        return (0, -1)
    elif dir == "N":
        return (-1, 0)
    elif dir == "S":
        return (1, 0)
    elif dir == "NE":
        return (-1, 1)
    elif dir == "NW":
        return (-1, -1)
    elif dir == "SE":
        return (1, 1)
    elif dir == "SW":
        return (1, -1)
    else:
        raise ValueError(f"Unknown direction: {dir}")


def move_to_dir(pos, dir, num_dirs=4):
    if num_dirs == 4:
        mapped_dir = map_dir(dir)
    elif num_dirs == 8:
        mapped_dir = map_dir_8(dir)
    else:
        raise ValueError(f"Unknown number of directions: {num_dirs}")

    return (pos[0] + mapped_dir[0], pos[1] + mapped_dir[1])


def get_neighbors(pos, num_dirs=4):
    if num_dirs == 4:
        return [move_to_dir(pos, d, num_dirs=4) for d in DIRS4]
    if num_dirs == 8:
        return [move_to_dir(pos, d, num_dirs=8) for d in DIRS8]

    raise ValueError(f"Unknown number of directions: {num_dirs}")


def turn(orig_dir, turn_dir):
    if turn_dir == "R":
        if orig_dir == "R":
            next_dir = "D"
        elif orig_dir == "D":
            next_dir = "L"
        elif orig_dir == "L":
            next_dir = "U"
        elif orig_dir == "U":
            next_dir = "R"
        else:
            raise ValueError(f"Unknown direction: {orig_dir}")
    elif turn_dir == "L":
        if orig_dir == "R":
            next_dir = "U"
        elif orig_dir == "D":
            next_dir = "R"
        elif orig_dir == "L":
            next_dir = "D"
        elif orig_dir == "U":
            next_dir = "L"
        else:
            raise ValueError(f"Unknown direction: {orig_dir}")
    else:
        raise ValueError(f"Unknown turn: {turn_dir}")
    return next_dir


def get_dict_board(board):
    dict_board = {
        (i, j): val for i, row in enumerate(board)
        for j, val in enumerate(row)
    }
    return dict_board



def get_blocks(dict_board, value):
    """Find all continuous blocks of a given position value."""
    positions = {pos for pos, val in dict_board.items() if val == value}
    blocks = []

    while positions:
        start = positions.pop()
        block = {start}
        to_visit = {start}

        while to_visit:
            pos = to_visit.pop()
            neighbors = get_neighbors(pos, num_dirs=4)
            for neighbor in neighbors:
                if neighbor in positions and neighbor not in block:
                    block.add(neighbor)
                    to_visit.add(neighbor)
                    positions.remove(neighbor)

        blocks.append(block)

    return blocks


def get_area(block):
    """Calculate area of a block."""
    return len(block)


def get_perimeter(block):
    """Calculate perimeter of a block.

    Each block has 4 sides, meaning 4 unit of perimeter. So each neighbor within
    the block reduces the perimeter by 1. So we check all four possible neighbors.
    """
    perimeter = 0
    for pos in block:
        neighbors = get_neighbors(pos, num_dirs=4)
        for neighbor in neighbors:
            if neighbor not in block:
                perimeter += 1
    return perimeter


def get_num_sides(block):
    """Calculate number of sides of a block.

    A side is a group of connected edge cells having the same "normal" direction.
    """
    # Find cells that are on the edge of the block, i.e., they are missing any neightbor.
    # Track also which neighbor they are missing.
    # "dir" here is not strictly the normal direction but as long as we are consistent
    # it should be fine.
    # Note, one position can show up multiple times in edge_cells_with_directions.
    # And the length of edge_cells_with_directions is in fact the perimeter of the block.
    edge_cells_with_directions = set()
    for pos in block:
        for dir in DIRS4:
            neighbor = move_to_dir(pos, dir)
            if neighbor not in block:
                edge_cells_with_directions.add((pos, dir))

    # For science!
    assert len(edge_cells_with_directions) == get_perimeter(block)

    # Now we count the number of sides by looking at each edge_cells_with_directions,
    # and count the number of "connected" edges facing the same direction.
    sides = 0
    visited_edges = set()
    for pos, dir in edge_cells_with_directions:
        if (pos, dir) not in visited_edges:
            sides += 1
            to_visit = [(pos, dir)]
            while to_visit:
                current, current_dir = to_visit.pop()
                if (current, current_dir) in visited_edges:
                    continue
                visited_edges.add((current, current_dir))
                for neighbor in get_neighbors(current):
                    if neighbor in block:
                        if ((neighbor, current_dir) in edge_cells_with_directions and
                            (neighbor, current_dir) not in visited_edges):
                            to_visit.append((neighbor, current_dir))

    return sides
