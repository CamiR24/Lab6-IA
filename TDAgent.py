import numpy as np

class TDAgent:
    def __init__(self):
        self.weights = np.random.randn(n_features)

    def value(self, board):
        features = extract_features(board)
        return np.dot(self.weights, features)