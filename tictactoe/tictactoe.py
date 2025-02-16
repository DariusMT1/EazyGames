import os
import random

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    return None

def is_draw(board):
    return all(cell != " " for cell in board)

def remove_random_moves(board):
    filled_positions = [i for i, cell in enumerate(board) if cell != " "]
    if len(filled_positions) >= 3:
        positions_to_clear = random.sample(filled_positions, 3)
        for pos in positions_to_clear:
            board[pos] = " "

def tictactoe():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn. Enter a position (1-9):")

        try:
            position = int(input()) - 1
            if position < 0 or position >= 9 or board[position] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        board[position] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins! Congratulations!")
            break

        if is_draw(board):
            remove_random_moves(board)

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        tictactoe()
        print("Do you want to play again? (y/n):")
        if input().lower() != 'y':
            print("Thanks for playing!")
            break
