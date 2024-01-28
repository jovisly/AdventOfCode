"""Reflections: This feels like a Project Euler problem!"""


def get_divisors(n):
    d = [1, n]
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            d.append(i)
            d.append(n // i)

    return list(set(d))


def get_num_presents(house_num):
    return sum(get_divisors(house_num)) * 10



def get_num_presents2(house_num, limit=50):
    divisors = get_divisors(house_num)
    divisors = [d for d in divisors if d * 50 >= house_num]
    return sum(divisors) * 11



def solve():
    i = 0
    while True:
        i += 1
        n = get_num_presents(i)
        if n >= 34_000_000:
            break
    print("Part 1:", i)

    i = 0
    while True:
        i += 1
        n = get_num_presents2(i)
        if n >= 34_000_000:
            break
    print("Part 2:", i)



if __name__ == "__main__":
    solve()


