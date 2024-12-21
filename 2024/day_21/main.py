import heapq
from utils import dict_remote, dict_keypad

filename = "input.txt"
filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

# We should start with the keypad.
goal = "029A"

dirs = ["<", ">", "v", "^"]
# seen = set()
# # queue: n, buttons, moves, pos
# queue = [(0, "", "", "A")]
# seen.add(("", "", "A"))
# solutions = []

# while queue and len(solutions) < 10:
#     n, buttons, moves, pos = heapq.heappop(queue)

#     if buttons == goal:
#         print("Found solution:", buttons, moves)
#         solutions.append(moves)
#         continue
#     if len(buttons) > len(goal):
#         continue
#     # Can also skip if any of the buttons are not the same.
#     if buttons != goal[:len(buttons)]:
#         continue

#     # Try moving in each direction
#     for d in dirs:
#         if d in dict_keypad[pos]:
#             new_pos = dict_keypad[pos][d]
#             new_state = (buttons, moves + d, new_pos)
#             if new_state not in seen:
#                 heapq.heappush(queue, (n + 1, buttons, moves + d, new_pos))

#     # Try pressing the button
#     new_buttons = buttons + pos
#     new_state = (new_buttons, moves + "A", pos)
#     if new_state not in seen:
#         heapq.heappush(queue, (n + 1, new_buttons, moves + "A", pos))

# print(solutions)


goal = "<A^A>^^AvvvA"
seen = set()
queue = [(1, 0, "", "", "A")]
seen.add(("", "", "A"))
solutions = []

while queue and len(solutions) < 5:
    _, n, buttons, moves, pos = heapq.heappop(queue)
    print(n, buttons, moves, pos)

    if buttons == goal:
        print("Found solution:", buttons, moves)
        solutions.append(moves)
        continue
    if len(buttons) > len(goal):
        continue
    # Can also skip if any of the buttons are not the same.
    if buttons != goal[:len(buttons)]:
        continue

    # Try moving in each direction
    for d in dirs:
        if d in dict_remote[pos]:
            new_pos = dict_remote[pos][d]
            new_state = (buttons, moves + d, new_pos)
            if new_state not in seen:
                new_moves = moves + d
                ratio = 1 - new_moves.count('A') / len(new_moves)
                heapq.heappush(queue, (ratio, n + 1, buttons, new_moves, new_pos))

    # Try pressing the button
    new_buttons = buttons + pos
    new_state = (new_buttons, moves + "A", pos)
    if new_state not in seen:
        new_moves = moves + "A"
        ratio = 1 - new_moves.count('A') / len(new_moves)
        heapq.heappush(queue, (ratio, n + 1, new_buttons, new_moves, pos))



print(solutions)









exit()
# this is too slow.
def try_press_button(button, pos1, buttons1, pos2, buttons2, pos3, buttons3):
    new_pos1 = pos1
    new_pos2 = pos2
    new_pos3 = pos3
    new_buttons1 = buttons1
    new_buttons2 = buttons2
    new_buttons3 = buttons3

    try:
        if button == "A":
            new_buttons3 += pos_3
            if pos_3 == "A":
                new_buttons2 += pos_2
                if pos_2 == "A":
                    new_buttons1 += pos_1
                else:
                    new_pos1 = dict_keypad[pos1][pos2]
            else:
                new_pos2 = dict_remote[pos2][pos3]
        else:
            new_pos3 = dict_remote[pos3][button]
        return True, new_pos1, new_buttons1, new_pos2, new_buttons2, new_pos3, new_buttons3
    except:
        # Not a valid move.
        return False, new_pos1, new_buttons1, new_pos2, new_buttons2, new_pos3, new_buttons3

# queue: n, pos1, buttons1, pos2, buttons2, pos3, buttons3, buttons (you)
queue = [
    (1, "A", "", "A","", "A", "", "<"),
    (1, "A", "", "A","", "A", "", ">"),
    (1, "A", "", "A","", "A", "", "v"),
    (1, "A", "", "A","", "A", "", "^")
]

while queue:
    n, pos1, buttons1, pos2, buttons2, pos3, buttons3, buttons = heapq.heappop(queue)
    print("len", len(queue), len(buttons))

    if buttons1 == "029A":
        print(n, buttons)
        break
    if len(buttons1) > len("029A"):
        continue

    # Try to press all buttons.
    for button in ["<", ">", "v", "^", "A"]:
        success, new_pos1, new_buttons1, new_pos2, new_buttons2, new_pos3, new_buttons3 = try_press_button(button, pos1, buttons1, pos2, buttons2, pos3, buttons3)
        if success:
            heapq.heappush(queue, (n + 1, new_pos1, new_buttons1, new_pos2, new_buttons2, new_pos3, new_buttons3, buttons + button))
        # else:
        #     print("Not a valid move:", button)



exit()
buttons_you_str = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
buttons_you = list(buttons_you_str)
buttons_bot3 = ""
buttons_bot2 = ""
buttons_bot1 = ""

pos_bot3 = "A"
pos_bot2 = "A"
pos_bot1 = "A"


for button_you in buttons_you:
    assert button_you in dict_remote
    if button_you == "A":
        buttons_bot3 += pos_bot3

        # This causes pos_bot2 to be updated.
        if pos_bot3 == "A":
            buttons_bot2 += pos_bot2

            if pos_bot2 == "A":
                buttons_bot1 += pos_bot1
            else:
                pos_bot1 = dict_keypad[pos_bot1][pos_bot2]
        else:
            pos_bot2 = dict_remote[pos_bot2][pos_bot3]
    else:
        pos_bot3 = dict_remote[pos_bot3][button_you]



print(buttons_bot3)
print(buttons_bot2)
print(buttons_bot1)

print("Part 1:")



print("Part 2:")
