from tqdm import tqdm
import time

from part1 import make_monkey

def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    dict_monkey = {}
    multiplier = 1
    for line in lines:
        monkey = make_monkey(line)
        dict_monkey[monkey.num] = monkey
        multiplier *= monkey.divisible_test


    for _ in tqdm(range(10000)):
        for i in range(len(dict_monkey)):
            monkey_num = str(i)
            monkey = dict_monkey[monkey_num]
            monkey.operate(reduce_worry=False, multiplier=multiplier)
            monkey.throw_items(dict_monkey)

    num_inspections = [v.num_inspections for v in dict_monkey.values()]
    num_inspections.sort(reverse=True)
    print("result:", num_inspections[0] * num_inspections[1])
    return num_inspections[0] * num_inspections[1]


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 2713310158


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
