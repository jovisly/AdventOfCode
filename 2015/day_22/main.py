"""Is this MTG?

Reflections: The number of rounds should not exceed 50. This is because each
round, the boss deals damange = 10, and even with armor effect of 7 and heal of
2, that's still 1. So by round 50, the player would lose. Each round there are
5 possible actions. We can't really deal with 5 ** 50 even if we can eliminate a
lot of possibilities due to restrictions. Even if we reduce it to 10 rounds that's
still 5 ** 10.

If we want least amount of mana, we want to end the game fast?

Looking at the game setup, it's actually very difficult to win the game. So
let's just try some simulations without optimization and see what happens.

We first set up the simulation and run it for 10M games with randomly selected
user action. In this case, no game was won by the player.

Second attempt was to make the game interactive, and I used the strategy of
cycles of shi-rec-poi until later rounds when I then use a lot of missles. The
reason was that player hp is a lot lower, so we use shi as soon as possible. Then
we'd run out of mana with poi, so we do rec next. Then poi is the most effective
attack so we do that, and these three make a cycle. Sadly though, this strategy
also doesn't work.

Finally I set up a queued search. That runs for about a minute but we were able
to get the answer: it's actually cycles of poi-rec-shi instead of shi-rec-poi,
which is surprising -- the player can take two full hits until using shield. Ok.

Is this question more difficult than day 19? This one is certainly more tedious
to set up and very bugs-prone (need to understand the rules, and having played
MTG quite helps). But in terms of search, day 19 can lead to being stuck, whereas
once the search was set up here, it could be done just fine.
"""
import heapq
import random

class Boss:
    def __init__(self, hp=71, dam=10):
        self.dam = dam
        self.hp = hp

COST_MIS = 53
COST_DRA = 73
COST_SHI = 113
COST_POI = 173
COST_REC = 229

DICT_COST = {
    "mis": COST_MIS,
    "dra": COST_DRA,
    "shi": COST_SHI,
    "poi": COST_POI,
    "rec": COST_REC,
}

class Player:
    def __init__(self, hp=50, mana=500):
        self.hp = hp
        self.mana = mana
        self.mana_spent = 0
        self.dam = 0
        self.arm = 0

        self.turn_shi = 0
        self.turn_poi = 0
        self.turn_rec = 0

    def cast_spell(self, name, boss):
        if name == "mis":
            self.cast_mis(boss)
        elif name == "dra":
            self.cast_dra(boss)
        elif name == "shi":
            self.cast_shi()
        elif name == "poi":
            self.cast_poi()
        elif name == "rec":
            self.cast_rec()

    def cast_mis(self, boss):
        self.mana -= COST_MIS
        self.mana_spent += COST_MIS
        boss.hp -= 4

    def cast_dra(self, boss):
        self.mana -= COST_DRA
        self.mana_spent += COST_DRA
        self.hp += 2
        boss.hp -= 2

    def cast_shi(self):
        self.mana -= COST_SHI
        self.mana_spent += COST_SHI
        self.turn_shi = 6
        self.arm = 7

    def cast_poi(self):
        self.mana -= COST_POI
        self.mana_spent += COST_POI
        self.turn_poi = 6

    def cast_rec(self):
        self.mana -= COST_REC
        self.mana_spent += COST_REC
        self.turn_rec = 5

    def get_available_spells(self):
        spells = []
        if self.mana >= COST_MIS:
            spells.append("mis")
        if self.mana >= COST_DRA:
            spells.append("dra")
        if self.turn_shi == 0 and self.mana >= COST_SHI:
            spells.append("shi")
        if self.turn_poi == 0 and self.mana >= COST_POI:
            spells.append("poi")
        if self.turn_rec == 0 and self.mana >= COST_REC:
            spells.append("rec")
        return spells


