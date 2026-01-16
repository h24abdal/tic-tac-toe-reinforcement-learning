from ttt_env import TicTacToeEnv
from agents import QLearningAgent, RandomAgent


def train(num_episodes=50000):
    env = TicTacToeEnv()
    agent = QLearningAgent()
    opponent = RandomAgent()

    for episode in range(num_episodes):
        env.reset()
        done = False

        while not done:
            state = env.board.copy()
            available_actions = env.available_actions()

            # RL agent move
            action = agent.act(state, available_actions, training=True)
            next_state, reward, done = env.step(action)

            next_available_actions = env.available_actions()

            agent.update(
                state,
                action,
                reward,
                next_state,
                done,
                next_available_actions,
            )

            if done:
                break

            # Opponent (random) move
            opp_action = opponent.act(env.board, env.available_actions())
            _, _, done = env.step(opp_action)

    return agent


if __name__ == "__main__":
    trained_agent = train(10000)
    print("Training finished")











