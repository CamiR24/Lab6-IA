from TDAgent import TDAgent
from Connect4 import Connect4
from RandomAgent import random_move

#función para evaluar el desempeño dle agente
def evaluate(agent, games=1000):
    wins = 0

    for _ in range(games):
        game = Connect4()
        player = 1

        while not game.is_terminal():
            if player == 1:
                action = agent.choose_action(game)
            else:
                action = random_move(game)

            game.drop_piece(action, player)
            player *= -1

        if game.check_winner(1):
            wins += 1

    return wins / games

def train_agent(episodes=50000):

    n_features = 5
    agent = TDAgent(n_features=n_features, alpha=0.01, gamma=0.9, epsilon=0.1)

    # loop de entrenamiento
    for episode in range(episodes):

        game = Connect4()
        state = game
        player = 1

        while not game.is_terminal():

            if player == 1:
                action = agent.choose_action(game)
            else:
                action = random_move(game)

            next_state = game.copy()
            next_state.drop_piece(action, player)

            # recompensa
            if next_state.check_winner(player):
                reward = 1 if player == 1 else -1
            elif next_state.is_terminal():
                reward = 0
            else:
                reward = 0

            if player == 1:
                agent.update(state, reward, next_state)

            game = next_state
            state = next_state
            player *= -1

        agent.epsilon = max(0.05, agent.epsilon * 0.995)

        if episode % 1000 == 0:
            print(f"Episodio {episode} | epsilon: {agent.epsilon:.3f}")

    return agent