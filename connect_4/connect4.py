from typing import Union


def checkWin(board) -> bool:
    win = False
    for row in board:
        if checkRowWin(row):
            win = True

    if checkColWin(board):
        win = True

    if checkDiagonalWin(board):
        win = True

    return win


def checkRowWin(row) -> bool:
    win = False
    for i in range(len(row) - 3):
        if (
            row[i] != '' and
            row[i] == row[i+1] and
            row[i+1] == row[i+2] and
            row[i+2] == row[i+3]
        ):
            win = True

    return win


def checkColWin(board) -> bool:
    # Count how many cols in a row match
    matchCounter = 0
    prevColSquare = ''
    for colNo in range(len(board[0])):
        for row in board:
            # check counter b4 if so if there is already a match
            # it doesn't reset back to 0
            if matchCounter >= 3:
                return True
            if (
                row[colNo] != '' and
                row[colNo] == prevColSquare
            ):
                matchCounter += 1
            else:
                matchCounter = 0
            prevColSquare = row[colNo]

        # for last row last column
        if matchCounter >= 3:
            return True

        # reset and check next col
        prevColSquare = ''

    return False


def checkDiagonalWin(board) -> bool:
    win = False
    # check downwards diagonals
    for colNo in range(len(board[0]) - 3):
        for rowNo in range(len(board) - 3):
            if (
                board[rowNo][colNo] != '' and
                board[rowNo][colNo] == board[rowNo+1][colNo+1] and
                board[rowNo+1][colNo+1] == board[rowNo+2][colNo+2] and
                board[rowNo+2][colNo+2] == board[rowNo+3][colNo+3]
            ):
                win = True

    # check upwards diagonals
    for colNo in range(len(board[0])-3):
        for rowNo in range(len(board)-1, 2, -1):  # 2 to skip first 3 rows
            if (
                board[rowNo][colNo] != '' and
                board[rowNo][colNo] == board[rowNo-1][colNo+1] and
                board[rowNo-1][colNo+1] == board[rowNo-2][colNo+2] and
                board[rowNo-2][colNo+2] == board[rowNo-3][colNo+3]
            ):
                win = True

    return win


def placePiece(board: 'list[list[str]]', colour: str, col: int) -> 'list[list[str]]':
    newBoard = board.copy()
    for rowNo in range(len(board)-1, -1, -1):
        if board[rowNo][col-1] == '':
            newBoard[rowNo][col-1] = colour
            return newBoard

    # Raise error if whole col is occupied
    raise ValueError


def printBoard(board: 'list[list[str]]'):
    print()
    for row in board:
        print([" " if square == '' else square for square in row])


board = [
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
    ['', '', '', '', '', '', ''],
]
turn = 'Y'

while True:

    printBoard(board)
    while True:
        userInput = input("{0}'s turn, please enter the row: ".format(turn))
        col = int(userInput)
        if col >= 1 and col <= 7:
            break
        else:
            print("Please enter valid row")

    try:
        board = placePiece(board, turn, col)
    except:
        print("Column is full!")

    if checkWin(board):
        printBoard(board)
        print("{0} has won!".format(turn))
        break

    if turn == 'Y':
        turn = 'R'
    else:
        turn = 'Y'
