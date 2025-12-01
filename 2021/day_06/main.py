filename = "input.txt"
# filename = "input-test.txt"
lines = open(filename, encoding="utf-8").read().splitlines()


class Fish:
    def __init__(self, age: int):
        self.age = age

    def grow(self) -> bool:
        """Returns boolean on if to create a new fish"""
        if self.age == 0:
            self.age = 6
            return True

        self.age -= 1
        return False


ages = lines[0].split(",")
ages = [int(a) for a in ages]

fishes = [Fish(age=a) for a in ages]

# Now we pass time.
n_days = 80
for _ in range(n_days):
    new_fishes = []
    for f in fishes:
        out = f.grow()
        if out is True:
            new_fishes.append(Fish(age=8))

    fishes.extend(new_fishes)


print("Part 1:", len(fishes))

# Part 2 -- do it longer... Now it takes too long. Even test case can't finish.
# n_days = 256
# for _ in range(n_days):
#     new_fishes = []
#     for f in fishes:
#         out = f.grow()
#         if out is True:
#             new_fishes.append(Fish(age=8))

#     fishes.extend(new_fishes)

# We don't have to track all finishes. Just number of how many in each age.
class FishCohort:
    def __init__(self, age: int, num: int):
        self.age = age
        # Number of finishes in this cohort
        self.num = num

    def grow(self) -> int:
        """Returns number of new fishes to create."""
        if self.age == 0:
            self.age = 6
            return self.num

        self.age -= 1
        return 0

# This should work with question 1.
from collections import Counter


ages = lines[0].split(",")
ages = [int(a) for a in ages]

# fishes = [Fish(age=a) for a in ages]
counts = Counter(ages)
cohorts = [
    FishCohort(age=k, num=v)
    for k, v in counts.items()
]

# Now grow. Try part 1 first.
# n_days = 80
n_days = 256
for _ in range(n_days):
    num_new = 0
    for c in cohorts:
        out = c.grow()
        num_new += out

    cohorts.append(FishCohort(age=8, num=num_new))

# print("Part 1 (v2):", sum([c.num for c in cohorts]))


print("Part 2:", sum([c.num for c in cohorts]))
