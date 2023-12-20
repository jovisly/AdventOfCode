class Queue:
    def __init__(self, name, source, pulse, stop):
        self.name = name
        self.source = source
        self.pulse = pulse
        self.stop = stop


class FlipFlop:
    def __init__(self, name, targets, is_last):
        self.name = name
        self.targets = targets
        self.is_last = is_last
        self.state = -1

    def receive_pulse(self, queue_obj):
        if queue_obj.stop:
            return []
        elif queue_obj.pulse == "h":
            return []
        else :
            pulse_to_send = "h" if self.state == -1 else "l"
            stop = True if self.is_last else False
            self.state *= -1

            return [
                Queue(
                    name=target,
                    source=self.name,
                    pulse=pulse_to_send,
                    stop=stop
                )
                for target in self.targets
            ]


class Conjunction:
    def __init__(self, name, targets, is_last):
        self.name = name
        self.targets = targets
        self.is_last = is_last
        # Last pulse is keyed on the name of the source.
        self.last_pulse = {}

    def receive_pulse(self, queue_obj):
        if queue_obj.stop:
            return []

        # first update last_pulse.
        self.last_pulse[queue_obj.source] = queue_obj.pulse
        if all([True if p == "h" else False for p in self.last_pulse.values()]):
            pulse_to_send = "l"
        else:
            pulse_to_send = "h"

        stop = True if self.is_last else False
        return [
            Queue(
                name=target,
                source=self.name,
                pulse=pulse_to_send,
                stop=stop
            )
            for target in self.targets
        ]



class Broadcaster:
    def __init__(self, targets):
        self.name = "broadcaster"
        self.targets = targets

    def receive_pulse(self):
        return [
            Queue(
                name=target,
                source=self.name,
                # Button always sends a low pulse.
                pulse="l",
                stop=False
            )
            for target in self.targets
        ]


def get_dict_modules(lines):
    dict_modules = {}
    for ind, line in enumerate(lines):
        if ind == len(lines) - 1:
            is_last = True
        else:
            is_last = False

        [name, targets] = line.split(" -> ")
        targets = targets.split(", ")
        if name.startswith("%"):
            dict_modules[name[1:]] = FlipFlop(name[1:], targets, is_last)
        elif name.startswith("&"):
            dict_modules[name[1:]] = Conjunction(name[1:], targets, is_last)
        else:
            dict_modules["broadcaster"] = Broadcaster(targets)

    return dict_modules



def add_pulses(queue, num_h, num_l):
    for q in queue:
        if q.pulse == "h":
            num_h += 1
        else:
            num_l += 1
    return num_h, num_l


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_modules = get_dict_modules(lines)
    print("DICT MODULES")
    print(dict_modules)

    # Press button.
    # num_button_presses = 1000
    num_button_presses = 1
    num_h = 0
    num_l = 0

    for _ in range(num_button_presses):
        # Press button
        num_l += 1
        queue = dict_modules["broadcaster"].receive_pulse()
        print("=== ORIGINAL QUEUE:", queue)
        for q in queue:
            print("name:", q.name, "; pulse:", q.pulse)
        next_queue = []
        num_h, num_l = add_pulses(queue, num_h, num_l)
        while len(queue) > 0:
            # Go through all the items in the queue and construct a new queue.
            q = queue.pop(0)
            next_queue += dict_modules[q.name].receive_pulse(q)

            if len(queue) == 0:
                queue = next_queue
                print("=== NEW QUEUE:", queue)
                for q in queue:
                    print("name:", q.name, "; pulse:", q.pulse)
                next_queue = []
                num_h, num_l = add_pulses(queue, num_h, num_l)

    print("NUM H", num_h)
    print("NUM L", num_l)


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
