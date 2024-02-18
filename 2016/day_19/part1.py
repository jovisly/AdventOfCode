NUM = 5
NUM = 3014387

arr = [1] * NUM
# We are using set for the faster membership check.
has_present = set([i for i in range(NUM)])

i = -1
while len(has_present) > 1:
    if len(has_present) % 10000 == 0:
        print(len(has_present))
    i = (i + 1) % NUM
    if i in has_present:
        # j is the smallest index greater than i, or the smallest index less
        # than i.
        j = (i + 1) % NUM
        while j not in has_present:
            j = (j + 1) % NUM

        arr[i] += arr[j]
        arr[j] = 0
        has_present.remove(j)

# Note, this is index, so we need to add 1.
print(has_present)
