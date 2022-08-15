#Global Variable: Dictionary caused errors. Switched to list. KeyValue: 0 Error
board = [' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' ']

#Global variables called in below fucntions
currentP = "X"
not_finished = True
win = False


#BOARD FUNCTIONS
#full_board() adds '|' between each value in the dictionary, plus a 'line' of 5 hyphens
def fullBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-'*5)
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-'*5)
    print(board[6] + '|' + board[7] + '|' + board[8])

    
    
#PLAYER FUNCTIONS   
#Function taking argument 'board' that asks the current player where they'd like to place their symbol
def playerPlace(board):
    placement = int(input("Choose placement from 1-9: "))
    if placement >= 1 and placement <=9 and board[placement-1] == ' ':
        board[placement-1] = currentP
    else:
        print("Place already taken")
       #FIX THIS!
    
    
#No board modification, so no argument required    
def changeCurrentP():
    global currentP #Changes global currentP variable within the function
    if currentP == "X":
        print("It's O's turn now")
        currentP = "O"
    else:
        print("X's turn now")
        currentP = "X" #No need to write an 'elif' for the reverse, as only two outcomes possible

    
    
#CHECKING FOR WIN FUNCTIONS
#Checking if all slots in a row are equal to each other
#Makes global variable 'win' the symbol of the player
def checkHoriz(board):
    global win #Calls the global variable win within function
    if len(set(board[0:3])) <= 1 and board[0] != ' ': #Convert list to set, removes duplicates, should be one of that value in the set
        win = board[0]
        return True #Can be used to break out of game when checking result of function
    elif len(set(board[3:6])) <= 1  and board[4] != ' ':
        win = board[3]
        return True
    elif len(set(board[6:9])) <= 1  and board[7] != ' ':
        win = board[6]
        return True
    
    
def checkVert(board):
    global win 
    if len(set(board[0:7:3])) <= 1 and board[0] != ' ':
        win = board[0]
        return True
    elif len(set(board[1:8:3])) <= 1 and board[1] != ' ':
        win = board[1]
        return True
    elif len(set(board[2:9:3])) <= 1 and board[2] !=  ' ':
        win = board[2]
        return True
    
    
def checkDiag(board):
    global win
    if len(set(board[0:9:4])) <= 1 and board[0] != ' ':
        win = board[0]
        return True
    elif len(set(board[2:7:2])) <= 1 and board[2] != ' ':
        win = board[2]
        return True
    
    
def checkTie(board):
    if ' ' not in board:
        not_finished = False
        print("Tie Game! Close one!")

        
def checkWin():
    if checkHoriz(board) or checkVert(board) or checkDiag(board):
        not_finished = False
        print(f"Winner is {win}!") #f-strings to shorten required string formatting
        
    
    
    
while not_finished:
    fullBoard(board)
    playerPlace(board)
    changeCurrentP()
    checkTie(board)
    checkWin()