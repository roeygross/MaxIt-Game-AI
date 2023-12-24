'''
game.py
===============================================
game.py contains all MAXIT propeties and functions (backend)
The game board is a matrix of 8x8 with randomised ints, Empty cells = 99
The matrix contains in the eighth row data about the game:
board[8][0] - Who's turn is it: HUMAN or COMPUTER
board[8][1] - The last move made
board[8][2] - The heuristic value of the state
board[8][3] - Human score
board[8][4] - AI score
'''


import copy
import numpy as np
COMPUTER=4 #Numerical representation of the ASCII value of "COMPUTER"
HUMAN=1 #Numerical representation of the ASCII value of "HUMAN"

def lastTurn(board):
    #returns what is the last move that have been made
    return board[8][1]

def HumScore(board):
    #returns the human score
    return board[8][3]
def CompScore(board):
    #returns the computer score
    return board[8][4]
def value(s):
    #returns the heuristic value of a state
    return s[8][2]
def isHumTurn(s):
#Returns True iff it the human's turn to play
    if s[8][0] == HUMAN:
        return 1

def isFinished(board):
    # Returns True iff the game ended
    isHum=isHumTurn(board)
    row = lastTurn(board)
    #check if there is any left available moves
    rowsum=0
    colsum=0
    if isHum: #row turn -check if row is full
        for i in range(8):
            if board[row][i]==99:
                rowsum+=1
        if rowsum==8: #no available moves left
            return 1
    if not isHum: #col turn - check if col is full
        col=row
        for i in range(8):
            if board[i][col] == 99:
                colsum += 1
        if colsum == 8: #no available moves left
            return 1
    return 0
def create():
#Returns an initialized board.
    board = [[0 for x in range(8)] for y in range(9)] #creats a 0 valued board of 9x8
    board = np.random.randint(-9,15,size=(9,8))  #fill the board of 9x8  with random numbers ranged -9 -> 15
    a=HUMAN
    board[8][0] =a #who's turn it is
    board[8][1] = np.random.randint(0, 7)  # initial game row
    board[8][2] = 0.00001  # initial heuristic value
    board[8][3] = board[8][4] = 0  # initial scores

    return board

def inputMove(s, number):
# Reads, enforces legality and executes the user's move.
    isHum=isHumTurn(s)
    #gets input
    row = lastTurn(s)
    move=number
    if s[row][move]==99:
        return -1
    else:
        makeMove(s, move)
        return 1

def makeMove(board, move):
    # puts 99 in chosen place
    # switches turns
    # re-evaluates the heuristic value.
    # Assumes the move is legal.

    isHum=isHumTurn(board)
    row = lastTurn(board)

    if isHum:  #row turn
        if isHum:
            board[8][3] += board[row][move] #add to Human score
            board[row][move] = 99
        else:
            board[8][4] += board[row][move] #add to Computer score
            board[row][move] = 99

    elif not isHum: #col turn
        col=row
        if isHum:
            board[8][3] += board[move][col] #add to Human score
            board[move][col] = 99
        else:
            board[8][4] += board[move][col] #add to Computer score
            board[move][col] = 99

    board[8][0] = COMPUTER + HUMAN - board[8][0]  # switch turn
    board[8][1] = move #puts move in last move
    board[8][2] = board[8][4] - board[8][3] #calculate heuristic value
    # Explaination for heuristic value:
    # The AI algorithm wants to choose the highest value possible,  while letting the human get the lowest possible score
    # The heuristic value of a state just refers to a state as a 0-sum situation!
    # More points for AI and fewer points for human will give a state with a higher heuristic value
    # This way the minimax algorithm will work perfect, especially in high depths,
    # It'll choose the route of moves of AI that will give the highest difference between AI and Human

# returns a list of the next states of s
# will contain all available next states and will sort them by heuristic value
def getNext(s):
    isHum=isHumTurn(s)
    ns=[]
    currRow = s[8][1]
    if isHum: #row turn
        for col in range(8):
            if s[currRow][col] != 99:
                tmp=copy.deepcopy(s)
                makeMove(tmp,col)
                ns += [tmp]
    elif not isHum: #col turn
        currCol=currRow
        for row in range(8):
            if s[row][currCol] != 99:
                tmp = copy.deepcopy(s)
                makeMove(tmp, row)
                ns += [tmp]
 #sort by heuristic value
    #sorting the states will make the a-b-prunning faster
    if isHum:
        ns.sort(key=value)
    else:
        ns.sort(key=value,reverse=True)
    return ns

