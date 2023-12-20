class FlipFlop:
    def __init__(self, name, targets):
        self.type = "FlipFlop"
        self.name = name
        self.targets = targets
        self.state = -1

    def receive_pulse(self, pulse):
        if pulse == "l":
            self.state *= -1

        self.send_pulse()

    def send_pulse(self):
        pulse = "h" if self.state == -1 else "l"
        self.state *= -1
        return pulse


class Conjunction:
    def __init__(self, name, targets):
        self.type = "Conjunction"
        self.name = name
        self.targets = targets
        # Last pulse is keyed on the name of the source.
        self.last_pulse = {}

    def receive_pulse(self, name_source, pulse):
        # first update last_pulse.
        self.last_pulse[name_source] = pulse
        if all([True if p == "h" else False for p in self.last_pulse.values()]):
            self.send_pulse("l")
        else:
            self.send_pulse("l")

    def send_pulse():
        pass


class Broadcaster:
    def __init__(self, targets):
        self.type = "Broadcaster"
        self.name = "broadcaster"
        self.targets = targets

    def receive_and_send_pulse(self, dict_modules, pulse):
        for target in self.targets:
            dict_modules[target].receive_pulse(pulse)



def press_button(dict_modules):
    """Press the button to send a low pulse to the broadcaster module."""
    dict_modules["broadcaster"].receive_and_send_pulse("l")


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


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()

    dict_modules = {
        parse_line(line)[0]: parse_line(line)[1]
        for line in lines
    }
    print("DICT MODULES")
    print(dict_modules)
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
