"""
Time: 10 minutes

Reflections: Wow I'm suprised part 2 didn't turn out to be extra challenging and
kindly lowered number of blueprints to 3. That allowed me to use exactly the same
method as part 1 but simply changed time to 32.
"""
from tqdm import tqdm

from part1 import parse_blueprint, make_robots, get_robots_can_make, ROBOT_TYPES, get_score, prune_queue


def make_robots(dict_blueprint, t=32, max_queue_length=60_000):
    queue = [{
        "r_ore": 1,
        "r_clay": 0,
        "r_obsidian": 0,
        "r_geode": 0,
        "m_ore": 0,
        "m_clay": 0,
        "m_obsidian": 0,
        "m_geode": 0,
        "score": 0
    }]
    while t > 0:
        new_queue = []

        for q in queue:
            dict_stuff = q.copy()

            # Check what materials we have and if we should build anything.
            robots_can_make = get_robots_can_make(dict_blueprint, dict_stuff)
            for r in robots_can_make:
                new_dict_stuff = dict_stuff.copy()
                req = dict_blueprint[r]
                for m, n in req.items():
                    new_dict_stuff[f"m_{m}"] -= n

                # Let the existing robot make new materials before we add the
                # new robot.
                for r2 in ROBOT_TYPES:
                    n = new_dict_stuff[f"r_{r2}"]
                    new_dict_stuff[f"m_{r2}"] += n

                # Then add the new robot that just got made and score the queue.
                new_dict_stuff[f"r_{r}"] += 1
                new_dict_stuff["score"] = get_score(new_dict_stuff)
                new_queue.append(new_dict_stuff)

            # It's also acceptable to not make any new robot and just make
            # materials.
            new_dict_stuff = dict_stuff.copy()
            for r in ROBOT_TYPES:
                n = new_dict_stuff[f"r_{r}"]
                new_dict_stuff[f"m_{r}"] += n

            new_dict_stuff["score"] = get_score(new_dict_stuff)
            new_queue.append(new_dict_stuff)


        t -= 1
        queue = [q.copy() for q in new_queue]
        # Dedupe.
        queue = [dict(t) for t in {tuple(q.items()) for q in queue}]

        if len(queue) > max_queue_length:
            queue = prune_queue(queue, max_queue_length)


    return max([q["m_geode"] for q in queue])


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    blueprints = [parse_blueprint(line) for line in lines]
    # Reduce it to the first three.
    blueprints = blueprints[:3]

    total = 1
    for b in tqdm(blueprints):
        output = make_robots(b)
        total *= output

    return total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 56 * 62


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
