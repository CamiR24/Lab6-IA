import numpy as np

class TDAgent:
    def __init__(self):
        self.weights = np.random.randn(n_features)

    def value(self, board):
        features = extract_features(board)
        return np.dot(self.weights, features)
    
    #politica e-greedy para evitar quedarse en óptimos locales
    def choose_action(board):
        if random.random() < epsilon:
            return random_move(board)
        
        best_value = -inf
        best_action = None

        for a in board.actions():
            new_board = board.copy()
            new_board.drop_piece(a, 1)

            v = agent.value(new_board)

            if v > best_value:
                best_value = v
                best_action = a

        return best_action