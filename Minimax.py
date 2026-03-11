import numpy as np
import math

def minimax(board, depth, maximizing_player): #función minimax

    if depth == 0 or board.is_terminal():
        return board.evaluate(), None, 1  #1 nodo visitado

    total_nodes = 1

    valid_moves = board.actions() #obtiene valores permitidos

    if maximizing_player:
        max_eval = -math.inf
        best_move = None

        for move in valid_moves:
            new_board = board.copy()
            new_board.drop_piece(move, 1) #coloca pieza

            eval_score, _, child_nodes = minimax(new_board, depth - 1, False) #llamada recursiva

            total_nodes += child_nodes

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move

        return max_eval, best_move, total_nodes

    else:
        min_eval = math.inf
        best_move = None

        for move in valid_moves:
            new_board = board.copy()
            new_board.drop_piece(move, -1) #coloca pieza

            eval_score, _, child_nodes = minimax(new_board, depth - 1, True) #llamada recursiva

            total_nodes += child_nodes

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move

        return min_eval, best_move, total_nodes