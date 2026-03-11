import numpy as np
import math
import copy

ROWS = 6
COLS = 7

class Connect4:
    
    def __init__(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)
    
    def copy(self):
        new_game = Connect4()
        new_game.board = self.board.copy()
        return new_game
    
    def actions(self):
        return [c for c in range(COLS) if self.board[0][c] == 0]
    
    def drop_piece(self, col, player): #colocar pieza
        for row in reversed(range(ROWS)):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                break
    
    def is_terminal(self):
        return self.check_winner(1) or self.check_winner(-1) or len(self.actions()) == 0
    
    