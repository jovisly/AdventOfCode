# Problem type:
# ~~~~~~~ learning deque ~~~~~~~
# Initially I was doing my own array manipulation and had a really bad bug: I was
# adding 23 as points instead of the marble value. Sad. But the process of fixing
# this bug lead me to learn deque which is really great!
from collections import defaultdict, deque

n_players = 405
n_marbles = 71700

dict_scores = defaultdict(int)
marbles = deque([0])
player = 0

for marble in range(1, n_marbles + 1):
    if marble % 23 == 0:
        marbles.rotate(7)
        dict_scores[player] += marble
        dict_scores[player] += marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(marble)

    player += 1
    player = player % n_players


max_score = max(dict_scores.values())

print("Part 1:", max_score)


n_marbles *= 100

dict_scores = defaultdict(int)
marbles = deque([0])
player = 0

for marble in range(1, n_marbles + 1):
    if marble % 23 == 0:
        marbles.rotate(7)
        dict_scores[player] += marble
        dict_scores[player] += marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(marble)

    player += 1
    player = player % n_players


max_score = max(dict_scores.values())
print("Part 2:", max_score)