class Game:
    def __init__(self, interactive=False, part2=False):
        self.boss = Boss()
        self.player = Player()
        self.turn_num = 1
        self.ended = False
        self.player_won = False
        self.interactive = interactive
        self.part2 = part2

    def take_player_turn(self, move=None):
        self.chores_before_turn()
        # Player loses if no more hp.
        if self.player.hp <= 0:
            self.ended = True
            self.player_won = False
            return

        if self.interactive:
            print(f"--- Turn {self.turn_num} ---")
            print("  player...", self.player.__dict__)
        spells = self.player.get_available_spells()
        # Player loses if not enough mana to cast a spell.
        if len(spells) == 0:
            self.ended = True
            self.player_won = False
            return

        if not self.interactive:
            if move is not None and move in spells:
                spell = move
            else:
                spell = random.choice(spells)
        else:
            print(f"    available spells: {spells}")
            spell = input("    pick: ")
        # print(f"    casts: {spell}")
        self.player.cast_spell(spell, self.boss)
        self.chores_after_turn()

    def take_boss_turn(self):
        self.chores_before_turn(is_player_turn=False)
        if self.interactive:
            print("  boss...", self.boss.__dict__)
        dam = max(1, self.boss.dam - self.player.arm)
        self.player.hp -= dam
        self.chores_after_turn()

    def chores_before_turn(self, is_player_turn=True):
        # In part 2, player loses 1 hp.
        if self.part2 and is_player_turn:
            self.player.hp -= 1

        # Shield.
        if self.player.turn_shi > 0:
            self.player.turn_shi -= 1
            if self.player.turn_shi == 0:
                self.player.arm = 0
        # Poison.
        if self.player.turn_poi > 0:
            self.player.turn_poi -= 1
            self.boss.hp -= 3
        # Recharge.
        if self.player.turn_rec > 0:
            self.player.turn_rec -= 1
            self.player.mana += 101


    def chores_after_turn(self):
        self.turn_num += 1
        if self.player.hp <= 0:
            self.ended = True
            self.player_won = False

        if self.boss.hp <= 0:
            self.ended = True
            self.player_won = True


def play_game(interactive=False):
    game = Game(interactive=interactive)
    while game.ended == False:
        game.take_player_turn()
        if game.ended == False:
            game.take_boss_turn()

    return game


def setup_game_with_moves(moves, part2=False):
    list_m = moves.split("-")
    list_m = [m for m in list_m if m]
    game = Game(part2=part2)
    for m in list_m:
        game.take_player_turn(m)
        if game.ended == False:
            game.take_boss_turn()
    return game



if __name__ == "__main__":
    # Attempt 1: Just simulate a lot of random moves. After 2M, still no wins.
    #
    # num_games = 100_000
    # tot_turns = 0
    # for _ in range(num_games):
    #     g = play_game()
    #     tot_turns += g.turn_num
    #     if g.player_won:
    #         print(g.player.mana_spent)

    # Attempt 2: Interactive mode. I decide what strategy to use. I'd think we
    # want shi-rec-poi-shi-rec-poi cycle until last few moves, where we use
    # mis, but that answer was not low enough.
    #
    # g = play_game(interactive=True)
    # print("Game ended:")
    # print("  did player win?", g.player_won)
    # print("  mana spent:", g.player.mana_spent)

    # Attemp 3: A more systemmatic search. Kinda like day 19 (2015). At each
    # player turn, get all possible moves, make those moves, and add them to the
    # queue (if game hasn't ended).
    #
    # queue is total mana spent, and sequence of moves (like "shi-rec-poi-shi").
    queue = [(0, "")]
    visited = {""}
    found = False

    while len(queue) > 0 and not found:
        curr_mana, curr_moves = heapq.heappop(queue)
        game = setup_game_with_moves(curr_moves)

        # print("curr_moves:", curr_mana, curr_moves)

        # Check if the game has ended.
        if game.ended:
            if game.player_won:
                found = True
                print("Part 1 - Found a won game:", game.player.mana_spent, curr_moves)
            else:
                # Player lost, then keep searching.
                continue

        # If game has not ended, then check all available moves and add to queue.
        # Do the player's turn but need to do some chores first.
        game.chores_before_turn()
        spells = game.player.get_available_spells()

        # For each spell, add them to queue.
        for s in spells:
            if curr_moves == "":
                seq = s
            else:
                seq = curr_moves + "-" + s

            if seq not in visited:
                # Need to calculate mana spent.
                heapq.heappush(queue, (curr_mana + DICT_COST[s], seq))
                visited.add(seq)

    # Part 2, the same search but with hp reduction.
    queue = [(0, "")]
    visited = {""}
    found = False

    while len(queue) > 0 and not found:
        curr_mana, curr_moves = heapq.heappop(queue)
        game = setup_game_with_moves(curr_moves, part2=True)

        if game.ended:
            if game.player_won:
                found = True
                print("Part 2 - Found a won game:", game.player.mana_spent, curr_moves)
            else:
                # Player lost, then keep searching.
                continue

        # If game has not ended, then check all available moves and add to queue.
        # Do the player's turn but need to do some chores first.
        game.chores_before_turn()
        spells = game.player.get_available_spells()

        # For each spell, add them to queue.
        for s in spells:
            if curr_moves == "":
                seq = s
            else:
                seq = curr_moves + "-" + s

            if seq not in visited:
                # Need to calculate mana spent.
                heapq.heappush(queue, (curr_mana + DICT_COST[s], seq))
                visited.add(seq)

