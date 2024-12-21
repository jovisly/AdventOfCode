"""
7 8 9
4 5 6
1 2 3
  0 A  bot1 (keypad)

  ^ A
< v >  bot2 (remote)

  ^ A
< v >  bot3 (remote)

  ^ A
< v >  you (remote)
"""

dict_remote = {
    "A": {
        "<": "^",
        "v": ">",
    },
    "^": {
        ">": "A",
        "v": "v",
    },
    "v": {
        "<": "<",
        ">": ">",
        "^": "^",
    },
    ">": {
        "^": "A",
        "<": "v"
    },
    "<": {
        ">": "v"
    }
}

dict_keypad = {
    "A": {
        "^": "3",
        "<": "0"
    },
    "0": {
        "^": "2",
        ">": "A"
    },
    "1": {
        "^": "4",
        ">": "2"
    },
    "2": {
        "^": "5",
        ">": "3",
        "<": "1",
        "v": "0"
    },
    "3": {
        "^": "6",
        "<": "2",
        "v": "A"
    },
    "4": {
        "^": "7",
        ">": "5",
        "v": "1"
    },
    "5": {
        "^": "8",
        ">": "6",
        "<": "4",
        "v": "2"
    },
    "6": {
        "^": "9",
        "<": "5",
        "v": "3",
    },
    "7": {
        ">": "8",
        "v": "4"
    },
    "8": {
        ">": "9",
        "<": "7",
        "v": "5"
    },
    "9": {
        "<": "8",
        "v": "6"
    },
}


dirs = ["<", ">", "v", "^"]


def get_first_solutions(goal, n_solutions=10):
    seen = set()
    # queue: n, buttons, moves, pos - prioritize on pressing buttons.
    queue = [(1, 0, "", "", "A")]
    seen.add(("", "", "A"))
    solutions = []

    while queue and len(solutions) < n_solutions:
        _, n, buttons, moves, pos = heapq.heappop(queue)

        if buttons == goal:
            solutions.append(moves)
            continue
        if len(buttons) > len(goal):
            continue
        # Can also skip if any of the buttons are not the same.
        if buttons != goal[:len(buttons)]:
            continue

        # Try moving in each direction
        for d in dirs:
            if d in dict_keypad[pos]:
                new_pos = dict_keypad[pos][d]
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
    return solutions



def get_second_solutions(goal, n_solutions=10):
    seen = set()
    queue = [(1, 0, "", "", "A")]
    seen.add(("", "", "A"))
    solutions = []

    while queue and len(solutions) < n_solutions:
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

