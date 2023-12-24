class CPU:
    def __init__(self):
        self.x = 1
        self.cycle = 1
        self.sum = 0

    def run_noop(self):
        self.incr_cycle()

    def run_addx(self, v):
        self.incr_cycle()
        self.incr_cycle(v)

    def incr_cycle(self, v=0):
        self.cycle += 1
        self.x += v
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.sum += self.x * self.cycle



def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    instructions = [lines.split(" ") for lines in lines]
    cpu = CPU()
    for instruction in instructions:
        if instruction[0] == "noop":
            cpu.run_noop()
        elif instruction[0] == "addx":
            cpu.run_addx(int(instruction[1]))

    return cpu.sum


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 13140


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
