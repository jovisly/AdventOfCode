import re


def parse_one_line(line):
    out = re.split(":", line)[1].strip().split(" ")
    out = [int(a) for a in out if a != ""]
    return out


def get_num_ways_to_win(total_time, max_distance):
    num_ways = 0
    for i in range(total_time):
        secs = i + 1
        speed = secs
        distance_traveled = speed * (total_time - secs)
        if distance_traveled > max_distance:
            num_ways += 1

    return num_ways


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    times_str, distances_str = lines

    times = parse_one_line(times_str)
    distances = parse_one_line(distances_str)

    result = 1
    for t, d in zip(times, distances):
        result *= get_num_ways_to_win(t, d)

    return result



def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 288


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
