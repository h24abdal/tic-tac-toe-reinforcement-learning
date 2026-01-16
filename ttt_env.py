class TicTacToeEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        """
        Resets the board to an empty state.
        """
        self.board = [0] * 9
        self.current_player = 1
        return self.board

    def available_actions(self):
        """
        Returns a list of available actions (empty positions).
        """
        return [i for i, v in enumerate(self.board) if v == 0]

    def step(self, action):
        """
        Applies an action and returns:
        next_state, reward, done
        """
        # Invalid move
        if self.board[action] != 0:
            raise ValueError("Invalid action")

        # Apply move
        self.board[action] = self.current_player

        # Check for winner
        winner = self.check_winner()

        if winner is not None:
            reward = 1
            done = True
        elif len(self.available_actions()) == 0:
            reward = 0
            done = True
        else:
            reward = 0
            done = False
            self.current_player *= -1

        return self.board, reward, done

    def check_winner(self):
        """
        Checks if there is a winner.
        Returns 1, -1, or None.
        """
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != 0:
                return self.board[a]

        return None



