from collections import defaultdict
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
# print(lines)

# Simple dictionary structure instead of classes. Key:value pair is bot id and
# bot. Each bot corresponds to an array of items.
dict_bots = defaultdict(list)
# We probably don't need this yet for part 1.
dict_outputs = {}

# Process just the value.
for line in lines:
    if line.startswith("value"):
        v = int(line.split(" ")[1])
        b = int(line.split(" ")[-1])
        dict_bots[b].append(v)

# print(dict_bots)
# One bot would need to have two items.

bot_with_2 = [k for k, v in dict_bots.items() if len(v) == 2]
assert len(bot_with_2) == 1
bot_with_2 = bot_with_2[0]
print("bot_with_2:", bot_with_2)

# Process the "bot xxx gives low to bot..." lines.
dict_routing = {}
for line in lines:
    if line.startswith("bot"):
        b = int(line.split(" ")[1])
        low_to = int(line.split(" ")[6])
        high_to = int(line.split(" ")[-1])
        dict_routing[b] = {"h": high_to, "l": low_to}

# Start with the bot with two items and propagate.
queue = [bot_with_2]
while True:
    bot = queue.pop()
    high_to = dict_routing[bot]["h"]
    low_to = dict_routing[bot]["l"]
    high = max(dict_bots[bot])
    low = min(dict_bots[bot])
    dict_bots[bot] = []
    dict_bots[high_to].append(high)
    dict_bots[low_to].append(low)

    # Check if any bots have both 17 and 61.
    for k, v in dict_bots.items():
        if 17 in v and 61 in v:
            print("FOUND:", k)
            exit()

    # Add more queues. Let's say this might not be only one but we really would
    # like it to since we are not taking care of ordering.
    bot_with_2 = [k for k, v in dict_bots.items() if len(v) == 2]
    if len(bot_with_2) > 1:
        print("WARING: multiple bots with more than 2", bot_with_2)
    queue = queue + bot_with_2
    # Ok we do have multiple bots with more than 2 but seems like ordering
    # doesn't matter in the design of the data.
