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
    
    def evaluate(self): #función para definir que valor devuelve dependiendo si gana, pierde o empata
        if self.check_winner(1):
            return 1000
        elif self.check_winner(-1):
            return -1000
        else:
            return 0
        
node_counter = 0 #contador de nodos

def minimax(board, depth, maximizing_player): #función minimax
    global node_counter
    node_counter += 1
        
    if depth == 0 or board.is_terminal():
        return board.evaluate(), None
        
    valid_moves = board.actions() #obtiene los movimientos válidos que puede realizar
        
    if maximizing_player: 
        max_eval = -math.inf
        best_move = None
            
        for move in valid_moves:
            new_board = board.copy()
            new_board.drop_piece(move, 1) #para cada movimiento deja caer la pieza
                
            eval_score, _ = minimax(new_board, depth - 1, False) #llamada recursiva
                
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            
        return max_eval, best_move #max
        
    else: 
        min_eval = math.inf
        best_move = None
            
        for move in valid_moves:
            new_board = board.copy()
            new_board.drop_piece(move, -1) #para cada movimiento deja caer la pieza
                
            eval_score, _ = minimax(new_board, depth - 1, True) #llamada recursiva
                
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            
        return min_eval, best_move #min
        
game = Connect4()
# Estado inicial
depth = 4

node_counter = 0
score, move = minimax(game, depth, True)
print("Minimax nodos visitados:", node_counter)
        
        