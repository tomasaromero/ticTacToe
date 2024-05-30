import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 600, 600
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BLACK)

# Draw the board
def draw_board():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

# Draw X and O
def draw_xo(row, col, player):
    center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        pygame.draw.line(screen, WHITE, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (center_x + 50, center_y - 50), (center_x - 50, center_y + 50), LINE_WIDTH)
    elif player == 2:
        pygame.draw.circle(screen, WHITE, (center_x, center_y), 50, LINE_WIDTH)

# Check for a winner
def check_winner(board):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == 1 for j in range(BOARD_SIZE)) or all(board[j][i] == 1 for j in range(BOARD_SIZE)):
            return 1  # Player 1 wins

        if all(board[i][j] == 2 for j in range(BOARD_SIZE)) or all(board[j][i] == 2 for j in range(BOARD_SIZE)):
            return 2  # Player 2 wins

    # Check diagonals
    if all(board[i][i] == 1 for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == 1 for i in range(BOARD_SIZE)):
        return 1  # Player 1 wins

    if all(board[i][i] == 2 for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == 2 for i in range(BOARD_SIZE)):
        return 2  # Player 2 wins

    return 0  # No winner yet

# Main game loop
def main():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    turn = 1  # Player 1 starts

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE

                if board[row][col] == 0:
                    board[row][col] = turn
                    draw_xo(row, col, turn)
                    winner = check_winner(board)

                    if winner:
                        print(f"Player {winner} wins!")
                        pygame.time.delay(2000)
                        
                        pygame.quit()
                        sys.exit()

                    turn = 3 - turn  # Switch player

        draw_board()
        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    main()
