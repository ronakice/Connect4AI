import sys
import random
from time import sleep

choice=0
win=0
board=[['.']*7 for _ in xrange(6)]

def checkcolumn(c):
    #checkcolumn(c) checks if the top of the cth column is empty
    return (board[0][c-1] == '.')

def checkwin(XoO):
    #checkwin(XoO) prints which player wins if any and returns True if a player has won or returns False otherwise
    t1='X' if XoO==0 else 'O'
    for row in range(6):
        for column in range(7):
            if column<=3 and t1==board[row][column] and t1==board[row][column+1] and t1==board[row][column+2] and t1==board[row][column+3]:
                print "\nPlayer "+ str(XoO+1) +" wins!\n"
                return True
            if row<=2 and t1==board[row][column] and t1==board[row+1][column] and t1==board[row+2][column] and t1==board[row+3][column]:
                print "\nPlayer "+ str(XoO+1) +" wins!\n"
                print ""
                return True
            if column>=3 and row<=2 and t1==board[row][column] and t1==board[row+1][column-1] and t1==board[row+2][column-2] and t1==board[row+3][column-3]:
                print "\nPlayer "+ str(XoO+1) +" wins!\n"
                return True
            if column<=3 and row<=2 and t1==board[row][column] and t1==board[row+1][column+1] and t1==board[row+2][column+2] and t1==board[row+3][column+3]:
                print "\nPlayer "+ str(XoO+1) +" wins!\n"
                return True
    return False

def checkwin1(b2):
    t1="X"
    t2="O"
    for row in range(0,6):
        for column in range(0, 7):
            if column<=3 and t1==b2[row][column] and t1==b2[row][column+1] and t1==b2[row][column+2] and t1==b2[row][column+3]:
                return 100
            if row<=2 and t1==b2[row][column] and t1==b2[row+1][column] and t1==b2[row+2][column] and t1==b2[row+3][column]:
                return 100
            if column>=3 and row<=2 and t1==b2[row][column] and t1==b2[row+1][column-1] and t1==b2[row+2][column-2] and t1==b2[row+3][column-3] :
                return 100
            if column<=3 and row<=2 and t1==b2[row][column] and t1==b2[row+1][column+1] and t1==b2[row+2][column+2] and t1==b2[row+3][column+3] :
                return 100
            if column<=3 and t2==b2[row][column] and t2==b2[row][column+1] and t2==b2[row][column+2] and t2==b2[row][column+3]:
                return -100
            if row<=2 and t2==b2[row][column] and t2==b2[row+1][column] and t2==b2[row+2][column] and t2==b2[row+3][column]:
                return -100
            if column>=3 and row<=2 and t2==b2[row][column] and t2==b2[row+1][column-1] and t2==b2[row+2][column-2] and t2==b2[row+3][column-3] :
                return -100
            if column<=3 and row<=2 and t2==b2[row][column] and t2==b2[row+1][column+1] and t2==b2[row+2][column+2] and t2==b2[row+3][column+3] :
                return -100
    return 0

def FullBoard(bot):
    for i in range(0,7):
        if bot[0][i]==".":
            return False
    return True

def minimax(board1,level,levelweight):
    t42=checkwin1(board1)
    if(t42==100):
        return levelweight*100
    elif(t42==-100):
        return  (-100/levelweight)
    elif(level==5):
        #change the level to increase complexity
        return 0
    else:
        if FullBoard(board1):
            return 0
        else:
            a=[]
            b=[]
            for i in range(0,7):
                if board1[0][i]==".":
                    for j in range(5,-1,-1):
                        if board1[j][i]=='.':
                            if (level+choice)%2==1:
                                board1[j][i]="O"
                            else:
                                board1[j][i]="X"
                            a.append(minimax(board1,level+1,levelweight/2))
                            if level==0:
                                b.append(i)
                            board1[j][i]="."
                            break
            if(level==0 and choice==1):
                c=b[0]
                t=a[0]
                for i in range(0, len(a)):
                    if a[i]<t:
                        c=b[i]
                        t=a[i]
                return c
            elif(level==0 and choice==2):
                c=b[0]
                t=a[0]
                for i in range(0, len(a)):
                    if a[i]>t:
                        c=b[i]
                        t=a[i]
                return c
            else:
                if((level%2==0 and choice==1) or(level%2==1 and choice==2)):
                    return min(a)
                else:
                    return max(a)

def callAi(t):
    #callAi(t) makes a move from a column 1-7 with consideration of winning
    c=minimax(board,0,64)
    #print str(c)
    board.reverse()
    for x in board:
        if x[c]=='.':
            if choice==1:
                x[c]='O'
                break
            else:
                x[c]='X'
                break
    board.reverse()

def GameOn():
    global choice
    #GameOn() is the mid portion of the game i.e filling up the board and displaying it
    t=0
    words= "Choose whether you would like to be player 1 or player 2(1 or 2): "
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    choice=int(raw_input(""))
    while(t<=42):
        print("")
        for row in board:
            for x in row:
                sys.stdout.write(x+" ")
            print("")
        if t==42:
            #If the board is Full and there is no winner
            print("TIE! Game TIED!")
            break
        if t%2 == (choice-1):
            k=0
            while(k==0):
                c=raw_input("Choose your column, mate!(1-7): ")
                if c not in "0123456789" or c=="":
                    print "Choose an integer between 1-7!"

                else:
                    c=int(c)
                    if c<=0 or c>=8:
                        print "Choose between 1-7!"
                    elif not checkcolumn(c):
                        print "Column full,try another column!"
                    else:
                        board.reverse()
                        for x in board:
                            if x[c-1]=='.':
                                if t%2==0:
                                    x[c-1]='X'
                                    break
                                else:
                                    x[c-1]='O'
                                    break
                        board.reverse()
                        k=1
        else:
            callAi(t)
        if checkwin(t%2):
            for row in board:
                for x in row:
                    sys.stdout.write(x+" ")
                print ""
            break
        t=t+1;

def startGame() :
    print(len(board))
    #startGame() gives the pre-game instructions
    words = "Greetings Stranger(s)! "
    #Experimental Typing
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print ""
    words = "Welcome to my Connect-4 Game! Do you know the rules to the game?(Y/N)"
    #Experimental Typing
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    c=raw_input("")
    if c=="N":
        words = "The rules of this game are simple you connect 4 of X's or the O's, vertically,horizontally or diagonally to win the game."
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    print ""
    GameOn()
#GameOn()
startGame()
