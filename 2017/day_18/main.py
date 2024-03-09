# Problem type:
# ~~~~~~~~~~~~ follow instruction (part 1) ~~~~~~~~~~~~
# ~~~~~~~~~~~~ follow instruction X 2!! (part 2) ~~~~~~~~~~~~

from collections import defaultdict
import utils

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()
dict_reg = defaultdict(int)
last_played = None

i = 0
while i < len(lines) and i >= 0:
    inst = lines[i]
    segs = inst.split(" ")
    op = segs[0]
    v1 = segs[1]
    if v1.replace("-", "").isdigit():
        v1 = int(v1)
    else:
        v1 = dict_reg[v1]

    if len(segs) > 2:
        v2 = segs[2]
        if v2.replace("-", "").isdigit():
            v2 = int(v2)
        else:
            v2 = dict_reg[v2]
    else:
        v2 = None

    # print("dict_reg:", i, op, inst, dict_reg)

    if op == "snd":
        last_played = v1
        i += 1
    elif op == "set":
        dict_reg[segs[1]] = v2
        i += 1
    elif op == "add":
        dict_reg[segs[1]] += v2
        i += 1
    elif op == "mul":
        dict_reg[segs[1]] *= v2
        i += 1
    elif op == "mod":
        dict_reg[segs[1]] %= v2
        i += 1
    elif op == "rcv":
        if v1 > 0:
            break
        else:
            i += 1
    elif op == "jgz":
        if v1 > 0:
            i += v2
        else:
            i += 1
    else:
        raise Exception("Unrecognized op" + op)


print("Part 1:", last_played)

# Part 2.  Start with resettting.
lines = open(filename, encoding="utf-8").read().splitlines()
# For testing
lines_test = """\
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
""".splitlines()

def get_values(inst, dict_reg):
    segs = inst.split(" ")
    v1 = segs[1]
    if v1.replace("-", "").isdigit():
        v1 = int(v1)
    else:
        v1 = dict_reg[v1]

    if len(segs) > 2:
        v2 = segs[2]
        if v2.replace("-", "").isdigit():
            v2 = int(v2)
        else:
            v2 = dict_reg[v2]
    else:
        v2 = None
    return v1, v2


# We have to define classes.
class Pgm:
    def __init__(self, id):
        self.line_num = 0
        self.id = id
        self.dict_reg = defaultdict(int)
        self.dict_reg["p"] = id
        # Queue is the values it's received.
        self.queue = []
        self.num_sent = 0

    def do_inst(self, instructions, other_program):
        if self.line_num < 0 or self.line_num >= len(instructions):
            return "out"
        inst = instructions[self.line_num]
        # print("~*" * 20)
        # print(f"Program {self.id} doing instruction '{inst}'")
        # print("Before:", self.dict_reg)
        segs = inst.split(" ")
        op = segs[0]
        v1, v2 = get_values(inst, self.dict_reg)
        if op == "snd":
            # Send a sound. Equivalent to appending v1 to the other program.
            other_program.queue.append(v1)
            self.num_sent += 1
            self.line_num += 1
        elif op == "set":
            self.dict_reg[segs[1]] = v2
            self.line_num += 1
        elif op == "add":
            self.dict_reg[segs[1]] += v2
            self.line_num += 1
        elif op == "mul":
            self.dict_reg[segs[1]] *= v2
            self.line_num += 1
        elif op == "mod":
            self.dict_reg[segs[1]] %= v2
            self.line_num += 1
        elif op == "rcv":
            # Receives a sound. Pop the first value of the queue.
            if len(self.queue) > 0:
                v = self.queue[0]
                self.dict_reg[segs[1]] = v
                self.queue = self.queue[1:]
                self.line_num += 1
            else:
                # If there is no item in the queue but we are receiving, then
                # just wait.
                return "waiting"
        elif op == "jgz":
            if v1 > 0:
                self.line_num += v2
            else:
                self.line_num += 1
        else:
            raise Exception("Unrecognized op" + op)

        # print("After:", self.dict_reg)
        # print("--" * 20)
        return "done"


pgm0 = Pgm(0)
pgm1 = Pgm(1)

while True:
    res0 = pgm0.do_inst(lines, pgm1)
    res1 = pgm1.do_inst(lines, pgm0)
    if res0 != "done" and res1 != "done":
        # print(res0, res1)
        break

print("Part 2:", pgm1.num_sent)
