from IPython.display import clear_output

def displayBoard(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])
    
    
def askInput(inp1):
    while(inp1!='X' and inp1!='O'):
        print('Player 1, enter your choice')
        inp1 = input()
    print('Player 1 is using',inp1)
    if(inp1=='X'):
        inp2='O'
        print('Player 2 is using','O')
    else:
        inp2='X'
        print('Player 2 is using','X')
    return inp1,inp2

def updateBoard(choice,board,player):
    if(player==1):
        board[choice]=inp1
    else:
        board[choice]=inp2
    return board
        
def checkGame(board,mark):
    for lines in check:
        if(board[lines[0]] == board[lines[1]] == board[lines[2]] == mark):
            return True,True
    for i in range(1,10):
        if(board[i]==' '):
            return False,False
    return True,False

def getChoices(gameOver,choice,player1):    
    while(not gameOver):
        while ((choice not in range(1,10)) or board[choice] != ' '):
            print('enter your choice')
            choice = int(input())
            print('your choice is',choice)
        if(player1):
            updateBoard(choice,board,1)
            player1=False
            gameOver,gameWon = checkGame(board,inp1)
        else:
            updateBoard(choice,board,2)
            player1=True
            gameOver,gameWon = checkGame(board,inp2)
        displayBoard(board)
        if gameWon:
            print('you won the game!!!')
        if gameOver:
            print('game is over!!!')

check=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

while True:
    print('do you want to play game Y')
    answer = input()
    board = [' ']*10
    if answer=='Y':
        displayBoard(board)
        inp1=' '
        inp2=' '
        inp1,inp2=askInput(inp1)
        gameOver = False
        player1=True
        choice=0
        getChoices(gameOver,choice,player1)
    else:
        break
    

    
    
    
