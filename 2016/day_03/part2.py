import utils

def parse_line(line):
    l = line.strip()
    ns = l.split(" ")
    ns = [n.strip() for n in ns]
    ns = [int(n) for n in ns if n]
    return ns


filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

parsed_lines = [parse_line(line) for line in lines]


dict_board = utils.get_dict_board(parsed_lines)

dict_fixed = {}
for k, v in dict_board.items():
    new_k = k[0] // 3
    if (new_k, k[1]) in dict_fixed:
        dict_fixed[(new_k, k[1])].append(v)
    else:
        dict_fixed[(new_k, k[1])] = [v]

print(len(dict_fixed))

num = 0
num_tri = 0
for ns in dict_fixed.values():
    num_tri += 1
    if ns[0] + ns[1] > ns[2] and ns[1] + ns[2] > ns[0] and ns[2] + ns[0] > ns[1]:
        num += 1

print(num_tri)
print(num)
