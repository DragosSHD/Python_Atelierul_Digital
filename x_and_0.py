import random

game_board = [0 for i in range(10)]  # initialize by 10 zeros


# Check if a position is already taken on the board.
def pos_is_taken(crt_pos):
    if game_board[crt_pos] == 0:
        return False
    return True


def get_user_input():
    while True:
        crt_input = input("Enter position:")
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


# Here we decide which players gets to place first.
def who_starts():
    if random.randint(0, 1) == 0:
        print("Player 1 gets to start the game!")
        return 1
    else:
        print("Player 2 gets to start the game!")
        return 0


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
            print("Great you chose: ", p1_choice)
        else:
            p2_choice = 2
            game_board[p2_choice] = 2
            print("P2 chose ", p2_choice)
        round_count += 1
