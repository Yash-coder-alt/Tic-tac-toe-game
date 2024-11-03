import random

# Tic Tac Toe game in Python with Score Tracking and Computer Opponent

# Initialize the game board as a list of empty spaces
board = [' ' for _ in range(9)]
# Dictionary to store scores for Player X, Computer (O), and Ties
scores = {"X": 0, "O": 0, "Ties": 0}


# Function to print the current state of the board in a 3x3 format
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


# Function to check if there is a winner
def check_winner(player):
    # Define all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    # Check if any winning combination is met by the current player
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


# Function to check if the board is full, indicating a tie if no winner
def is_board_full():
    return ' ' not in board


# Function to reset the board to start a new game
def reset_board():
    global board
    board = [' ' for _ in range(9)]


# Function to display the current score of both players and ties
def display_score():
    print("\nScores:")
    print(f"Player X: {scores['X']}")
    print(f"Computer (O): {scores['O']}")
    print(f"Ties: {scores['Ties']}")
    print("\n")


# Function to handle the computer's move by selecting a random available spot
def computer_move():
    # Get a list of available spots on the board
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    # Randomly choose a move from the available spots
    move = random.choice(available_moves)
    # Place the computer's mark ('O') on the chosen spot
    board[move] = 'O'
    print("Computer has made its move:")
    print_board()


# Main function to control the game flow
def play_game():
    print("Welcome to Tic Tac Toe with Score Tracking and Computer Opponent!")

    current_player = 'X'  # Player X starts the game

    # Game loop to allow continuous play
    while True:
        print_board()

        # Player X's turn
        if current_player == 'X':
            try:
                # Get the player's move and adjust for 0-based index
                move = int(input("Player X, enter a position (1-9): ")) - 1
                # Validate the move
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            # Place the player's mark ('X') on the board
            board[move] = 'X'

        # Computer's turn
        else:
            computer_move()

        # Check if the current player has won
        if check_winner(current_player):
            print_board()
            if current_player == 'X':
                print("Player X wins!")
                scores['X'] += 1  # Update Player X's score
            else:
                print("Computer (O) wins!")
                scores['O'] += 1  # Update Computer's score
            display_score()
            # Ask if players want to play again
            if input("Play again? (y/n): ").lower() != 'y':
                break
            reset_board()  # Reset board for new game
            current_player = 'X'  # Reset to player 'X' for the new game
            continue

        # Check if the game is a tie
        if is_board_full():
            print_board()
            print("It's a tie!")
            scores["Ties"] += 1  # Update Tie score
            display_score()
            # Ask if players want to play again
            if input("Play again? (y/n): ").lower() != 'y':
                break
            reset_board()  # Reset board for new game
            current_player = 'X'  # Reset to player 'X' for the new game
            continue

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


# Run the game
play_game()
