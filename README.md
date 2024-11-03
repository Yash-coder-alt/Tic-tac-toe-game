Explanation of Each Part

Initialize the Board and Scores:
board is a list of 9 spaces representing the 3x3 Tic-Tac-Toe grid.
scores dictionary tracks wins for Player X, wins for the Computer (O), and ties.

Display Board:
print_board() function displays the current state of the board.

Check Winner:
check_winner() checks for winning combinations on the board. It returns True if any of the winning combinations are matched by the current player.

Check Full Board:
is_board_full() returns True if there are no empty spaces left, indicating a tie.

Reset Board:
reset_board() clears the board by reinitializing it with empty spaces for a new game.

Display Score:
display_score() shows the current win counts for Player X, Computer O, and the number of tied games.

Computer Move:
computer_move() selects a random available spot for the computer’s move.

Game Flow:
In play_game(), the game alternates turns between the player and the computer. After each move, it checks for a winner or a tie, updates the score accordingly, and offers the option to replay.

This code provides a straightforward way for a player to enjoy multiple rounds against a computer opponent while tracking scores!
