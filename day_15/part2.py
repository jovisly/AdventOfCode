from part1 import get_hash


def handle_equal(input, dict_boxes):
    items = input.split("=")
    label = get_hash(items[0])
    focal_length = items[1]

    # Is there any item in the box with label.
    if len(dict_boxes[label]) == 0:
        dict_boxes[label].append(f"{items[0]} {focal_length}")
    else:
        # Is there already an item with the same label?
        num_same_label = len([
            item for item in dict_boxes[label]
            if item.startswith(items[0])
        ])

        if num_same_label == 0:
            dict_boxes[label].append(f"{items[0]} {focal_length}")
        else:
            new_items = [
                item
                if not item.startswith(items[0]) else f"{items[0]} {focal_length}"
                for item in dict_boxes[label]
            ]
            dict_boxes[label] = new_items



def handle_dash(input, dict_boxes):
    items = input.split("-")
    label = get_hash(items[0])
    if len(dict_boxes[label]) != 0:
        # Remove an item if it has that label.
        new_items = [item for item in dict_boxes[label] if not item.startswith(items[0])]
        dict_boxes[label] = new_items
    else:
        pass



def handle_both(input, dict_boxes):
    if "=" in input:
        handle_equal(input, dict_boxes)
    else:
        handle_dash(input, dict_boxes)


def get_score(dict_boxes):
    total = 0
    for label, content in dict_boxes.items():
        for ind, c in enumerate(content):
            focal_length = int(c.split(" ")[1])
            total += (label + 1) * (ind + 1) * int(focal_length)
    return total



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    segs = lines[0].split(",")
    dict_boxes = {num: [] for num in range(256)}

    for seg in segs:
        handle_both(seg, dict_boxes)

    return get_score(dict_boxes)


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 145


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
