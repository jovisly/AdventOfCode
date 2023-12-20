class FlipFlop:
    def __init__(self, name, targets):
        self.type = "FlipFlop"
        self.name = name
        self.targets = targets
        self.state = -1

    def receive_pulse(self, source, pulse):
        if pulse == "h":
            return []
        else :
            self.state *= -1
            return [
                {
                    "name": target,
                    "source": self.name,
                    "pulse": "h" if self.state == 1 else "l",
                } for target in self.targets
            ]


class Conjunction:
    def __init__(self, name, targets):
        self.type = "Conjunction"
        self.name = name
        self.targets = targets
        # Last pulse is keyed on the name of the source.
        self.last_pulse = {}

    def receive_pulse(self, source, pulse):
        # first update last_pulse.
        self.last_pulse[source] = pulse
        if all([True if p == "h" else False for p in self.last_pulse.values()]):
            pulse_to_send = "l"
        else:
            pulse_to_send = "h"
        return [
            {
                "name": target,
                "source": self.name,
                "pulse": pulse_to_send,
            } for target in self.targets
        ]



class Broadcaster:
    def __init__(self, targets):
        self.type = "Broadcaster"
        self.name = "broadcaster"
        self.targets = targets

    def receive_pulse(self, source, pulse):
        return [
            {
                "name": target,
                "source": self.name,
                "pulse": pulse,
            } for target in self.targets
        ]


def parse_line(line):
    """Turn each line into a tuple of name and module object."""
    [name, targets] = line.split(" -> ")
    targets = targets.split(", ")
    if name.startswith("%"):
        return name[1:], FlipFlop(name[1:], targets)
    elif name.startswith("&"):
        return name[1:], Conjunction(name[1:], targets)
    else:
        return "broadcaster", Broadcaster(targets)


def add_pulses(queue, num_h, num_l):
    for q in queue:
        if q["pulse"] == "h":
            num_h += 1
        else:
            num_l += 1
    return num_h, num_l


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()

    dict_modules = {
        parse_line(line)[0]: parse_line(line)[1]
        for line in lines
    }
    print("DICT MODULES")
    print(dict_modules)

    # Press button.
    # num_button_presses = 1000
    num_button_presses = 1
    num_h = 0
    num_l = 0
    queue = []
    for _ in range(num_button_presses):
        # Press button
        num_l += 1
        queue = dict_modules["broadcaster"].receive_pulse("button", "l")
        num_h, num_l = add_pulses(queue, num_h, num_l)
        while len(queue) > 0:
            # Go through all the items in the queue and construct a new queue.
            q = queue.pop()
            new_queue = []
            new_queue += dict_modules[q["name"]].receive_pulse(q["source"], q["pulse"])

            num_h, num_l = add_pulses(q, num_h, num_l)




    return 0


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 32000000

    # filename = "input-test2.txt"
    # assert solve(filename) == 11687500


if __name__ == "__main__":
    mini_test()

    # filename = "input.txt"
    # total = solve(filename)

    # print(total)
