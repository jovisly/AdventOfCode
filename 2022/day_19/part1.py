"""
Time: This took me a good three plus hours.

Reflection:

I first tried a "greedy" approach where robots are made whenever possible. That
didn't work of course because I just end up with a bunch of ore/clay robots.

Then I tried a "breadth-first" approach where I identified all possible robots
that can be made, including not making any, and "split the path". The number of
path balloons very quickly. I got to a queue length of 1_677_620 at around 9 min
left, and the progress essentially stalled to a halt.

At this point I've spent about 90 minutes on this problem. So I looked for ideas
on Reddit thread. It seems like this is the same approach a lot of people took,
but with some smart pruning. Here let's just try a top-N pruning where we
prioritize on the number of geode robots. Then the question is how big should N
be? I've tried 1_000 which didn't work on the first row of the test dataset. Had
to boost it up to 20_000, which gets quite slow.

Bug Report:

Coming up with a good way to represent the robots was tricky. I also didn't want
to set up full classes. In addition they need to be queues -- hashable, sortable,
but also human readable to set up the update logic and debug. I'm not 100% happy
of what I have here but it got me through it.

A few issues I encountered:

* Prioritizing on materials was bad. Needed to prioritize on robots instead.
* Update logic order really matters. I had a bug where robots make materials
  first -- although this issue might've simply been due to not having big enough
  N for the top-N pruning.
* My queue originally had a lot of dupes. The way I set up the queue makes deduping
  not so efficient.

With N = 100_000, I was able to get to the right answer on the actual dataset.
It took about 5 minutes to run though. Also I think I added an extra 0 there
accidentally. 60_000 might've been enough.
"""
import re

from tqdm import tqdm

ROBOT_TYPES = ["ore", "clay", "obsidian", "geode"]
MATERIALS = {
    "ore": ["ore"],
    "clay": ["ore"],
    "obsidian": ["ore", "clay"],
    "geode": ["ore", "obsidian"]
}

def get_dict_blueprint(id):
    """Simple robot generator."""
    dict_blueprint = {"id": id}
    for t in ROBOT_TYPES:
        dict_blueprint[t] = {}
    return dict_blueprint


def parse_blueprint(blueprint):
    id = int(blueprint.split(":")[0].split(" ")[-1])
    robots = blueprint.split(":")[1].split(".")
    robots = [robot.strip() for robot in robots if robot.strip()]
    assert len(robots) == 4

    dict_blueprint = get_dict_blueprint(id)
    for robot, robot_type in zip(robots, ROBOT_TYPES):
        numbers = re.findall(r'\d+', robot)
        for number, material in zip(numbers, MATERIALS[robot_type]):
            dict_blueprint[robot_type][material] = int(number)
    return dict_blueprint



def get_robots_can_make(dict_blueprint, dict_stuff):
    robots_can_make = []
    for r in ROBOT_TYPES:
        req = dict_blueprint[r]
        can_make = True
        for m, n in req.items():
            if dict_stuff[f"m_{m}"] < n:
                can_make = False

        if can_make:
            robots_can_make.append(r)
    return robots_can_make


def prune_queue(queue, max_queue_length):
    """Reduce the queue to the top max_queue_length."""
    # Sort on score, and take only the highest max_queue_length.
    queue.sort(key=lambda x: x["score"], reverse=True)
    return queue[:max_queue_length]



def get_score(dict_stuff):
    """A score that prioritizes on getting geodes."""
    # Score on number of robots instead of materials, because the better robots
    # are more expensive, so scoring on materials will penalize making better
    # robots.
    return (
        1000 * dict_stuff["r_geode"] +
        10 * dict_stuff["r_obsidian"] +
        0.1 * dict_stuff["r_clay"] +
        0 * dict_stuff["r_ore"]
    )



def make_robots(dict_blueprint, t=24, max_queue_length=60_000):
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

    total = 0
    for b in tqdm(blueprints):
        output = make_robots(b)
        total += output * b["id"]

    return total


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 33


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
