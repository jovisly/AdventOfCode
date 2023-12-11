import collections

DICT_MAP = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
}


def get_hands_and_bids(lines):
    dict_hands = {}
    for line in lines:
        hand = line.split(" ")[0]
        hand_mapped = "".join([DICT_MAP[h] for h in hand])
        bid = int(line.split(" ")[1])
        dict_hands[hand_mapped] = bid
    return dict_hands



def is_fives(hand):
    return len(set(hand)) == 1


def is_fours(hand):
    return (
        len(set(hand)) == 2
        and max(collections.Counter(list(hand)).values()) == 4
    )


def is_full_house(hand):
    return (
        len(set(hand)) == 2
        and max(collections.Counter(list(hand)).values()) == 3
    )


def is_threes(hand):
    return (
        len(set(hand)) == 3
        and max(collections.Counter(list(hand)).values()) == 3
    )


def is_two_pairs(hand):
    return (
        len(set(hand)) == 3
        and max(collections.Counter(list(hand)).values()) == 2
    )


def is_one_pair(hand):
    return len(set(hand)) == 4



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_hands = get_hands_and_bids(lines)
    arr_hands = list(dict_hands.keys())
    # Split the hands into multiple arrays based on their hand. We have 7 types.
    arr_hands_categorized = [[] for _ in range(7)]
    for hand in arr_hands:
        if is_fives(hand):
            arr_hands_categorized[0].append(hand)
        elif is_fours(hand):
            arr_hands_categorized[1].append(hand)
        elif is_full_house(hand):
            arr_hands_categorized[2].append(hand)
        elif is_threes(hand):
            arr_hands_categorized[3].append(hand)
        elif is_two_pairs(hand):
            arr_hands_categorized[4].append(hand)
        elif is_one_pair(hand):
            arr_hands_categorized[5].append(hand)
        else:
            arr_hands_categorized[6].append(hand)

    # For each category, sort by the hand.
    for i in range(len(arr_hands_categorized)):
        arr_hands_categorized[i] = sorted(arr_hands_categorized[i])

    # Flatten the array of arrays.
    arr_hands_ranked = [
        hand for hand_category in arr_hands_categorized for hand in hand_category
    ]
    # Get total.
    total = 0
    for index, hand in enumerate(arr_hands_ranked):
        rank = len(arr_hands_ranked) - index
        total += dict_hands[hand] * rank

    return total



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 6440


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
