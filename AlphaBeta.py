import math

def minimax_ab(board, depth, alpha, beta, maximizing_player):
    #Caso base
    if depth == 0 or board.is_terminal():
        return board.evaluate(), None, 1  # 1 nodo visitado

    total_nodes = 1
    valid_moves = board.actions()

    if maximizing_player:
        max_eval = -math.inf
        best_move = None

        for move in valid_moves:
            new_board = board.copy()
            new_board.drop_piece(move, 1) #coloca la pieza

            eval_score, _, child_nodes = minimax_ab(
                new_board, depth - 1, alpha, beta, False
            ) #llamada recursiva

            total_nodes += child_nodes

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move

            alpha = max(alpha, eval_score)
            if beta <= alpha: #PODA SI BETA ES MENOR O IGUAL A ALPHA
                break

        return max_eval, best_move, total_nodes

    else:
        min_eval = math.inf
        best_move = None

        for move in valid_moves:
            new_board = board.copy()
            new_board.drop_piece(move, -1) #coloca la pieza

            eval_score, _, child_nodes = minimax_ab(
                new_board, depth - 1, alpha, beta, True
            ) #llamada recursiva

            total_nodes += child_nodes

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move

            beta = min(beta, eval_score)
            if beta <= alpha: #PODA SI BETA ES MENOR O IGUAL A ALPHA
                break

        return min_eval, best_move, total_nodes