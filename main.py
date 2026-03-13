import math
import time

from Connect4 import Connect4
from Minimax import minimax
from AlphaBeta import minimax_ab


def main():

    game = Connect4()

    #estado intermedio para que la poda sea más visible
    game.drop_piece(3, 1)
    game.drop_piece(3, -1)
    game.drop_piece(2, 1)
    game.drop_piece(4, -1)

    depth = 5

    print("Estado inicial:")
    print(game.board)

    start_time = time.time()
    score_mm, move_mm, nodes_mm = minimax(game, depth, True)
    end_time = time.time()

    print("\nMinimax")
    print("Mejor movimiento:", move_mm)
    print("Score:", score_mm)
    print("Nodos visitados:", nodes_mm)
    print("Tiempo:", round(end_time - start_time, 4))

    start_time = time.time()

    score_ab, move_ab, nodes_ab = minimax_ab(
        game, depth, -math.inf, math.inf, True
    )

    end_time = time.time()

    print("\nAlpha-Beta")
    print("Mejor movimiento:", move_ab)
    print("Score:", score_ab)
    print("Nodos visitados:", nodes_ab)
    print("Tiempo:", round(end_time - start_time, 4), "segundos")

    reduction = ((nodes_mm - nodes_ab) / nodes_mm) * 100 #compara la cantidad de nodos entre ambos algoritmos

    print("Reducción de nodos:", round(reduction, 2), "%")


if __name__ == "__main__":
    main()