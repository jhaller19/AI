# -*- coding: utf-8 -*-
"""
Calculations for 100 runs:

British Museum:
    Average Iteartions: 217404.86
    Average Moves:      1739238.88
    Max Iterations:     1135322 
    Max Moves:          9082576
    Min Iterations:     4354        
    Min Moves:          34832

DFS (deterministic):
    Average Iteartions: 982
    Average Moves:      982
    Max Iterations:     982 
    Max Moves:          982
    Min Iterations:     982        
    Min Moves:          982

Hill Climbing:
    Average Iteartions: 23.53
    Average Moves:      63.99
    Max Iterations:     193 
    Max Moves:          522
    Min Iterations:     2        
    Min Moves:          9

Forward Checking (deterministic):
    Average Iteartions: 219
    Average Moves:      219
    Max Iterations:     219 
    Max Moves:          219
    Min Iterations:     219        
    Min Moves:          219

"""
from cmath import inf
import math
from shutil import move

columns = [] #columns is the locations for each of the queens
size = 8
import random #hint -- you will need this for the following code: column=random.randrange(0,size)

"""Let's setup one iteration of the British Museum algorithm-- we'll put down 4 queens randomly."""

def place_n_queens(size):
    columns.clear()
    row = 0
    while row < size:
        column=random.randrange(0,size)
        columns.append(column)
        row+=1

place_n_queens(size)

"""Now, we can print the result with a simple loop:"""
def displayBoard(columns):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('X', end=' ')
            else:
                print(' .', end=' ')
        print()
    print(columns)
def display():
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('X', end=' ')
            else:
                print(' .', end=' ')
        print()


"""This of course is not necessary legal, so we'll write a simple DFS search with backtracking:"""

def solve_queen(size):
    columns.clear()
    number_of_moves = 0 #where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0  
    row = 0
    column = 0
    # iterate over rows of board
    while True:
        #place queen in next row
        ''''print(columns)
        print("I have ", row, " number of queens put down")
        display()
        print(number_of_moves)'''
        while column < size:
            number_of_iterations+=1
            number_of_moves += 1
            if next_row_is_safe(column):
                place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if (column == size or row == size):
            number_of_iterations+=1
            number_of_moves +=1
            # if board is full, we have a solution
            if row == size:
                #print("I did it! Here is my solution")
                display()
                print(str(number_of_iterations) + ", " + str(number_of_moves))
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row()
            if (prev_column == -1): #I backtracked past column 1
                print("There are no solutions")
                #print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column

"""This code is nice, but it uses three functions:
1. place_in_next_row
2. remove_in_current_row
3. next_row_is_safe
That we now have to define
"""

def place_in_next_row(column):
    columns.append(column)
 
def remove_in_current_row():
    if len(columns) > 0:
        return columns.pop()
    return -1
 
def next_row_is_safe(column):
    row = len(columns) 
    # check column
    for queen_column in columns:
        if column == queen_column:
            return False
 
    # check diagonal
    for queen_row, queen_column in enumerate(columns):
        if queen_column - queen_row == column - row:
            return False
 
    # check other diagonal
    for queen_row, queen_column in enumerate(columns):
        if ((size - queen_column) - queen_row
            == (size - column) - row):
            return False
    return True

num_iterations=0
number_moves = 0
print("***************DFS*****************")
num_iterations, number_moves=solve_queen(size)

######################################British Museum###########################################
print('*****British Museum********')
def checkValid(columns):
    valid = True
    checkCols = columns.copy()
    columns.clear()
    for i in checkCols:
        valid &= next_row_is_safe(i)
        if(not valid):
            return valid
        place_in_next_row(i)
    return valid

def britishMuseum(columns):
    valid = False
    iterations = 0
    moves = 0
    while(not valid):
        iterations+=1
        moves+=size
        #Randomly place queens then check if its a solution
        place_n_queens(size)
        valid = checkValid(columns)
    return iterations, moves
