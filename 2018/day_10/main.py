# Problem type:
# ~~~~~~~ Fun Visual! ~~~~~~~
# took me half an hour but it was a lot of fun!
import time

filename = "input.txt"
lines = open(filename, encoding="utf-8").read().splitlines()

def get_pos(line):
    pos = line.split(" velocity=")[0].split("position=")[1][1:-1].split(",")
    return tuple([int(p.strip()) for p in pos])


def get_vel(line):
    vel = line.split(" velocity=")[1][1:-1].split(",")
    return tuple([int(v.strip()) for v in vel])


def get_minmax(all_pos):
    x_vals = [p[0] for p in all_pos]
    y_vals = [p[1] for p in all_pos]
    return min(x_vals), max(x_vals), min(y_vals), max(y_vals)


def update_pos(all_pos, all_val):
    new_pos = []
    for pos, vel in zip(all_pos, all_vel):
        new_pos.append((pos[0] + vel[0], pos[1] + vel[1]))
    return new_pos


# Initialize.
all_pos = []
all_vel = []

for line in lines:
    all_pos.append(get_pos(line))
    all_vel.append(get_vel(line))

# Control c when we see a pattern.
num_sec = 0
while True:
    num_sec += 1
    print("  " + "+=" * 20 + "\n")
    # Update position.
    all_pos = update_pos(all_pos, all_vel)
    x_min, x_max, y_min, y_max = get_minmax(all_pos)
    # Only process  if it is not too big. We are betting that the actual result
    # is not too big.
    print(x_max - x_min, y_max - y_min, num_sec)
    # if (x_max - x_min) <= 240 and (y_max - y_min) <= 240:
    # We got part 1 so we know how small these two values need to be.
    if (x_max - x_min) <= 100 and (y_max - y_min) <= 10:
        for y in range(y_min, y_max + 1):
            line = ""
            for x in range(x_min, x_max + 1):
                if (x, y) in all_pos:
                    line += "#"
                else:
                    line += "."
            print(line)

        time.sleep(2)




