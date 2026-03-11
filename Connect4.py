import numpy as np
import math
import copy

ROWS = 6
COLS = 7

class Connect4:
    
    def __init__(self): #inicializar
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
    
    def is_terminal(self): #termina el juego
        return self.check_winner(1) or self.check_winner(-1) or len(self.actions()) == 0
    
    def check_winner(self, player): #verifica la victoria 
        # Horizontal
        for r in range(ROWS):
            for c in range(COLS - 3): #misma fila, solo cambia de columna
                if all(self.board[r][c+i] == player for i in range(4)):
                    return True
        
        # Vertical
        for r in range(ROWS - 3):
            for c in range(COLS): #misma columna, solo cambia de fila
                if all(self.board[r+i][c] == player for i in range(4)):
                    return True
        
        # Diagonal derecha
        for r in range(ROWS - 3):
            for c in range(COLS - 3): #cambia de columna de y de fila con pendiente positiva
                if all(self.board[r+i][c+i] == player for i in range(4)):
                    return True
        
        # Diagonal izquierda
        for r in range(3, ROWS):
            for c in range(COLS - 3): #cambia de columna de y de fila con pendiente negativa
                if all(self.board[r-i][c+i] == player for i in range(4)):
                    return True
        
        return False
    
    