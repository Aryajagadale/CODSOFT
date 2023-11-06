import random

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Define winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Function to check if a player has won
def check_win(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to make a move for the AI using Minimax
def ai_move(board, ai_player, human_player):
    if ai_player == 'X':
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(board, 0, False, ai_player, human_player)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
    else:
        best_score = float('inf')
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(board, 0, True, ai_player, human_player)
                board[i] = ' '
                if score < best_score:
                    best_score = score
                    best_move = i
    return best_move

# Minimax algorithm
def minimax(board, depth, is_maximizing, ai_player, human_player):
    if check_win(board, ai_player):
        return 1
    if check_win(board, human_player):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(board, depth + 1, False, ai_player, human_player)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = human_player
                score = minimax(board, depth + 1, True, ai_player, human_player)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Main game loop
def play_game():
    ai_player = 'X'
    human_player = 'O'
    current_player = ai_player

    while True:
        display_board(board)

        if current_player == ai_player:
            print("AI's turn:")
            ai_move_index = ai_move(board, ai_player, human_player)
            board[ai_move_index] = ai_player

            if check_win(board, ai_player):
                display_board(board)
                print("AI wins!")
                break
            if is_board_full(board):
                display_board(board)
                print("It's a tie!")
                break
            current_player = human_player
        else:
            print("Your turn (0-8):")
            try:
                human_move_index = int(input())
                if 0 <= human_move_index <= 8 and board[human_move_index] == ' ':
                    board[human_move_index] = human_player

                    if check_win(board, human_player):
                        display_board(board)
                        print("You win!")
                        break
                    if is_board_full(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    current_player = ai_player
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

# Start the game
play_game()
