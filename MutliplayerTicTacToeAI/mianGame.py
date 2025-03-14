import random

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Initialize board
def create_board():
    return [[EMPTY] * 3 for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if the board is full
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Check for a win
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Get available moves
def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

# Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return -1
    if check_winner(board, PLAYER_O):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for r, c in available_moves(board):
            board[r][c] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[r][c] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for r, c in available_moves(board):
            board[r][c] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[r][c] = EMPTY
            best_score = min(best_score, score)
        return best_score

# AI Move using Minimax
def ai_move(board):
    best_score = -float("inf")
    best_move = None
    for r, c in available_moves(board):
        board[r][c] = PLAYER_O
        score = minimax(board, 0, False)
        board[r][c] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

# Player move
def player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter row and column (e.g., 1 2): ")
            r, c = map(int, move.split())
            if board[r][c] == EMPTY:
                board[r][c] = player
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column between 0 and 2.")

# Main game loop
def play_game():
    board = create_board()
    mode = input("Choose mode: 1 (Multiplayer) or 2 (Play against AI): ").strip()

    while True:
        print_board(board)

        if mode == "1":  # Multiplayer Mode
            player_move(board, PLAYER_X)
            if check_winner(board, PLAYER_X):
                print_board(board)
                print("Player X wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            print_board(board)
            player_move(board, PLAYER_O)
            if check_winner(board, PLAYER_O):
                print_board(board)
                print("Player O wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

        elif mode == "2":  # Single Player Mode (vs AI)
            player_move(board, PLAYER_X)
            if check_winner(board, PLAYER_X):
                print_board(board)
                print("You win!")
                break
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            print("AI is thinking...")
            r, c = ai_move(board)
            board[r][c] = PLAYER_O

            if check_winner(board, PLAYER_O):
                print_board(board)
                print("AI wins! Try again.")
                break
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

        else:
            print("Invalid mode selected. Exiting game.")
            break

# Run the game
if __name__ == "__main__":
    play_game()