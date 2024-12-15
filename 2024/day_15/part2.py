"""
Reflections: OOOOOFFFFSSSS... Reminds me of the 3D tetris question from last year
which I also really struggled.
"""
from dataclasses import dataclass
import utils

filename = "input.txt"
# filename = "input-test.txt"
# filename = "input-test2.txt"
# filename = "input-test3.txt"
lines = open(filename, encoding="utf-8").read().split("\n\n")
board = lines[0].splitlines()
moves = [m for m in list(lines[1]) if len(m.strip()) > 0]


@dataclass
class Box:
    left: tuple[int, int]
    right: tuple[int, int]

    def contains_pos(self, pos: tuple[int, int]) -> bool:
        return pos in (self.left, self.right)

    def move(self, dir: str) -> None:
        self.left = utils.move_to_dir(self.left, dir)
        self.right = utils.move_to_dir(self.right, dir)



def get_boxes(dict_board) -> list[Box]:
    boxes = []
    processed = set()

    for pos, val in dict_board.items():
        if val == "[" and pos not in processed:
            right_pos = (pos[0], pos[1] + 1)
            assert dict_board[right_pos] == "]"
            boxes.append(Box(left=pos, right=right_pos))
            processed.add(pos)
            processed.add(right_pos)

    return boxes



def expand_board(board):
    all_lines = []
    for line in board:
        new_line = ""
        for char in list(line):
            if char == "#":
                new_line += "##"
            if char == "O":
                new_line += "[]"
            if char == ".":
                new_line += ".."
            if char == "@":
                new_line += "@."
        all_lines.append(new_line)
    return all_lines

board = expand_board(board)
dict_board = utils.get_dict_board(board)

def viz_board(dict_board):
    for i in range(len(board)):
        full_line = ""
        for j in range(len(board[0])):
            full_line += dict_board[(i, j)]
        print(full_line)


viz_board(dict_board)
def get_robot(dict_board):
    for pos, val in dict_board.items():
        if val == "@":
            return pos

def get_dir(move):
    if move == "^":
        dir = "U"
    if move == ">":
        dir = "R"
    if move == "v":
        dir = "D"
    if move == "<":
        dir = "L"
    return dir

def one_move(dict_board, robot_pos, move, boxes: list[Box]):
    dir = get_dir(move)
    next_pos = utils.move_to_dir(robot_pos, dir)
    if next_pos not in dict_board:
        return dict_board

    next_val = dict_board.get(next_pos, None)
    if next_val == "#":
        return dict_board
    if next_val == ".":
        dict_board[next_pos] = "@"
        dict_board[robot_pos] = "."
        return dict_board

    # Handle box pushing
    if next_val in ["[", "]"]:
        boxes_to_move = []
        positions_to_check = [next_pos]
        checked_positions = set()  # Keep track of what we've checked

        while positions_to_check:
            current_pos = positions_to_check.pop(0)
            if current_pos in checked_positions:
                continue
            checked_positions.add(current_pos)

            # Find which box this position belongs to
            for box in boxes:
                if box.contains_pos(current_pos):
                    if box not in boxes_to_move:
                        boxes_to_move.append(box)
                        # Check next positions for both sides of the box
                        next_left = utils.move_to_dir(box.left, dir)
                        next_right = utils.move_to_dir(box.right, dir)

                        # Check both next positions
                        for next_check in [next_left, next_right]:
                            if next_check not in checked_positions:
                                if dict_board[next_check] in ["[", "]"]:
                                    positions_to_check.append(next_check)
                                elif dict_board[next_check] == "#":
                                    return dict_board  # Can't move if any part hits a wall

        # Verify all moves are valid before making any changes
        for box in boxes_to_move:
            next_left = utils.move_to_dir(box.left, dir)
            next_right = utils.move_to_dir(box.right, dir)
            if not all(pos in dict_board for pos in [next_left, next_right]):
                return dict_board  # Can't move off board

        # Move all boxes
        for box in boxes_to_move:
            # Clear old positions
            dict_board[box.left] = "."
            dict_board[box.right] = "."

        # Update all box positions
        for box in boxes_to_move:
            box.move(dir)
            dict_board[box.left] = "["
            dict_board[box.right] = "]"

        # Move robot
        dict_board[next_pos] = "@"
        dict_board[robot_pos] = "."

    return dict_board


def get_coord(pos):
    return 100 * pos[0] +  pos[1]

viz_board(dict_board)

boxes = get_boxes(dict_board)
for move in moves:
    print("\nMove:", move)
    robot_pos = get_robot(dict_board)
    dict_board = one_move(dict_board, robot_pos, move, boxes)
    viz_board(dict_board)


tot = 0
for pos, v in dict_board.items():
    if v == "[":
        tot += get_coord(pos)



print("Part 2:", tot)

