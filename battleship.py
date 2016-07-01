from random import randint

def play():
    board = []
    ships_sunk = 0

    for x in range(5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print " ".join(row)

    print  ""
    print  ""

    print "Let's play Battleship!"

    print  ""

    print "Try and sink the 2 ships!"

    print  ""
    print_board(board)
    print  ""


    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship1_row = random_row(board)
    ship1_col = random_col(board)

    ship2_row = random_row(board)
    ship2_col = random_col(board)

    while ship1_row == ship2_row:
        ship2_row = random_row(board)

    while ship1_col == ship2_col:
        ship2_col = random_col(board)

    for turn in range(10):
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
        if guess_row == ship1_row and guess_col == ship1_col or guess_row == ship2_row and guess_col == ship2_col:
            print  ""
            print "Congratulations! You sunk my battleship!"
            board[guess_row][guess_col] = "S"
            ships_sunk += 1
            print ships_sunk
            if ships_sunk == 2:
                print  ""
                print "Congratulations! You won!!!"
                break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print  ""
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print  ""
                print "You guessed that one already."
            else:
                print  ""
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
            if turn == 9:
                print  ""
                print "Game Over"
                break
            print turn + 1
        print ""
        print_board(board)

play()
