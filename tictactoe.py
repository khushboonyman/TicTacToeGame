def display(board,index):
    val = str(index) if board[index]==' ' else (board[index])
    return val

def displayBoard(board):
    print(display(board,1)+'|'+display(board,2)+'|'+display(board,3))
    print('-----')
    print(display(board,4)+'|'+display(board,5)+'|'+display(board,6))
    print('-----')
    print(display(board,7)+'|'+display(board,8)+'|'+display(board,9))
    
    
def askInput(inp1):
    while(inp1!='X' and inp1!='O'):
        inp1 = input('Player 1, enter your choice, only X or O is acceptable : ')
    print('Player 1 is using',inp1)
    if(inp1=='X'):
        inp2='O'
        print('Player 2 is using O')
    else:
        inp2='X'
        print('Player 2 is using X')
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
    text = 'enter choice on board : '     
    while(not gameOver):
        while ((choice not in range(1,10)) or board[choice] != ' '):
            if player1 :
                choice = int(input('Player 1 '+text))
            else :
                choice = int(input('Player 2 '+text))
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
    answer = input('do you want to play game enter Y for yes, anything else is a No : ')
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
    

    
    
    
