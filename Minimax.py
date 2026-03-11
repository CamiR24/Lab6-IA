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