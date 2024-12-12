"""
Bug report: Drawing it out really helps. Updated utils.py to add the following:

* get_area()
* get_perimeter()
* get_num_sides()
"""
from tqdm import tqdm
import utils

filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

board = utils.get_dict_board(lines)

def get_price(dict_board):
    letters = set(dict_board.values())
    price = 0

    for letter in letters:
        blocks = utils.get_blocks(dict_board, letter)
        for block in blocks:
            price += utils.get_perimeter(block) * utils.get_area(block)

    return price



print("Part 1:", get_price(board))

def get_price_part2(board):
    letters = set(board.values())
    price = 0

    for letter in tqdm(letters):
        # print("*" * 40)
        # print("Letter", letter)
        blocks = utils.get_blocks(board, letter)
        for block in blocks:
            num_sides = utils.get_num_sides(block)
            # print(f"Val {letter}: {num_sides} sides")
            price += utils.get_num_sides(block) * utils.get_area(block)

    return price

print("Part 2:", get_price_part2(board))

