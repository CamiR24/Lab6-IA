import numpy as np
import random
import math

def extract_features(board):
    grid = board.board

    return np.array([
        np.sum(grid == 1),   #fichas propias
        np.sum(grid == -1),  #fichas oponente
        np.sum(grid[:, 3] == 1),  #control del centro
        np.sum(grid[:, 3] == -1),
    ])

class TDAgent:
    def __init__(self, n_features, alpha=0.01, gamma=0.9, epsilon=0.1):
        self.weights = np.random.randn(n_features)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def value(self, board):
        features = extract_features(board)
        return np.dot(self.weights, features)

    #política ε-greedy para no caer en óptimos locales
    def choose_action(self, board):
        valid_moves = board.actions()

        #exploración
        if random.random() < self.epsilon:
            return random.choice(valid_moves)

        #explotación
        best_value = -math.inf
        best_action = None

        for a in valid_moves:
            new_board = board.copy()
            new_board.drop_piece(a, 1)

            v = self.value(new_board)

            if v > best_value:
                best_value = v
                best_action = a

        return best_action

    #función update TD(0)
    def update(self, state, reward, next_state):
        v = self.value(state)
        v_next = self.value(next_state)

        td_error = reward + self.gamma * v_next - v

        features = extract_features(state)

        self.weights += self.alpha * td_error * features