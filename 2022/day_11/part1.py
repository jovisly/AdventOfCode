class Monkey:
    def __init__(
        self, num, items, divisible_test, throw_if_true, throw_if_false,
        operation_type, operation_val,
    ):
        self.num = num
        self.items = [{"orig": num + "-" + str(i), "curr": i} for i in items]
        self.divisible_test = divisible_test
        self.throw_if_true = throw_if_true
        self.throw_if_false = throw_if_false
        self.operation_type = operation_type
        self.operation_val = operation_val
        self.num_inspections = 0

    def update_item(self, item, new_val):
        return {
            "orig": item["orig"],
            "curr": new_val
        }

    def operate(self, reduce_worry=True, multiplier=1):
        if self.operation_type == "add":
            self.items = [
                self.update_item(item, item["curr"] + self.operation_val)
                for item in self.items
            ]
        elif self.operation_type == "multiply":
            self.items = [
                self.update_item(item, item["curr"] * self.operation_val)
                for item in self.items
            ]
        elif self.operation_type == "square":
            self.items = [
                self.update_item(item, item["curr"] * item["curr"])
                for item in self.items
            ]
        else:
            raise ValueError("Invalid operation type:", self.operation_type)


        # Then divide by 3, and take floor.
        if reduce_worry:
            self.items = [
                self.update_item(item, item["curr"] // 3)
                for item in self.items
            ]
        else:
            # Squash.
            self.items = [
                self.update_item(item, item["curr"] % multiplier)
                for item in self.items
            ]
        self.num_inspections += len(self.items)

    def throw_items(self, dict_monkey):
        for item in self.items:
            if item["curr"] % self.divisible_test == 0:
                new_owner = self.throw_if_true
                dict_monkey[new_owner].items.append(item)
            else:
                new_owner = self.throw_if_false
                dict_monkey[new_owner].items.append(item)
        self.items = []



def make_monkey(line):
    arr_lines = line.splitlines()
    monkey_num = arr_lines[0][:-1].split(" ")[1]
    items = arr_lines[1].split(":")[1].split(", ")
    items = [int(item.strip()) for item in items]

    if "old * old" in arr_lines[2]:
        operation_type = "square"
        operation_val = None
    elif "+" in arr_lines[2]:
        operation_type = "add"
        operation_val = int(arr_lines[2].split(" ")[-1])
    elif "*" in arr_lines[2]:
        operation_type = "multiply"
        operation_val = int(arr_lines[2].split(" ")[-1])
    else:
        raise ValueError("Invalid operation type:", arr_lines[2])

    divisible_test = int(arr_lines[3].split(" ")[-1])
    throw_if_true = arr_lines[4].split(" ")[-1]
    throw_if_false = arr_lines[5].split(" ")[-1]
    return Monkey(
        monkey_num, items, divisible_test, throw_if_true, throw_if_false,
        operation_type, operation_val
    )



def solve(filename):
    lines = open(filename, encoding="utf-8").read().split("\n\n")
    dict_monkey = {}
    for line in lines:
        monkey = make_monkey(line)
        dict_monkey[monkey.num] = monkey

    # Do 20 rounds.
    for _ in range(20):
        for i in range(len(dict_monkey)):
            monkey_num = str(i)
            monkey = dict_monkey[monkey_num]
            monkey.operate()
            monkey.throw_items(dict_monkey)

    num_inspections = [v.num_inspections for v in dict_monkey.values()]
    num_inspections.sort(reverse=True)

    return num_inspections[0] * num_inspections[1]


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 10605


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
