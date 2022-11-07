import copy
from msilib import sequence
import numpy as np
import random
from termcolor import colored  # can be taken out if you don't like it...

# # # # # # # # # # # # # # global values  # # # # # # # # # # # # # #
ROW_COUNT = 6
COLUMN_COUNT = 7

RED_CHAR = colored('X', 'red')  # RED_CHAR = 'X'
BLUE_CHAR = colored('O', 'blue')  # BLUE_CHAR = 'O'

EMPTY = 0
RED_INT = 1
BLUE_INT = 2


# # # # # # # # # # # # # # functions definitions # # # # # # # # # # # # # #

def create_board():
    """creat empty board for new game"""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
    return board


def drop_chip(board, row, col, chip):
    """place a chip (red or BLUE) in a certain position in board"""
    board[row][col] = chip


def is_valid_location(board, col):
    """check if a given column in the board has a room for extra dropped chip"""
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    """assuming column is available to drop the chip,
    the function returns the lowest empty row  """
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    """print current board with all chips put in so far"""
    # print(np.flip(board, 0))
    print(" 1 2 3 4 5 6 7 \n" "|" + np.array2string(np.flip(np.flip(board, 1)))
          .replace("[", "").replace("]", "").replace(" ", "|").replace("0", "_")
          .replace("1", RED_CHAR).replace("2", BLUE_CHAR).replace("\n", "|\n") + "|")

def game_is_won(board, chip):
    '''Check for 4 in a row'''


    winning_Sequence = np.array([chip, chip, chip, chip])
    # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board[r, :]))):
            return True
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board[:, c]))):
            return True
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, board.diagonal(offset)))):
            return True
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, winning_Sequence))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            return True

def three_in_a_row(board, chip):
    '''Count 3-in-a-rows'''
    count = 0
    sequence_1 = np.array([EMPTY, chip, chip, chip])
    sequence_2 = np.array([chip, EMPTY, chip, chip])
    sequence_3 = np.array([chip, chip, EMPTY, chip])
    sequence_4 = np.array([chip, chip, chip, EMPTY])

    # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, board[r, :]))):
            count+=1
     # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, board[r, :]))):
            count+=1
     # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, board[r, :]))):
            count+=1
     # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, board[:, c]))):
            count+=1
     # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, board[:, c]))):
            count+=1
     # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, board[:, c]))):
            count+=1
     # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
     # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
     # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
     # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    return count

def two_in_a_row(board, chip):
    '''Count 2-in-a-rows'''
    count = 0
    sequence_1 = np.array([EMPTY, EMPTY, chip, chip])
    sequence_2 = np.array([EMPTY, chip, EMPTY, chip])
    sequence_3 = np.array([EMPTY, chip, chip,EMPTY])
    sequence_4 = np.array([chip, EMPTY,EMPTY,chip])
    sequence_5 = np.array([chip,EMPTY, chip, EMPTY])
    sequence_6 = np.array([chip, chip, EMPTY, EMPTY])

    # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, board[r, :]))):
            count+=1
     # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, board[r, :]))):
            count+=1
     # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_5))) in "".join(list(map(str, board[r, :]))):
            count+=1
     # Check horizontal sequences
    for r in range(ROW_COUNT):
        if "".join(list(map(str, sequence_6))) in "".join(list(map(str, board[r, :]))):
            count+=1
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, board[:, c]))):
            count+=1
     # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, board[:, c]))):
            count+=1
     # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_5))) in "".join(list(map(str, board[:, c]))):
            count+=1
     # Check vertical sequences
    for c in range(COLUMN_COUNT):
        if "".join(list(map(str, sequence_6))) in "".join(list(map(str, board[:, c]))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_5))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check positively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_6))) in "".join(list(map(str, board.diagonal(offset)))):
            count+=1
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_1))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
     # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_2))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_3))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
     # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_4))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
     # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_5))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
     # Check negatively sloped diagonals
    for offset in range(-2, 4):
        if "".join(list(map(str, sequence_6))) in "".join(list(map(str, np.flip(board, 1).diagonal(offset)))):
            count+=1
    return count

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def MoveRandom(board, color):
    valid_locations = get_valid_locations(board)
    column = random.choice(valid_locations)   # you can replace with input if you like... -- line updated with Gilad's code-- thanks!
    row = get_next_open_row(board, column)
    drop_chip(board, row, column, color)

##########################
'''board = create_board()
print_board(board)
drop_chip(board,0,3,RED_INT)
drop_chip(board,2,1,RED_INT)
drop_chip(board,1,2,RED_INT)
drop_chip(board,3,0,BLUE_INT)
print(three_in_a_row(board,RED_INT))'''

