from z3 import Int, Solver, And

def get_pos_vel(line):
    pos, vel = line.split("@")
    pos = pos.split(",")
    pos = [int(p.strip()) for p in pos]
    vel = vel.split(",")
    vel = [int(v.strip()) for v in vel]
    return pos, vel


def solve(filename):
    lines = open(filename, encoding="utf-8").read().splitlines()
    hailstones = [get_pos_vel(line) for line in lines]

    # We have 3 variables, x, y, z, and 3 more for vx, vy, vx. In addition, each
    # timestep is a variable. Which is a lot. So let's try if we can get by with
    # just a few samples.
    z3_solver = Solver()

    # Time
    num_t = len(hailstones)
    variables_t = [Int(f"t{i}") for i in range(num_t)]
    for t in variables_t:
        z3_solver.add(t > 0)

    # Position
    x, y, z = Int("x"), Int("y"), Int("z")
    # Velocity
    vx, vy, vz = Int("vx"), Int("vy"), Int("vz")

    for ind, (pos, vec) in enumerate(hailstones):
        hx, hy, hz = pos
        hvx, hvy, hvz = vec
        z3_solver.add(x + variables_t[ind] * vx == hx + variables_t[ind] * hvx)
        z3_solver.add(y + variables_t[ind] * vy == hy + variables_t[ind] * hvy)
        z3_solver.add(z + variables_t[ind] * vz == hz + variables_t[ind] * hvz)

    print(f"Number of variables: {num_t + 6}")
    print("Model check:", z3_solver.check())
    m = z3_solver.model()

    return m[x].as_long() + m[y].as_long() + m[z].as_long()


def mini_test():
    filename = "input-test.txt"
    assert solve(filename) == 47


if __name__ == "__main__":
    mini_test()

    filename = "input.txt"
    total = solve(filename)

    print(total)
