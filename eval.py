from ttt_env import TicTacToeEnv
from agents import RandomAgent


def evaluate(agent, num_games=1000):
    env = TicTacToeEnv()
    opponent = RandomAgent()

    wins = 0
    draws = 0
    losses = 0

    for _ in range(num_games):
        env.reset()
        done = False

        while not done:
            # Agent move
            action = agent.act(env.board, env.available_actions(), training=False)
            _, reward, done = env.step(action)

            if done:
                if reward == 1:
                    wins += 1
                else:
                    draws += 1
                break

            # Opponent move
            opp_action = opponent.act(env.board, env.available_actions())
            _, reward, done = env.step(opp_action)

            if done:
                losses += 1

    return wins, draws, losses


