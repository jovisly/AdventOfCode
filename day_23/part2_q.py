"""Let's try to use Q Learning to solve this problem.

This works but also very slow. Slower than exhaustive search.
"""
import random
from part1 import DIRS


LEARNING_RATE = 0.8
DISCOUNT_FACTOR = 0.8
MAX_EPISODE_NUM = 10_000


def get_board(filename):
    """Get the board as a dictionary."""
    lines = open(filename, encoding="utf-8").read().splitlines()
    list_board = [list(l) for l in lines]
    num_rows = len(list_board)
    num_cols = len(list_board[0])
    start = (0, 1)
    end = (num_rows - 1, num_cols -2)

    return {
        (i, j): val
        for i, row in enumerate(list_board)
        for j, val in enumerate(row)
    }, start, end


class QLearner:
    def __init__(self, board, start, end):
        self.board = board
        self.q_table = self.get_q_table()
        self.start = start
        self.end = end


    def get_q_table(self):
        """Given a board, return Q table.

        States: (r, c)
        Actions: the four possible next positions parsed down by validity.
        """
        q_table = {}
        for pos, val in self.board.items():
            if val == "#":
                continue

            next_pos = [(pos[0] + dir[0], pos[1] + dir[1]) for dir in DIRS]
            next_pos = [p for p in next_pos if self.is_valid_position(p, {pos})]

            if len(next_pos) > 0:
                q_table[pos] = {p: 0 for p in next_pos}
        return q_table


    def run_one_episode(self, episode_num, max_episode_num=MAX_EPISODE_NUM):
        curr_pos = start
        visited = {start}
        while curr_pos != self.end and curr_pos in self.q_table:
            # Keep moving and updating q table.
            actions = self.q_table[curr_pos]
            actions = {k: v for k, v in actions.items() if self.is_valid_position(k, visited)}
            if len(actions) == 0:
                break

            # Anneal.
            epsilon = (1 - episode_num / max_episode_num)
            a = self.epsilon_greedy_policy(actions, epsilon)
            # Update q table.
            self.update_q_table(curr_pos, a, visited)
            # Move the agent.
            curr_pos = a
            visited.add(curr_pos)


    def greedy_policy(self, actions):
        return max(actions, key=actions.get)


    def epsilon_greedy_policy(self, actions, epsilon):
        if random.random() < epsilon:
            return random.choice(list(actions))
        else:
            return self.greedy_policy(actions)


    def calculate_reward(self, a, visited):
        if not self.is_valid_position(a, visited):
            return -10

        # The position is valid. Get path length.
        return len(visited)


    def calculate_max_reward(self, a, visited, debug=False):
        """Max reward given s and a is that we continue with greedy algo."""
        curr_pos = a
        new_visited = {v for v in visited}
        new_visited.add(curr_pos)
        while curr_pos != self.end and curr_pos in self.q_table:
            if debug:
                print(curr_pos)
            actions = self.q_table[curr_pos]
            actions = {k: v for k, v in actions.items() if self.is_valid_position(k, new_visited)}
            if len(actions) == 0:
                    break

            a = self.greedy_policy(actions)
            curr_pos = a
            new_visited.add(curr_pos)

        return len(new_visited) - 1 if curr_pos == self.end else -10


    def update_q_table(self, s, a, visited):
        """Update q_table following Bellman equation."""
        prev_q = self.q_table[s][a]
        r = self.calculate_reward(a, visited)
        max_r = self.calculate_max_reward(a, visited)
        self.q_table[s][a] = prev_q + LEARNING_RATE * (
            r + DISCOUNT_FACTOR * max_r - prev_q
        )


    def is_valid_position(self, pos, visited):
        if pos not in self.board:
            return False

        if pos in visited:
            return False

        return self.board[pos] != "#"



if __name__ == "__main__":
    filename = "input.txt"
    dict_board, start, end = get_board(filename)

    q_learner = QLearner(dict_board, start, end)

    for episode_num in range(MAX_EPISODE_NUM):
        q_learner.run_one_episode(episode_num)
        if episode_num % 1 == 0:
            max_reward = q_learner.calculate_max_reward(start, set())
            print(f"Episode {episode_num}: max reward {max_reward}")


    # Final reward after training.
    max_reward = q_learner.calculate_max_reward(start, set())
    print("Final max reward: ", max_reward)
