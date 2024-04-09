# Problem type:
# ~~~~~~~ faith- (then test-) based programming, but still off by 1 ~~~~~~~
# Part 2 is tricky because the test case is quite different. So at first I just
# tried to make it work without test, but kept getting wrong answer. So finally
# I added enough if conditions to check against the test. And in the end I still
# have off by 1 error. Not sure if I just didn't get the problem definition clearly.
from collections import defaultdict

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

dict_deps = defaultdict(list)
first = None
chars = set()
for line in lines:
    parent = line.split(" ")[1]
    if first is None:
        first = parent
    child = line.split(" ")[7]
    chars.add(parent)
    chars.add(child)
    dict_deps[child].append(parent)


def get_unlocked(seq, chars, dict_deps):
    available = [c for c in chars if c not in list(seq)]
    # Check which one available is unlocked.
    unlocked = []
    for a in available:
        deps = dict_deps[a]
        deps_unsat = [d for d in deps if d not in list(seq)]
        if len(deps_unsat) == 0:
            unlocked.append(a)
    # Unlocked needs to be greater than 0.
    return sorted(unlocked)[0]


seq = first
while len(seq) != len(chars):
    # Check which chars have been unlocked.
    unlocked = get_unlocked(seq, chars, dict_deps)
    seq += unlocked

print("Part 1:", seq)

def get_time(char):
    if filename == "input.txt":
        return ord(char) - 4
    else:
        return ord(char) - 64


def get_list_unlocked(seq, chars, dict_deps):
    available = [c for c in chars if c not in list(seq)]
    # Check which one available is unlocked.
    unlocked = []
    for a in available:
        deps = dict_deps[a]
        deps_unsat = [d for d in deps if d not in list(seq)]
        if len(deps_unsat) == 0:
            unlocked.append(a)

    return sorted(unlocked)


class Worker:
    def __init__(self, id):
        self.id = id
        self.working_on = None
        self.work_ends = None


t = 0
seq = ""
num_workers = 5 if filename == "input.txt" else 2
workers = [Worker(i) for i in range(num_workers)]
# Set up the first work.
workers[0].working_on = first
workers[0].work_ends = get_time(first)

while len(seq) != len(chars):
    # print(f"t: {t}, seq: {seq}")
    t += 1
    # See if anything is done.
    for w in workers:
        if w.working_on is not None and w.work_ends <= t:
            # Done!
            done = w.working_on
            seq += done
            w.working_on = None
            w.work_ends = None
    # See if anyone has capacity to pick up work.
    unlocked = get_list_unlocked(seq, chars, dict_deps)
    # Filter out those that are unlocked but already being worked on.
    working_on = [w.working_on for w in workers if w.working_on is not None]
    unlocked = [u for u in unlocked if u not in working_on]
    for w in workers:
        if w.working_on is None and len(unlocked) > 0:
            work = unlocked[0]
            unlocked = unlocked[1:]
            w.working_on = work
            w.work_ends = t + get_time(work)

print("Part 2:", t - 1)
