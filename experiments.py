from Connect4 import Connect4
from Minimax import minimax
from AlphaBeta import minimax_ab
from TDAgent import TDAgent
from TDtrain import train_agent
import math
import random
import matplotlib.pyplot as plt
import numpy as np

def play_game(agent1, agent2):
    game = Connect4()
    player = random.choice([1, -1])

    while not game.is_terminal():

        if player == 1:
            move = agent1(game)
        else:
            move = agent2(game)

        game.drop_piece(move, player)
        player *= -1

    if game.check_winner(1):
        return 1
    elif game.check_winner(-1):
        return -1
    else:
        return 0

# Wrappers para agentes
def td_agent_fn(agent):
    return lambda board: agent.choose_action(board)

def minimax_fn(depth):
    return lambda board: minimax(board, depth, True)[1]

def alphabeta_fn(depth):
    return lambda board: minimax_ab(board, depth, -math.inf, math.inf, True)[1]

#Correr experimentos
def run_experiment(agent1, agent2, games=50):
    results = {"win":0, "loss":0, "draw":0}

    for _ in range(games):
        result = play_game(agent1, agent2)

        if result == 1:
            results["win"] += 1
        elif result == -1:
            results["loss"] += 1
        else:
            results["draw"] += 1

    return results

#Ejecución
def main():

    print("Entrenando TD...")
    td_agent = train_agent(episodes=30000)

    td = td_agent_fn(td_agent)
    mm = minimax_fn(depth=4)
    ab = alphabeta_fn(depth=5)

    print("Condición A: TD vs Minimax")
    A = run_experiment(td, mm)

    print("Condición B: TD vs AlphaBeta")
    B = run_experiment(td, ab)

    print("Condición C: Minimax vs AlphaBeta")
    C = run_experiment(mm, ab)

    print("A:", A)
    print("B:", B)
    print("C:", C)

    return A, B, C

#Gráfica
def plot_results(A, B, C):

    labels = ["Wins", "Losses", "Draws"]

    data = {
        "Condición A (TD vs Minimax)": [A["win"], A["loss"], A["draw"]],
        "Condición B (TD vs AlphaBeta)": [B["win"], B["loss"], B["draw"]],
        "Condición C (Minimax vs AlphaBeta)": [C["win"], C["loss"], C["draw"]],
    }

    x = np.arange(len(labels))
    width = 0.25

    plt.figure(figsize=(10,6))

    for i, (cond, values) in enumerate(data.items()):
        plt.bar(x + i*width, values, width=width, label=cond)

    plt.xticks(x + width, labels)
    plt.xlabel("Resultados")
    plt.ylabel("Número de partidas")
    plt.title("Desempeño de agentes en Connect Four (50 partidas por condición)")
    plt.legend()

    plt.tight_layout()

    plt.savefig("results.pdf")  # 🔥 ESTE ES EL QUE ENTREGAS
    plt.show()

if __name__ == "__main__":
    A, B, C = main()
    plot_results(A, B, C)