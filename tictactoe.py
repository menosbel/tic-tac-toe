# me permite llamar la funcion randint()
import random

def drawBoard(board):
    # crear el tablero
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')



def inputPlayerLetter():
    # el jugador elige que letra quiere ser
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('¿Querés ser X u O?')
        letter = input().upper()
    # la primera letra corresponde al jugador y la segunda  a la compu
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # quien va primero se decide aleatoriamente
    if random.randint(0, 1) == 0:
        return 'computadora'
    else:
        return 'jugadore'


def playAgain():
    # devuelve true si el jugador quiere volver a jugar y false si no quiere
    print('¿Querés volver a jugar? (sí / no)')
    return input().lower().startswith('s')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(board, letter):
    # devuelve true si el jugador gano
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # primera horizontal
            (board[4] == letter and board[5] == letter and board[6] == letter) or # segunda horizontal
            (board[1] == letter and board[2] == letter and board[3] == letter) or # tercera horizontal
            (board[7] == letter and board[4] == letter and board[1] == letter) or # primera vertical
            (board[8] == letter and board[5] == letter and board[2] == letter) or # segunda vertical
            (board[9] == letter and board[6] == letter and board[3] == letter) or # tercera vertical
            (board[7] == letter and board[5] == letter and board[3] == letter) or #diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter)) #diagonal


def getBoardCopy(board):
    # hacer un duplicado de la lista del tablero y devolver el duplicado
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isSpaceFree(board, move):
    # devuelve true si el movimiento esta libre en el tablero
    return board[move] == ' '


def getPlayerMove(board):
    # el jugador ingresa su movimiento
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('¿Cuál es tu siguiente jugada? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # devuelve los movimientos posibles
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # dado el tablero y la letra de la compu, dterminar a donde moverse
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # la compu chequea si puede ganar
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # se fija si el jugador puede ganar en el siguiente movimiento
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # trata de ocupar una de las esquinas
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # trata de ocupar el centro
    if isSpaceFree(board, 5):
        return 5

    # ocupa uno de los lados
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # devuelve true si estan ocupados todos los espacios del tablero
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# Empieza el juego
print('Bienvenido al ta te ti')

while True:
    # resetea el tablero
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn.capitalize() + ', empezás.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'jugadore':
            # turno del jugador
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('¡Ganaste!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empataron.')
                    break
                else:
                    turn = 'computadora'

        else:
            # turno de la compu
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('La computadora ganó el juego. Perdiste.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Empataron.')
                    break
                else:
                    turn = 'jugadore'

    if not playAgain():
        break