'''
BM_Iterations = 0
BM_Moves = 0
BM_Max_Iterations = -inf
BM_Max_Moves = -inf
BM_Min_Iterations = inf
BM_Min_Moves = inf
n = 100
for i in range(n):
    cur_Iterations, cur_Moves = britishMuseum(columns)
    BM_Iterations += cur_Iterations
    BM_Moves += cur_Moves
    BM_Max_Iterations = max(BM_Max_Iterations,cur_Iterations)
    BM_Max_Moves = max(BM_Max_Moves,cur_Moves)
    BM_Min_Iterations = min(BM_Min_Iterations,cur_Iterations)
    BM_Min_Moves = min(BM_Min_Moves,cur_Moves)
    displayBoard(columns)
print(str(BM_Iterations/n) + "," + str(BM_Moves/n))
print(str(BM_Max_Iterations) + "," + str(BM_Max_Moves))
print(str(BM_Min_Iterations) + "," + str(BM_Min_Moves))
'''
num_i, num_m = britishMuseum(columns)
displayBoard(columns)
print(str(num_i) + "," + str(num_m))

#####################################################################################################
def countAttacks(columns):
    # check column
    c = 0
    row = 0
    for column in columns:
        for i in range(len(columns)):
            if column == columns[i] and i != row:
                c+=1
        # check diagonal
        for queen_row, queen_column in enumerate(columns):
            if queen_column - queen_row == column - row and (queen_column != column and queen_row != row):
                c+=1
        # check other diagonal
        for queen_row, queen_column in enumerate(columns):
            if ((size - queen_column) - queen_row
                == (size - column) - row) and (queen_column != column and queen_row != row):
                c+=1
        row+=1
    return c/2
################################Hill Climbing#################################
#checks if arrays are equal
def arEqual(ar1,ar2):
    for i in range(len(ar1)):
        if(ar1[i] != ar2[i]):
            return False
    return True
#Used for random restart
def rePlaceQueens(columns,size):
    columns.clear()
    row = 0
    while row < size:
        column=random.randrange(0,size)
        columns.append(column)
        row+=1
def displayBoard(columns):
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('X', end=' ')
            else:
                print(' .', end=' ')
        print()
    print(columns)
place_n_queens(size)

def hillClimbing(columns):
    moves = len(columns)
    rePlaceQueens(columns,len(columns))
    prevH = countAttacks(columns)
    min = prevH
    iterations = 0
    curIterations = 0
    maxIterations = 300
    while True:
        iterations+=1
        curIterations+=1
        copyOfColumns = columns.copy()
        curMinArray = columns.copy()
        #Look at all possible states 1 move away from the current state
        for i in range(len(columns)):
            for j in range(len(columns)):
                temp = copyOfColumns[i]
                copyOfColumns[i] = j
                if(not arEqual(copyOfColumns,columns)):
                    #Calculate the h-value of the state
                    h = countAttacks(copyOfColumns)
                    if(h == 0):                     #Solution found
                        columns = copyOfColumns
                        displayBoard(copyOfColumns)
                        return iterations,moves
                    if(h <= min):
                        min = h
                        curMinArray = copyOfColumns.copy()
                copyOfColumns[i] = temp 
        #Do a random restart if we go above maxIterations or the previous h-value is the same as the current one           
        if(prevH == min or curIterations >= maxIterations):
            rePlaceQueens(columns,size)
            curIterations = 0
            moves += len(columns) #increment moves by size of columns for restart
            prevH = countAttacks(columns)
            min = prevH
            continue
        moves+=1
        prevH = min
        columns = curMinArray
print("********Hill Climbing*************")
'''
HC_Iterations = 0
HC_Moves = 0
HC_Max_Iterations = -inf
HC_Max_Moves = -inf
HC_Min_Iterations = inf
HC_Min_Moves = inf
n = 100
for i in range(n):
    cur_Iterations, cur_Moves = hillClimbing(columns)
    HC_Iterations += cur_Iterations
    HC_Moves += cur_Moves
    HC_Max_Iterations = max(HC_Max_Iterations,cur_Iterations)
    HC_Max_Moves = max(HC_Max_Moves,cur_Moves)
    HC_Min_Iterations = min(HC_Min_Iterations,cur_Iterations)
    HC_Min_Moves = min(HC_Min_Moves,cur_Moves)
    displayBoard(columns)
print(str(HC_Iterations/n) + "," + str(HC_Moves/n))
print(str(HC_Max_Iterations) + "," + str(HC_Max_Moves))
print(str(HC_Min_Iterations) + "," + str(HC_Min_Moves))
'''
num_i, num_m = hillClimbing(columns)
print(str(num_i) + "," + str(num_m))


