def look_and_say(input):
    curr = None
    output = ""
    for i in list(input):
        if curr is None:
            curr = i
            count = 1
        elif i == curr:
            count += 1
        else:
            output += str(count) + curr
            curr = i
            count = 1

    # Add the last one
    output += str(count) + curr
    return output


def solve(input):
    output = input
    for _ in range(40):
        output = look_and_say(output)

    print("Part 1:", len(output))

    output = input
    for _ in range(50):
        output = look_and_say(output)
    print("Part 2:", len(output))


if __name__ == "__main__":
    input = "1113222113"
    solve(input)