class Game:
    def isFinished(self, s):
        return game_is_won(s,RED_INT) or game_is_won(s,BLUE_INT)#Not sure about whether this should be hard coded as red
    #Get heuristic value
    def value(self, s,color):
        otherColor = -2
        if color == RED_INT:
            otherColor = BLUE_INT
        else:
            otherColor = RED_INT
        val = 0
        #additive, blocks, wins
        if(game_is_won(s,color)):
            return 10000000
        if(game_is_won(s,otherColor)):
            return -10000001
        # +1 for each 2 pieces in a row by Player 1, -1 for each 2 pieces in a row by Player 2.
        val += two_in_a_row(s,color)
        val -= two_in_a_row(s,otherColor)
        # +10 for each 3 pieces in a row by Player 1, -500 for each 3 pieces in a row by Player 2.
        val += three_in_a_row(s,color)*10
        val -= three_in_a_row(s,otherColor)*500
        return val
    #Get all possible "neighboring" moves
    def getNext(self,s,chip):
        nextBoards = []
        for i in range(COLUMN_COUNT):
            if(is_valid_location(s,i)):
                curBoard = copy.deepcopy(s)
                row = get_next_open_row(s,i)
                drop_chip(curBoard,row,i,chip)
                nextBoards.append(curBoard)
        return nextBoards
game = Game()
class AB:
    #S = the state (max's turn)
    #d= max. depth of search
    #a, b= alpha and beta
    #returns [v, ns]: v= state s's value. ns = the state after recomennded move
    #if s is a terminal state ns=0.
    def abmax (self,s, d, a, b,color) :
        otherColor = -2
        if color == RED_INT:
            otherColor = BLUE_INT
        else:
            otherColor = RED_INT
        if d==0 or game.isFinished(s) :
            return [game.value(s,color), 0]
        v=float("-inf")
        ns=game.getNext(s,color)
        bestMove=0
        for i in ns:
            tmp=self.abmin (copy.deepcopy (i) , d-1,a, b,color)
            if tmp[0]>v:
                v=tmp[0]
                bestMove=i
            if v>=b:
                return [v,i]
            if v>a:
                a=v
        return [v,bestMove]

    def abmin (self, s, d, a, b,color) :
        otherColor = -2
        if color == RED_INT:
            otherColor = BLUE_INT
        else:
            otherColor = RED_INT
        if d==0 or game.isFinished(s) :
            return [game.value(s,color),0]
        v=float("inf")
        ns=game.getNext(s,otherColor)
        bestMove=0
        for i in ns:
            tmp=self.abmax(copy.deepcopy (i) , d-1,a, b,color)
            if tmp[0]<v:
                v=tmp[0]
                bestMove=i
            if v<=a:
                return [v,i]
            if v<b:
                b=v
        return [v,bestMove]

#tmp = copy.deepcopy(board)
# # # # # # # # # # # # # # main execution of the game # # # # # # # # # # # # # #
turn = 0

board = create_board()
print_board(board)
game_over = False
abPruning = AB()
def agent1(board,color):
    #Use AB Pruning + heiristics to get the state of the board after making the best move
    nextBoard = abPruning.abmax(board, 3, float("-inf"), float("inf"),BLUE_INT)[1]
    #Return column which I just placed my chip in
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            if nextBoard[i][j] != board[i][j]:
                return j
    return -1
while not game_over:
    if turn % 2 == 0:
        
        col = int(input("RED please choose a column(1-7): "))
        while col > 7 or col < 1:
            col = int(input("Invalid column, pick a valid one: "))
        while not is_valid_location(board, col - 1):
            col = int(input("Column is full. pick another one..."))
        col -= 1

        row = get_next_open_row(board, col)
        drop_chip(board, row, col, RED_INT)
        
    if turn % 2 == 1 and not game_over:
        #MoveRandom(board,BLUE_INT)
        ##Make this return col of move and dropchip()
        nextCol = agent1(board,BLUE_INT)
        nextRow = get_next_open_row(board,nextCol)
        drop_chip(board,nextRow,nextCol,BLUE_INT)
        #board = copy.deepcopy(abPruning.abmax(board, 1, float("-inf"), float("inf"),BLUE_INT))[1]

    print_board(board)
    
    if game_is_won(board, RED_INT):
        game_over = True
        print(colored("Red wins!", 'red'))
    if game_is_won(board, BLUE_INT):
        game_over = True
        print(colored("Blue wins!", 'blue'))
    if len(get_valid_locations(board)) == 0:
        game_over = True
        print(colored("Draw!", 'blue'))
    turn += 1