######################################Forward Checking############################################3
def next_row_is_safe_FC(column, temp):
    row = len(columns) 
    # check column for invalid move
    if temp[row][column] != 0:
        return False
    for queen_column in columns:
        if column == queen_column:
            return False
    return True

def place_in_next_row_FC(column,row,temp,columns):
    columns.append(column)
    size = len(columns)
    #Mark off the invalid spots after this placements
    #Mark off columns
    for i in range(len(temp)):
        if(temp[i][column] == 0):
            temp[i][column] = size
    r = row
    c = column
    #Mark off diagonals
    while True:
        if(r > len(temp) - 1 or c > len(temp) - 1):
            break
        if(temp[r][c] == 0):
            temp[r][c] = size
        r+=1
        c+=1
    r = row
    c = column
    while True:
        if(r < 0 or c < 0):
            break
        if(temp[r][c] == 0):
            temp[r][c] = size
        r-=1
        c-=1
    r = row
    c = column
    while True:
        if(r > len(temp) - 1 or c < 0):
            break
        if(temp[r][c] == 0):
            temp[r][c] = size
        r+=1
        c-=1
    r = row
    c = column
    while True:
        if(c > len(temp) - 1 or r < 0):
            break
        if(temp[r][c] == 0):
            temp[r][c] = size
        c+=1
        r-=1
    
def remove_in_current_row_FC(column,row,temp,columns):
    #Revalidate the marked spots after removal of a queen
    if len(columns) > 0:
        #Revalidate columns
        for i in range(len(temp)):
            if(temp[i][column] == len(columns)):
                temp[i][column] = 0
        r = row
        c = column
        #Revalidate diagonals
        while True:
            if(r > len(temp) - 1 or c > len(temp) - 1):
                break
            if(temp[r][c] == len(columns)):
                temp[r][c] = 0
            r+=1
            c+=1
        r = row
        c = column
        while True:
            if(r < 0 or c < 0):
                break
            if(temp[r][c] == len(columns)):
                temp[r][c] = 0
            r-=1
            c-=1
        r = row
        c = column
        while True:
            if(r > len(temp) - 1 or c < 0):
                break
            if(temp[r][c] == len(columns)):
                temp[r][c] = 0
            r+=1
            c-=1
        r = row
        c = column
        while True:
            if(c > len(temp) - 1 or r < 0):
                break
            if(temp[r][c] == len(columns)):
                temp[r][c] = 0
            c+=1
            r-=1
        return columns.pop()
    return -1    

'''
This method is the same as the DFS one above but with the additional feature of
marking all invalid spots on the board in the place_in_next_row() method
and unmarks the invalid spots in the remove_in_current_row() method
'''
def forwardChecking(columns):
    temp = [ [ 0 for i in range(size) ] for j in range(size) ] # copy of board to mark off invalid spots after placement
    columns.clear()
    number_of_moves = 0
    number_of_iterations = 0  
    row = 0
    column = 0
    # iterate over rows of board
    while True:
        while column < size:
            #If the row+column has been marked off as invalid already, skip to next iteration
            if(temp[row][column] != 0):
                column+=1
                continue
            number_of_iterations+=1
            if next_row_is_safe_FC(column,temp):
                number_of_moves += 1
                place_in_next_row_FC(column,row,temp,columns)
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if (column == size or row == size):
            number_of_iterations+=1
            number_of_moves +=1
            # if board is full, we have a solution
            if row == size:
                #print("I did it! Here is my solution")
                displayBoard(columns)
                print(str(number_of_iterations) + ", " + str(number_of_moves))
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row_FC(columns[row - 1],row - 1,temp,columns)
            if (prev_column == -1): #I backtracked past column 1
                print("There are no solutions")
                #print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column
print("*********Forward Checking***********")
num_i, num_m = forwardChecking(columns)
