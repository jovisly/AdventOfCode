# Similar to part 1 but (a) takes care of outputs, (b) go through all the queue
# then look at the outputs.
from collections import defaultdict
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
# print(lines)

# Simple dictionary structure instead of classes. Key:value pair is bot id and
# bot. Each bot corresponds to an array of items.
dict_bots = defaultdict(list)
dict_outputs = defaultdict(list)

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
        low_to_type = line.split(" ")[5]
        high_to = int(line.split(" ")[-1])
        high_to_type = line.split(" ")[-2]
        dict_routing[b] = {
            "h": high_to, "ht": high_to_type, "l": low_to, "lt": low_to_type
        }


# Start with the bot with two items and propagate.
queue = [bot_with_2]
while len(queue) > 0:

    bot = queue.pop()
    high_to = dict_routing[bot]["h"]
    low_to = dict_routing[bot]["l"]
    high = max(dict_bots[bot])
    low = min(dict_bots[bot])
    dict_bots[bot] = []

    if dict_routing[bot]["ht"] == "bot":
        dict_bots[high_to].append(high)
    else:
        dict_outputs[high_to].append(high)

    if dict_routing[bot]["lt"] == "bot":
        dict_bots[low_to].append(low)
    else:
        dict_outputs[low_to].append(low)

    bot_with_2 = [k for k, v in dict_bots.items() if len(v) == 2]
    queue = queue + bot_with_2
    queue = list(set(queue))



print(dict_outputs[0][0] * dict_outputs[1][0] * dict_outputs[2][0])
