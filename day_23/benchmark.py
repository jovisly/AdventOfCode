"""Benchmark comparisons of some simple operations."""
import copy
import time

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
list_board = [list(l) for l in lines]
dict_board = {(i, j): val for i, row in enumerate(list_board) for j, val in enumerate(row)}


# List lookup.
num_iterations = 200_000
ti = time.time()
for _ in range(num_iterations):
    if list_board[0][1] == "#":
        pass
tf = time.time()
print(f"List lookup: {tf - ti}")

# Dictionary lookup.
ti = time.time()
for _ in range(num_iterations):
    if dict_board[(0, 1)] == "#":
        pass
tf = time.time()
print(f"Dictionary lookup: {tf - ti}")

# Conclusion -- surprisingly no difference between list lookup vs dictionary.



list_positions = list(dict_board)
set_positions = set(list_positions)

num_iterations = 200_000

ti = time.time()
for _ in range(num_iterations):
    if (0, 1) in list_positions:
        pass
tf = time.time()
print(f"List membership check: {tf - ti}")

ti = time.time()
for _ in range(num_iterations):
    if (0, 1) in set_positions:
        pass
tf = time.time()
print(f"Set membership check: {tf - ti}")

# Really!? No difference!? I guess the list/set is not big enough to make a difference.



# Deepcopy.
num_iterations = 1_000
ti = time.time()
for _ in range(num_iterations):
    list_positions_copy = copy.deepcopy(list_positions)
tf = time.time()
print(f"Deep copy a list: {tf - ti}")

ti = time.time()
for _ in range(num_iterations):
    list_positions_copy = [p for p in list_positions]
tf = time.time()
print(f"Manual copy a list: {tf - ti}")

# Wow!!
# Deep copy a list: 42.7985200881958
# Manual copy a list: 0.4460322856903076
