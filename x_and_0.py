import random

game_board = [0 for i in range(10)]  # initialize by 10 zeros


# Check if a position is already taken on the board.
def pos_is_taken(crt_pos):
    if game_board[crt_pos] == 0:
        return False
    return True


# Function meant to manage the user input.
def get_user_input():
    while True:
        crt_input = input("Enter position:")
        if crt_input == 'exit':
            exit()
        if not crt_input.isnumeric():
            print("The position has to be a number!")
            continue
        crt_input = int(crt_input)
        if crt_input < 1 or crt_input > 9:
            print("The position has to be between 1 and 9!")
            continue
        if pos_is_taken(crt_input):
            print("The position is already taken!")
            continue
        return crt_input


def get_robot_input(difficuly):
    if difficuly == 'easy':  # positions are chosen at random
        while True:
            crt_generated = random.randint(1, 9)
            if not pos_is_taken(crt_generated):
                return crt_generated


# Here we decide which player gets to place first.
def who_starts():
    if random.randint(0, 1) == 0:
        print("Player 1 gets to start the game!")
        return 1
    else:
        print("Player 2 gets to start the game!")
        return 0


def check_winner(crt_player):
    for i in range(1, 4):  # search on columns
        if game_board[i] == crt_player and game_board[i+3] == crt_player and game_board[i+6] == crt_player:
            return True
    for i in [1, 4, 7]:  # search on rows
        if game_board[i] == crt_player and game_board[i+1] == crt_player and game_board[i+2] == crt_player:
            return True
    if game_board[5] != crt_player:  # easy exclusion search for diagonals
        return False
    if game_board[1] == crt_player and game_board[5] == crt_player and game_board[9] == crt_player:  # search on
        return True                                                                                  # first diagonal
    if game_board[3] == crt_player and game_board[5] == crt_player and game_board[7] == crt_player:  # search on
        return True                                                                                  # second diagonal
    return False




# This is the main method of this program. Here is where the action takes place...
def play_x_and_0():
    print("Hi! Good luck trying to win in this glorious game!"
          "\nYour are Player 1 and your opponent is Player 2.")
    p1_won = False
    p2_won = False
    round_count = 1
    p1_starts = who_starts()

    while p1_won is False and p2_won is False:
        if round_count % 2 == p1_starts:
            p1_choice = get_user_input()
            game_board[p1_choice] = 1
            print("Great! You chose: ", p1_choice)
        else:
            p2_choice = get_robot_input('easy')
            game_board[p2_choice] = 2
            print("P2 chose ", p2_choice)
        round_count += 1
        if round_count >= 3:
            p1_won = check_winner(1)
            p2_won = check_winner(2)
        if round_count >= 9:
            print(round_count)
            break

    if p1_won:
        print("Congratulations, you won!")
    elif p2_won:
        print("Too bad... you've been defeated!")
    else:
        print("We have a draw this time.")


    # Template for how it'll be drawn at the end:
    #
    #      |     |
    #   x  |  o  |  x
    # _____|_____|_____
    #      |     |
    #   o  |  o  |  x
    # _____|_____|_____
    #      |     |
    #   x  |  x  |  o
    #      |     |

