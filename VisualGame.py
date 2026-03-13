import pygame
import sys
import math
from Connect4 import Connect4
from AlphaBeta import minimax_ab
from RandomAgent import random_move

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

pygame.init()

font = pygame.font.SysFont("monospace", 50)
small_font = pygame.font.SysFont("monospace", 30)

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4 - AlphaBeta AI")

def animate_drop(game, col, player):

    row_to_place = None

    # Encontrar la fila donde caerá la ficha
    for r in reversed(range(ROW_COUNT)):
        if game.board[r][col] == 0:
            row_to_place = r
            break

    # Animación bajando
    for r in range(row_to_place + 1):
        draw_board(game)

        pygame.draw.circle(
            screen,
            RED if player == 1 else YELLOW,
            (int(col*SQUARESIZE + SQUARESIZE/2),
             int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)),
            40
        )

        pygame.display.update()
        pygame.time.wait(50)

    # Ahora sí colocamos la pieza real
    game.drop_piece(col, player)

def draw_board(game):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK,
                               (int(c*SQUARESIZE+SQUARESIZE/2),
                                int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),
                               40)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if game.board[r][c] == 1:
                pygame.draw.circle(screen, RED,
                    (int(c*SQUARESIZE+SQUARESIZE/2),
                     height-int((ROW_COUNT-r-0.5)*SQUARESIZE)), 40)
            elif game.board[r][c] == -1:
                pygame.draw.circle(screen, YELLOW,
                    (int(c*SQUARESIZE+SQUARESIZE/2),
                     height-int((ROW_COUNT-r-0.5)*SQUARESIZE)), 40)

    pygame.display.update()


#Juego contra random (máquina) o humano
def play_game(vs_random=True):

    game = Connect4()
    turn = 0   # 0 = humano/random, 1 = AI
    game_over = False
    nodes = 0

    draw_board(game)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Humano juega
            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0 and not vs_random:
                col = int(event.pos[0] / SQUARESIZE)

                if col in game.actions():
                    animate_drop(game, col, -1)
                    turn = 1

        # Random juega
        if turn == 0 and vs_random and not game_over:
            col = random_move(game)
            pygame.time.wait(300)
            animate_drop(game, col, -1)
            turn = 1

        # AI juega
        if turn == 1 and not game_over:
            score, col, nodes = minimax_ab(game, 5, -math.inf, math.inf, True)

            pygame.time.wait(300)
            animate_drop(game, col, 1)
            turn = 0

        draw_board(game)

        # Mostrar info
        info_text = small_font.render(f"Depth: 5  |  Nodes: {nodes}", True, (255,255,255))
        screen.blit(info_text, (10,10))
        pygame.display.update()

        # Revisar ganador
        if game.check_winner(1):
            label = font.render("AI WINS!", True, RED)
            screen.blit(label, (40,10))
            pygame.display.update()
            game_over = True

        elif game.check_winner(-1):
            label = font.render("YOU WIN!", True, YELLOW)
            screen.blit(label, (40,10))
            pygame.display.update()
            game_over = True

        elif len(game.actions()) == 0:
            label = font.render("DRAW!", True, (255,255,255))
            screen.blit(label, (40,10))
            pygame.display.update()
            game_over = True

    # Mantener ventana abierta
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    play_game(vs_random=True)  # vs random
    #play_game(vs_random=False)  # vs humano