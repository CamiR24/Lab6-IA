import random

def random_move(board):
    return random.choice(board.actions())