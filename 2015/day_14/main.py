def parse_line(line):
    es = line.split(" ")
    deer = es[0]
    speed = int(es[3])
    duration = int(es[6])
    rest = int(es[-2])
    return deer, speed, duration, rest


def get_dict_deers(lines):
    dict_deers = {}
    for line in lines:
        deer, speed, duration, rest = parse_line(line)
        dict_deers[deer] = (speed, duration, rest)
    return dict_deers


def get_distance(dict_deers, deer, num_seconds):
    speed, duration, rest = dict_deers[deer]
    num_cycles = num_seconds // (duration + rest)
    remainder = num_seconds % (duration + rest)
    distance = num_cycles * speed * duration
    if remainder < duration:
        distance += remainder * speed
    else:
        distance += speed * duration
    return distance


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    dict_deers = get_dict_deers(lines)
    max_dist = 0
    for d in list(dict_deers):
        dist = get_distance(dict_deers, d, num_seconds=2503)
        if dist > max_dist:
            max_dist = dist

    print("Part 1:", max_dist)

    dict_dist = {d: 0 for d in dict_deers}
    dict_points = {d: 0 for d in dict_deers}
    for sec in range(1, 2503 + 1):
        for d in list(dict_dist):
            dict_dist[d] = get_distance(dict_deers, d, num_seconds=sec)

        max_dist = max(dict_dist.values())
        winners = [d for d in dict_dist if dict_dist[d] == max_dist]
        for w in winners:
            dict_points[w] += 1

    max_points = max(dict_points.values())
    print("Part 2:", max_points)



if __name__ == "__main__":
    filename = "input.txt"
    solve(filename)


