def map_dir(dir):
    if dir == "R" or dir == "E" or dir == ">":
        return (0, 1)
    elif dir == "L" or dir == "W" or dir == "<":
        return (0, -1)
    elif dir == "U" or dir == "N" or dir == "^":
        return (-1, 0)
    elif dir == "D" or dir == "S" or dir == "v":
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


def viz_board(dict_board):
    max_x = max([p[0] for p in dict_board.keys()])
    max_y = max([p[1] for p in dict_board.keys()])
    for i in range(max_x + 1):
        full_line = ""
        for j in range(max_y + 1):
            full_line += dict_board[(i, j)]
        print(full_line)



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


def find_inside_positions(
    dict_board,
    boundary_char="X",
    empty_char="."
):
    """Find all positions that are inside boundaries.

    Returns:
        Set of (x, y) positions that are inside.
    """
    if not dict_board:
        return set()

    max_x = max([p[0] for p in dict_board.keys()])
    max_y = max([p[1] for p in dict_board.keys()])

    # Start from all edge positions that are empty
    queue = []
    for x in range(max_x + 1):
        if dict_board.get((x, 0)) == empty_char:
            queue.append((x, 0))
        if dict_board.get((x, max_y)) == empty_char:
            queue.append((x, max_y))
    for y in range(max_y + 1):
        if dict_board.get((0, y)) == empty_char:
            queue.append((0, y))
        if dict_board.get((max_x, y)) == empty_char:
            queue.append((max_x, y))

    # BFS to mark all reachable positions as outside
    outside_positions = set()
    visited = set()

    while queue:
        pos = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        outside_positions.add(pos)

        # Check neighbors
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (x + dx, y + dy)
            if (new_pos in dict_board and
                dict_board[new_pos] == empty_char and
                new_pos not in visited):
                queue.append(new_pos)

    # All empty positions that are NOT outside must be inside
    all_empty = {pos for pos, val in dict_board.items() if val == empty_char}
    inside_positions = all_empty - outside_positions

    return inside_positions
