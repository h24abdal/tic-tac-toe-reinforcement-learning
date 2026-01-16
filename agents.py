import random


class RandomAgent:
    def act(self, board, available_actions):
        return random.choice(available_actions)


class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.95, epsilon=1.0, epsilon_decay=0.999):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.Q = {}

    def get_state_key(self, board):
        return tuple(board)

    def act(self, board, available_actions, training=True):
        state = self.get_state_key(board)

        if training and random.random() < self.epsilon:
            return random.choice(available_actions)

        q_values = [self.Q.get((state, a), 0) for a in available_actions]
        max_q = max(q_values)
        best_actions = [
            a for a, q in zip(available_actions, q_values) if q == max_q
        ]
        return random.choice(best_actions)

    def update(self, board, action, reward, next_board, done, next_available_actions):
        state = self.get_state_key(board)
        next_state = self.get_state_key(next_board)

        old_q = self.Q.get((state, action), 0)

        if done:
            target = reward
        else:
            future_qs = [
                self.Q.get((next_state, a), 0) for a in next_available_actions
            ]
            target = reward + self.gamma * max(future_qs)

        self.Q[(state, action)] = old_q + self.alpha * (target - old_q)
        self.epsilon *= self.epsilon_decay


class PerfectAgent:
    def act(self, board, available_actions):
        # 1. Win if possible
        for a in available_actions:
            board[a] = -1
            if self.check_winner(board) == -1:
                board[a] = 0
                return a
            board[a] = 0

        # 2. Block opponent win
        for a in available_actions:
            board[a] = 1
            if self.check_winner(board) == 1:
                board[a] = 0
                return a
            board[a] = 0

        # 3. Take center
        if 4 in available_actions:
            return 4

        # 4. Take a corner
        for a in [0, 2, 6, 8]:
            if a in available_actions:
                return a

        # 5. Take any side
        return available_actions[0]

    def check_winner(self, board):
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in combos:
            if board[a] == board[b] == board[c] != 0:
                return board[a]
        return None




  


