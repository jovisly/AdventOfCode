"""
Bug report: The whole "move cars in order" thing really caught me off guard. But at
least Part 2 was a simple extension to Part 1.
"""
from collections import Counter

import utils

filename = "input.txt"
# filename = "input-test.txt"
# filename = "input-test2.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


class Car:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
        self.num_intersections = 0

    def encounter_intersection(self):
        self.num_intersections += 1
        if self.num_intersections % 3 == 1:
            # Turn left.
            self.dir = utils.turn(self.dir, "L")
        elif self.num_intersections % 3 == 0:
            # Turn right.
            self.dir = utils.turn(self.dir, "R")

    def encounter_corner(self, corner_value):
        if corner_value == "\\":
            if self.dir == "U":
                self.dir = "L"
            elif self.dir == "D":
                self.dir = "R"
            elif self.dir == "R":
                self.dir = "D"
            elif self.dir == "L":
                self.dir = "U"
        elif corner_value == "/":
            if self.dir == "U":
                self.dir = "R"
            elif self.dir == "D":
                self.dir = "L"
            elif self.dir == "R":
                self.dir = "U"
            elif self.dir == "L":
                self.dir = "D"


dict_board = utils.get_dict_board(lines)

dict_board_cleaned = {}
cars = []
for pos, val in dict_board.items():
    if val in ["<", ">"]:
        cars.append(Car(pos, "R" if val == ">" else "L"))
        dict_board_cleaned[pos] = "-"
    elif val in ["^", "v"]:
        cars.append(Car(pos, "U" if val == "^" else "D"))
        dict_board_cleaned[pos] = "|"
    else:
        dict_board_cleaned[pos] = val


def viz_board(dict_board, cars):
    max_x = max([p[0] for p in dict_board.keys()])
    max_y = max([p[1] for p in dict_board.keys()])

    for i in range(max_x + 1):
        full_line = ""
        for j in range(max_y + 1):
            cars_here = [car for car in cars if car.pos == (i, j)]
            if len(cars_here) > 1:
                full_line += "X"
            elif len(cars_here) == 1:
                full_line += cars_here[0].dir
            elif (i, j) in dict_board:
                full_line += dict_board[(i, j)]
        print(full_line)



iter_num = 0
has_crashed = False
while True and not has_crashed:
    print(f"\nIteration {iter_num}")
    # viz_board(dict_board_cleaned, cars)
    cars.sort(key=lambda car: (car.pos[0], car.pos[1]))
    for car in cars:
        curr_pos, curr_dir = car.pos, car.dir
        next_pos = utils.move_to_dir(curr_pos, curr_dir)
        next_val = dict_board_cleaned[next_pos]
        if next_val == "+":
            car.encounter_intersection()
        elif next_val in ["\\", "/"]:
            car.encounter_corner(next_val)
        car.pos = next_pos

        # Check for crash.
        car_positions = [c.pos for c in cars]
        position_counts = Counter(car_positions)
        for pos, count in position_counts.items():
            if count > 1:
                print(f"Part 1: Crash at {pos[1]},{pos[0]}")
                has_crashed = True
                break
        if has_crashed:
            break

    iter_num += 1


# Part 2 -- remove cars that crashed. First reset all the cars.
dict_board = utils.get_dict_board(lines)
dict_board_cleaned = {}
cars = []
for pos, val in dict_board.items():
    if val in ["<", ">"]:
        cars.append(Car(pos, "R" if val == ">" else "L"))
        dict_board_cleaned[pos] = "-"
    elif val in ["^", "v"]:
        cars.append(Car(pos, "U" if val == "^" else "D"))
        dict_board_cleaned[pos] = "|"
    else:
        dict_board_cleaned[pos] = val




iter_num = 0
while len(cars) > 1:
    print(f"\nIteration {iter_num}")
    # viz_board(dict_board_cleaned, cars)
    cars.sort(key=lambda car: (car.pos[0], car.pos[1]))
    for car in cars:
        curr_pos, curr_dir = car.pos, car.dir
        next_pos = utils.move_to_dir(curr_pos, curr_dir)
        next_val = dict_board_cleaned[next_pos]
        if next_val == "+":
            car.encounter_intersection()
        elif next_val in ["\\", "/"]:
            car.encounter_corner(next_val)
        car.pos = next_pos

        # Check for crash.
        car_positions = [c.pos for c in cars]
        position_counts = Counter(car_positions)
        for pos, count in position_counts.items():
            if count > 1:
                # Remove crashed cars.
                cars = [c for c in cars if c.pos != pos]

    iter_num += 1


print(f"Part 2: {cars[0].pos[1]},{cars[0].pos[0]}")
