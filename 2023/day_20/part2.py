import math
from part1 import *

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
dict_modules = get_dict_modules(lines)

# Waiting for rx took took long, so we see what makes it happen. It recieves
# from gq, which receives from ["xj", "qs", "kz", "km"]. So gq would only send l
# to rx if it received h from all of those in the same button press. So we trace
# those instead.
modules_of_interest = ["xj", "qs", "kz", "km"]
num_button_presses = 0
max_num_button_presses = 50000
dict_log = {m: set() for m in modules_of_interest}
while num_button_presses < max_num_button_presses:
    num_button_presses += 1
    # print("num_button_presses:", num_button_presses)
    queue = dict_modules["broadcaster"].receive_pulse()

    next_queue = []
    while len(queue) > 0:
        # Go through all the items in the queue and construct a new queue.
        q = queue.pop(0)
        if q.name not in dict_modules:
            pass
        else:
            next_queue += dict_modules[q.name].receive_pulse(q)

        if len(queue) == 0:
            queue = next_queue
            for q in queue:
                if q.source in modules_of_interest and q.pulse == "h":
                    dict_log[q.source].add(num_button_presses)

            next_queue = []


print("dict_log")
multiples = []
for k, v in dict_log.items():
    print(f"{k}: {sorted(v)}")
    multiples.append(sorted(v)[0])

print(math.lcm(*multiples))
