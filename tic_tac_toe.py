board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
game_not_over = True
player = "X"
winner = None

def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def turn_handler(symbol):
    global player
    print(player + "'s Turn,")
    position = input("Enter the position (1-9): ")
    if position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print("Try a valid Position")
        turn_handler(symbol)
    else:
        position = int(position) - 1
        if board[position] == '-':
            board[position] = symbol
        else:
            print("Position already Occupied! TRY AGAIN")
            turn_handler(symbol)

def play_game():
    global winner
    show_board()
    while game_not_over:
        turn_handler(player)
        show_board()
        is_game_over()
        flip_player()

        if winner == 'O' or winner == 'X':
            print(winner + " is the winner")
        elif winner is None and is_tie():
            print("Tie")

def is_row_won():
    global winner
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        return True

    return False

def is_col_won():
    global winner
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        return True

    return False

def is_diag_won():
    global winner
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        return True

    return False

def is_won():
    return is_row_won() or is_col_won() or is_diag_won()

def is_tie():
    return '-' not in board and not is_won()

def flip_player():
    global player
    player = 'O' if player == 'X' else 'X'

def is_game_over():
    global winner
    if is_won() or is_tie():
        game_not_over = False
        winner = player

# START PLAYING!!!
play_game()
