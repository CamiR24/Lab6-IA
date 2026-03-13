import numpy as np

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
    
    # def evaluate(self): #función para definir que valor devuelve dependiendo si gana, pierde o empata. NO SIRVE CUANDO SE CORTA EN PROFUNDIDAD 5 O 6
    #     if self.check_winner(1):
    #         return 1000
    #     elif self.check_winner(-1):
    #         return -1000
    #     else:
    #         return 0       

    def evaluate_window(self, window, player):
        score = 0
        opponent = -player

        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(0) == 2:
            score += 2
        
        if window.count(opponent) == 3 and window.count(0) == 1:
            score -=4

        return score
    
    #función para definir que valor devuelve dependiendo si gana, pierde o empata.
    #Evalúa que tan buena es una posición
    def evaluate(self): 
        if self.check_winner(1):
            return 1000
        elif self.check_winner(-1):
            return -1000

        score = 0
        player = 1

        center_array = list(self.board[:, COLS//2]) # Control del centro
        center_count = center_array.count(player)
        score += center_count * 3

        for r in range(ROWS):         # Evaluar horizontales
            row_array = list(self.board[r, :])
            for c in range(COLS - 3):
                window = row_array[c:c+4]
                score += self.evaluate_window(window, player)

        for c in range(COLS):         # Evaluar verticales
            col_array = list(self.board[:, c])
            for r in range(ROWS - 3):
                window = col_array[r:r+4]
                score += self.evaluate_window(window, player)

        for r in range(ROWS - 3):         # Diagonales positivas
            for c in range(COLS - 3):
                window = [self.board[r+i][c+i] for i in range(4)]
                score += self.evaluate_window(window, player)

        for r in range(3, ROWS):         # Diagonales negativas
            for c in range(COLS - 3):
                window = [self.board[r-i][c+i] for i in range(4)]
                score += self.evaluate_window(window, player)

        return score