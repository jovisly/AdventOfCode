NUM = 5
NUM = 3014387

arr = [i + 1 for i in range(NUM)]

# ~S~L~O~W~ as we are doing a lot of list manipulations.
while len(arr) > 1:
    if len(arr) % 500 == 0:
        print(len(arr))
    # Get the center.
    l = len(arr) // 2
    # pop this one.
    arr.pop(l)
    # move the first one to last.
    f = arr.pop(0)
    arr.append(f)

print(arr)
