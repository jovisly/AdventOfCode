def parse_card(line):
    """Parse one line to get two lists: winning numbers and actual numbers."""
    str_numbers = line.split(":")[1]
    arr_numbers = str_numbers.split("|")
    # Clean up white space and linebreaks.
    arr_numbers = [n.strip() for n in arr_numbers]
    winning_numbers = arr_numbers[0].split(" ")
    my_numbers = arr_numbers[1].split(" ")

    # Clean up numbers and return as int.
    winning_numbers = [int(n.strip()) for n in winning_numbers if n.strip() != ""]
    my_numbers = [int(n.strip()) for n in my_numbers if n.strip() != ""]

    # Let's also get card number.
    card_num = int(line.split(":")[0].split(" ")[-1].strip())
    return card_num, winning_numbers, my_numbers


def get_cards_won(dict_parsed_cards, card_num):
    my_numbers = dict_parsed_cards[card_num][1]
    winning_numbers = dict_parsed_cards[card_num][0]
    num = 0
    for n in my_numbers:
        if n in winning_numbers:
            num += 1

    # This returns an answer that was incorrect.
    # return [card_num + i + 1 for i in range(num) if card_num + i + 1 < len(dict_parsed_cards)]
    return [card_num + i + 1 for i in range(num)]



def get_dict_parsed_cards(lines):
    """Returns a dictionary for each parsed cards."""
    dict_parsed_cards = {}
    for line in lines:
        card_num, winning_numbers, my_numbers = parse_card(line)
        dict_parsed_cards[card_num] = (winning_numbers, my_numbers)
    return dict_parsed_cards



def get_dict_won_cards(dict_parsed_cards):
    """Returns a dictionary for the cards won by each cards.

    Returns: e.g., {1: [2, 3, 4, 5], 2: [3, 4], ...}
    """
    dict_won_cards = {}
    for card_num in dict_parsed_cards.keys():
        dict_won_cards[card_num] = get_cards_won(dict_parsed_cards, card_num)
    return dict_won_cards


def get_dict_generator(dict_won_cards):
    """Returns a dictionary that specifies the cards that can generate each card.

    Returns: e.g., {1: [], 2: [1], 3: [1, 2], 4: [1, 2, 3], 5: [1, 3, 4], 6: []}
    """
    dict_generators = {}
    for card_num in list(dict_won_cards):
        dict_generators[card_num] = []
        for k, cards in dict_won_cards.items():
            if card_num in cards:
                dict_generators[card_num].append(k)

    return dict_generators


def get_dict_instances(dict_generators):
    """Returns a dictionary specifying how many cards are won.

    Returns, e.g., {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}
    """
    dict_instances = {}
    for card_num, cards in dict_generators.items():
        dict_instances[card_num] = 1
        for c in cards:
            dict_instances[card_num] += dict_instances[c]

    return dict_instances



def get_total_num_cards(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    dict_parsed_cards = get_dict_parsed_cards(lines)
    dict_won_cards = get_dict_won_cards(dict_parsed_cards)
    dict_generators = get_dict_generator(dict_won_cards)
    dict_instances = get_dict_instances(dict_generators)

    return sum(dict_instances.values())


def mini_test():
    filename = "input-test.txt"
    assert get_total_num_cards(filename) == 30


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = get_total_num_cards(filename)
    print(total)
