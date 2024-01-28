"""
There are total of 5 weapons * 6 armors (including none) * (6 pick 2 + 6 pick 1
+ none) = 5 * 6 * (15 + 6 + 1) = 660 options. Not too bad to just check them all.
"""
import math
from itertools import combinations


WEAPONS = """\
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""

ARMORS = """\
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""

RINGS = """\
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

def get_dict(points, damage, armor):
    return {
        "points": points,
        "damage": damage,
        "armor": armor
    }


def player_wins(dict_player, dict_boss):
    points_p = dict_player["points"]
    points_b = dict_boss["points"]
    damage_p = dict_player["damage"]
    damage_b = dict_boss["damage"]
    armor_p = dict_player["armor"]
    armor_b = dict_boss["armor"]

    # Damage dealt by player each round.
    damage_actual_p = max(1, damage_p - armor_b)
    damage_actual_b = max(1, damage_b - armor_p)

    # How many rounds can each last. This had a bug.
    # num_rounds_p = 1 + points_p // damage_actual_b
    # num_rounds_b = 1 + points_b // damage_actual_p
    num_rounds_p = math.ceil(points_p / damage_actual_b)
    num_rounds_b = math.ceil(points_b / damage_actual_p)

    if num_rounds_b > num_rounds_p:
        # print("Boss wins")
        return False
    else:
        # print("Player wins")
        return True


# Created this function because player_wins() was giving me wrong answer. This
# helped to debug.
def player_wins_v2(dict_player, dict_boss):
    points_p = dict_player["points"]
    points_b = dict_boss["points"]
    damage_p = dict_player["damage"]
    damage_b = dict_boss["damage"]
    armor_p = dict_player["armor"]
    armor_b = dict_boss["armor"]

    while True:
        points_b -= max(1, damage_p - armor_b)
        if points_b <= 0:
            return True
        points_p -= max(1, damage_b - armor_p)
        if points_p <= 0:
            return False


def get_weapons():
    ws = []
    for line in WEAPONS.splitlines():
        es = line.split(" ")
        es = [e for e in es if e]
        ws.append((int(es[1]), int(es[2])))

    return ws


def get_armors():
    # Not using armor is an option.
    ars = [(0, 0)]
    for line in ARMORS.splitlines():
        es = line.split(" ")
        es = [e for e in es if e]
        # (cost, armor)
        ars.append((int(es[1]), int(es[3])))
    return ars


def get_rings():
    # Can choose to not use any ring for both hands.
    rs = [(0, 0, 0), (0, 0, 0)]
    for line in RINGS.splitlines():
        es = line.split(" ")
        es = [e for e in es if e]
        # (cost, damage, armor)
        rs.append((int(es[2]), int(es[3]), int(es[4])))
    return rs


def solve():
    dict_boss = get_dict(103, 9, 2)
    weapons = get_weapons()
    armors = get_armors()
    rings = get_rings()

    all_w = weapons
    all_a = armors
    all_r = list(combinations(rings, 2))
    min_g = 9999999999
    for w in all_w:
        for a in all_a:
            for r in all_r:
                g = w[0] + a[0] + r[0][0] + r[1][0]
                damage = w[1] + r[0][1] + r[1][1]
                armor = a[1] + r[0][2] + r[1][2]
                dict_player = get_dict(100, damage, armor)
                if player_wins_v2(dict_player, dict_boss) and g < min_g:
                    min_g = g

    print("Part 1:", min_g)

    # Reset.
    all_w = weapons
    all_a = armors
    all_r = list(combinations(rings, 2))
    max_g = 0
    for w in all_w:
        for a in all_a:
            for r in all_r:
                g = w[0] + a[0] + r[0][0] + r[1][0]
                damage = w[1] + r[0][1] + r[1][1]
                armor = a[1] + r[0][2] + r[1][2]
                dict_player = get_dict(100, damage, armor)
                if not player_wins_v2(dict_player, dict_boss) and g > max_g:
                    max_g = g

    print("Part 2:", max_g)



if __name__ == "__main__":
    filename = "input.txt"
    solve()


