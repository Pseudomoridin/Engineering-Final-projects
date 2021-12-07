import random

# Tic-Tac-Toe Game Against A Computer

# Prints the board for the game to console output
def drawBoard():
    print("   | 1 | 2 | 3 ")
    print('---------------')
    print(' 1 | ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------------')
    print(' 2 | ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------------')
    print(' 3 | ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# Lets the player decide which symbol (X or O) he wants to be
def pickSymbol():
    symbol = ' '

    while not (symbol == 'X' or symbol == 'O'):
        print('Do you want to be symbol X, or the symbol O?')
        symbol = input().upper()

    # Return a list containing the player's symbol (first element) and the computer's symbol (second element)
    if symbol == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# Randomly determines if the player or the computer goes first
def pickFirst():
    if random.randint(0,1) == 0:
        return 'player'
    else:
        return 'computer'

# Checks that the x-coordinate the player chose is valid
def isValidX(x):
    try:
        intX = int(x)
        if not 1 <= intX <= 3:
            raise ValueError()
    except ValueError:
        return False

    return True

# Checks that the y-coordinate the player chose is valid
def isValidY(y):
    try:
        intY = int(y)
        if not 1 <= intY <= 3:
            raise ValueError()
    except ValueError:
        return False

    return True

# Converts a player's input coordinates to a move
def convertCoordinates(x, y):
    if x == 1:
        if y == 1:
            return 7
        elif y == 2:
            return 8
        else:
            return 9
    elif x == 2:
        if y == 1:
            return 4
        elif y == 2:
            return 5
        else:
            return 6
    else:
        if y == 1:
            return 1
        elif y == 2:
            return 2
        else:
            return 3

# Checks if a space for a given move is free
def isFree(move):
    return board[move] == ' '

# Gets the player's move
def getPlayerMove():
    while True:
        x = ' ' # arbitrary initial value before player input
        while not isValidX(x):
            print('Enter input x:')
            x = input()

        y = ' ' # arbitrary initial value before player input
        while not isValidY(y):
            print('Enter input y:')
            y = input()

        move = convertCoordinates(int(x),int(y))
        if not isFree(move):
            print('That space is taken. Please enter a different coordinate')
            continue
        else:
            break

    return move

# Gets the computer's move
def getComputerMove():
    return 9

# Places the move onto the board
def placeMove(move, sym):
    board[move] = sym

# Determines if the board is in a win state for a given symbol
def isWin(sym):
    return ((board[7] == sym and board[8] == sym and board[9] == sym) or # top
        (board[4] == sym and board[5] == sym and board[6] == sym) or     # middle    
        (board[1] == sym and board[2] == sym and board[3] == sym) or     # bottom
        (board[7] == sym and board[5] == sym and board[3] == sym) or     # diagonal
        (board[1] == sym and board[5] == sym and board[9] == sym) or     # diagonal
        (board[7] == sym and board[4] == sym and board[1] == sym) or     # left
        (board[8] == sym and board[5] == sym and board[2] == sym) or     # center
        (board[9] == sym and board[6] == sym and board[3] == sym))       # right

# Determines if the board is in a tie state
def isTie():
    return board.count('X') + board.count('O') == 9

# Prints the final output if the game is in a tie state
def tie():
    drawBoard()
    print('The game has ended in a tie.')

# Prints the final output if the game is in a win state for the PLAYER
def playerWin():
    drawBoard()
    print('Congratulations! You beat the computer!')

# Prints the final output if the game is in a win state for the COMPUTER
def computerWin():
    drawBoard()
    print('Sorry... the computer beat you.')

# The player makes a move
def playerTurn(playerSym):
    move = getPlayerMove()
    placeMove(move, playerSym)

# The computer makes a move
def computerTurn(computerSym):
    move = getComputerMove()
    placeMove(move, computerSym)

def tttmain():
    print("Welcome to Tic-Tac-Toe!")
    playerSym, computerSym = pickSymbol()
    turn = pickFirst()
    print("The " + turn + " will play first.")
    global board
    board = [' '] * 10

    while True:
        if turn == 'player':
            drawBoard()
            playerTurn(playerSym)
            if isWin(playerSym):
                playerWin()
                break
            if isTie():
                tie()
                break
            turn = 'computer'
        if turn == 'computer':
            drawBoard()
            computerTurn(computerSym)
            if isWin(computerSym):
                computerWin()
                break
            if isTie():
                tie()
                break
            turn = 'player'
