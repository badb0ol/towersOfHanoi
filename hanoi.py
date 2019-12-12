import turtle
import random
import time
import copy
from datetime import datetime, date

## IMPORTANT VARIABLES FOR DRAWING
turtle.hideturtle()
turtle.setup(width=1366, height=768, startx=30, starty=60)
turtle.colormode(255)
turtle.bgcolor(105,105,105)

R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)

R1 = random.randint(0,255)
G1 = random.randint(0,255)
B1 = random.randint(0,255)

## HANOI FUNCTIONS

def init(n):
    t = 3 # tower constant
    a = [[] for i in range(t)] # 2d array generation
    #a = [[1],[6],[3]] debugging
    for i in range(n): # first cell
        a[0].append(n-i) # decrement disk nb in descending order
    #print(len(a[]))
    return(a)

def diskAmount(gameboard, nbTower):
    if nbTower > 2 or nbTower < 0:
        return -1
    else:
        return len(gameboard[nbTower])

def diskPosition(gameboard, numDisk):
    for i in gameboard:
        if len(i) >= 0:
            if numDisk in i:
                return gameboard.index(i)
    return -1

def diskPos(gameboard, f, n): # useless
    z = True
    while z:
        if f <= 0:
            print('disque trop petit')
            f = int(input('Quel disque cherchez vous? '))
        z = False
    if isInList(gameboard, f, n) == True:
        g = diskPosition(gameboard, f)
        print('Le disque', f,'est situe sur la tour', g)
    else:
        return -1

def checkMove(gameboard, nt1, nt2):
    return (isEmpty(gameboard, nt1) == False and (lastElem(gameboard, nt2) > lastElem(gameboard, nt1))) or isEmpty(gameboard, nt2) == True

def checkVictory(gameboard, n):
    #moveCount = (2**n)+1
    if isEmpty(gameboard, 0) == True and isEmpty(gameboard, 1) == True:
        if lastElem(gameboard, 2) == 1 and firstElem(gameboard, 2) == n:
            if diskAmount(gameboard, 2) == n:
                return True
    return False

## EXTRA FUNCTIONS

def buttonClick():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(5,6)
    t.pendown()
    t.hideturtle()
    t.write('Game initializing...\n Please Wait', align='center', font=('Arial',20,'normal'))
    time.sleep(2)
    t.undo()
    t.hideturtle()
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.hideturtle()
    t.write('Welcome to the Towers Of Hanoi!', align='center', font=('Arial',20,'normal'))
    time.sleep(3)
    #t.undo()
    main()

def exitButton():
    t.hideturtle()
    t.penup()
    t.goto(5,6)
    t.pendown()
    #for i in range(3):

    t = turtle.Turtle()
    t.onclick(exitClick)
    turtle.listen()

def firstElem(gameboard, nbTower):# FONCTION DISQUE_SUPERIEUR
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        if isEmpty(gameboard, nbTower) == True:
            return 0
        return gameboard[nbTower][0] #lastElem is the 1st element starting from the end
    return -1

def lastElem(gameboard, nbTower):
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        if isEmpty(gameboard, nbTower) == True:
            return 0
        return gameboard[nbTower][-1]
    return -1

def diskPosInList(gameboard, nDisk):
    nTower = diskPosition(gameboard, nDisk)
    for towerIndex, tower in enumerate(gameboard):
        if len(tower) >= 0:
            for diskIndex, disk in enumerate(tower):
                if nDisk == disk:
                    return diskIndex
    return -1

def isEmpty(gameboard, nbTower):
    if nbTower >= 0 and nbTower <= 2:
        for i in gameboard:
            if len(gameboard[nbTower]) == 0:
                return True
        return False
    return -1

def isInList(gameboard, elem, n):
    if elem <= 0 or elem > n:
        return False
    else:
        for i in gameboard:
            if elem in i:
                return True
        return False

## DRAWING FUNCTIONS

def drawBoard(n, R1, G1, B1):
    #R = random.randint(0,255)
    #G = random.randint(0,255)
    #B = random.randint(0,255)
    boardSize = 30+80+(4*(40+(30*(n-1))))# 10px towers, gap of 20px between towers, biggestDisk = 40+(30*n-1)
    originX = (-250)-(40+(30*n))
    originY = (-100)-(20*n)
    tHeight = (20*n)+20
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(originX,originY)
    t.pendown()
    turtle.colormode(255)
    t.fillcolor(R1, G1, B1)
    t.begin_fill()
    i = 0
    while i < 2:
        t.forward(boardSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        i += 1
    t.end_fill()
    t1 = (boardSize/4)
    t2 = (boardSize/2)
    t3 = ((boardSize/4)*3)
    t.penup()
    t.goto(originX+t1,originY+20) #goto tower 1
    t.pendown()

    t.fillcolor(R1, G1, B1)
    t.begin_fill()
    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.end_fill()

    t.penup()
    t.goto(originX+t2,originY+20) #goto tower 2
    t.pendown()

    t.fillcolor(R1, G1, B1)
    t.begin_fill()
    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.end_fill()

    t.penup()
    t.goto(originX+t3,originY+20) #goto tower 3
    t.pendown()

    t.fillcolor(R1, G1, B1)
    t.begin_fill()
    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.end_fill()

def eraseBoard(n):
    boardSize = 30+80+(4*(40+(30*(n-1))))# 10px towers, gap of 20px between towers, biggestDisk = 40+(30*n-1)
    originX = (-250)-(40+(30*n))
    originY = (-100)-(20*n)
    tHeight = (20*n)+20
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(originX,originY)
    t.pendown()
    turtle.colormode(255)
    t.pencolor(105,105,105)
    t.fillcolor(105,105,105)
    t.begin_fill()
    i = 0
    while i < 2:
        t.forward(boardSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        i += 1
    t.end_fill()
    t1 = (boardSize/4)
    t2 = (boardSize/2)
    t3 = ((boardSize/4)*3)
    t.penup()
    t.goto(originX+t1,originY+20) #goto tower 1
    t.pendown()

    t.fillcolor(105,105,105)
    t.begin_fill()
    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.end_fill()

    t.penup()
    t.goto(originX+t2,originY+20) #goto tower 2
    t.pendown()

    t.fillcolor(105,105,105)
    t.begin_fill()
    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.end_fill()

    t.penup()
    t.goto(originX+t3,originY+20) #goto tower 3
    t.pendown()

    t.fillcolor(105,105,105)
    t.begin_fill()
    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.end_fill()

def drawDisk(nDisk, gameboard, n, R,G,B): # draws the disk you pass as parameter
    t = turtle.Turtle()
    t.hideturtle()
    turtle.colormode(255)
    t.fillcolor(R,G,B)
    t.speed(0)
    boardSize = 30+80+(4*(40+(30*(n-1))))
    t1 = (boardSize/4)
    t2 = (boardSize/2)
    t3 = ((boardSize/4)*3)
    diskSize = 40+(30*(nDisk-1))
    originX = (-250)-(40+(30*n))
    originY = (-100)-(20*n)
    tHeight = (20*n)+20
    dPos = diskPosition(gameboard, nDisk) #Position of disk by order of lists
    g = diskPosInList(gameboard, nDisk) #Position of disk within its list
    # get index of elem in the sublist and index of arrival
    if dPos == 0: # if destination tower = 1 and is empty
        #t.hideturtle()
        t.penup()
        t.goto(originX+t1,originY+20+(g*20)) #goto tower 1
        t.pendown()
        t.fillcolor(R,G,B)
        t.begin_fill()
        t.forward(diskSize/2)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(diskSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.left(diskSize/2)
        t.end_fill()
    elif dPos == 1: # if destination tower = 2 and is empty
        #t.hideturtle()
        t.penup()
        t.goto(originX+t2,originY+20+(g*20)) #goto tower 1
        t.pendown()
        t.fillcolor(R,G,B)
        t.begin_fill()
        t.forward(diskSize/2)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(diskSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.left(diskSize/2)
        t.end_fill()
    elif dPos == 2: # if destination tower = 3 and is empty
        #t.hideturtle()
        t.penup()
        t.goto(originX+t3,originY+20+(g*20)) #goto tower 1
        t.pendown()
        t.fillcolor(R,G,B)
        t.begin_fill()
        t.forward(diskSize/2)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(diskSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.left(diskSize/2)
        t.end_fill()

def eraseDisk(nDisk, gameboard, n):
        R = 105
        G = 105
        B = 105
        t = turtle.Turtle()
        t.hideturtle()
        turtle.colormode(255)
        t.speed(0)
        boardSize = 30+80+(4*(40+(30*(n-1))))
        t1 = (boardSize/4)
        t2 = (boardSize/2)
        t3 = ((boardSize/4)*3)
        diskSize = 40+(30*(nDisk-1))
        originX = (-250)-(40+(30*n))
        originY = (-100)-(20*n)
        tHeight = (20*n)+20
        dPos = diskPosition(gameboard, nDisk)
        g = diskPosInList(gameboard, nDisk)
        # get index of elem in the sublist and index of arrival
        if dPos == 0: # if destination tower = 1 and is empty
            #t.hideturtle()
            t.penup()
            t.goto(originX+t1,originY+20+(g*20)) #goto tower 1
            t.pendown()
            t.pencolor(R,G,B)
            t.fillcolor(R,G,B)
            t.begin_fill()
            t.forward(diskSize/2)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(diskSize)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.left(diskSize/2)
            t.end_fill()
        elif dPos == 1: # if destination tower = 2 and is empty
            #t.hideturtle()
            t.penup()
            t.goto(originX+t2,originY+20+(g*20)) #goto tower 1
            t.pendown()
            t.pencolor(R,G,B)
            t.fillcolor(R,G,B)
            t.begin_fill()
            t.forward(diskSize/2)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(diskSize)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.left(diskSize/2)
            t.end_fill()
        elif dPos == 2: # if destination tower = 3 and is empty
            #t.hideturtle()
            t.penup()
            t.goto(originX+t3,originY+20+(g*20)) #goto tower 1
            t.pendown()
            t.pencolor(R,G,B)
            t.fillcolor(R,G,B)
            t.begin_fill()
            t.forward(diskSize/2)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(diskSize)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.left(diskSize/2)
            t.end_fill()

def drawConfig(gameboard, n, R,G,B):
    for i in range(n+1):
        drawDisk(i, gameboard, n, R,G,B)

def eraseAll(gameboard, n):
    for i in range(n+1):
        eraseDisk(i, gameboard, n)

## MOVE FUNCTIONS

def readCoords(gameboard):
    screen =turtle.Screen()
    i = True
    while i:
        t1 = screen.numinput('Choisir 1ere tour: ','Choisir 1ere tour: ')
        t2 = screen.numinput('Choisir 2eme tour: ','Choisir 2eme tour: ')
        temp1 = int(t1)
        temp2 = int(t2)
        t1 = temp1
        t2 = temp2
        if checkMove(gameboard, t1, t2) == True:
            return t1, t2
        t1 = screen.numinput('Choix impossible\nChoisir 1ere tour: ','Choisir 2eme tour: ')
        t2 = screen.numinput('Choisir 2eme tour: ','Choisir 2eme tour: ')
        temp1 = int(t1)
        temp2 = int(t2)
        t1 = temp1
        t2 = temp2

def playTurn(gameboard, n):
    t1, t2 = readCoords(gameboard)
    topT1 = lastElem(gameboard, t1)
    topT2 = lastElem(gameboard, t2)
    if checkMove(gameboard, t1, t2) == True:
        eraseDisk(topT1, gameboard, n) # eraseDisk(lastElem(gameboard, t1), gameboard, n)
        gameboard[t1].pop()
        drawDisk(topT2, gameboard, n, R,G,B) #drawDisk(lastElem(gameboard, t2), gameboard, n, R,G,B)
        gameboard[t2].append(topT1)
    else:
        print('Please try again')
        t1, t2 = readCoords(gameboard)
    return gameboard

def gameLoop(gameboard, n):
    moveCount = 0
    startTimeSecs = time.mktime(time.localtime())
    while (checkVictory(gameboard, n) == False):
        drawBoard(n, R1, G1, B1)
        drawConfig(gameboard, n, R,G,B)
        playTurn(gameboard, n)
        moveCount += 1
        #drawBoard(n, R1, G1, B1)
        #drawConfig(gameboard, n, R,G,B)
    print('Game over!')
    endTimeSecs = time.mktime(time.localtime())
    save(gameboard, n, endTimeSecs, startTimeSecs, moveCount)

def playAgain(gameboard, n):
    screen = turtle.Screen()
    t = turtle.Turtle()
    goAgain = screen.textinput('Rejouer?','Souhaitez vous rejouer? (y/n)')
    if goAgain.lower() == "y":
        eraseAll(gameboard, n)
        eraseBoard(n)
        main()
    elif goAgain.lower() == "n":
        print('Thank you for playing!')
        turtle.bye()
    while not (goAgain == 'y' or goAgain == 'n'):
        goAgain = screen.textinput('Rejouer?','Souhaitez vous rejouer? (y/n)')

## CANCEL HITS

def saveLastHit(gameboard):
    savedConfigs = {}
    i = 1
    while (checkVictory == False):
        nb = i
        i += 1
        savedGame = copy.deepcopy(gameboard)
        savedConfigs[nb] = savedGame

def cancelLastHit():
    return 0

## GAME FILES

def save(gameboard, n, endTimeSecs, startTimeSecs, moveCount):
    username = input('Enter your username: ')
    diskCount = n
    avgTime = endTimeSecs - startTimeSecs
    scores = [(username, diskCount, moveCount, avgTime)]
    sortByTime(scores)
    with open('HighScores.txt', 'a') as f: # using 'with' automatically closes the file when loop exits
        for username, diskCount, moveCount, avgTime in scores:
            f.write('Username: {0}, Disk Count: {1}, Move Count: {2}, Time Taken: {3}\n'.format(username, diskCount, moveCount, avgTime))
    return scores

def sortByTime(scores):
    scores.sort(key=lambda scores: scores[3])
    return scores

def readScores():
    with open('HighScores.txt', 'r') as f: # using 'with' automatically closes the file when loop exits
        print(f)
    return scores

def displayScores():
    with open('HighScores.txt', 'r') as f:
        print(f)

# RECURSIVE SOLVE

def goSolveUrself(gameboard, t1, t3, n):
    maxSize = (2**n)-1
    solvedGame = []
    #T1Array = [] for i in range(maxSize)
    #T2Array = [] for i in range(maxSize)
    if n == 0:
        return solvedGame
    if n == 1:
        gameboard[t3].append(gameboard[t1].pop())
        #print(t1,'->',t3,':',gameboard) # used during debugging to check solution & steps in terminal
        solvedGame.append(tuple([t1,t3])) # this appends a tupl e contained in a list to an already existing list everytime a movement is made
    else:
        # I chose to use append because extending a new tuple to a list recursively made it very inconvenient to traverse
        t2 = 3 - t1 - t3 # t1+t3+t2 = 3 this allows recursion to keep track of which tower to traverse recursively
        solvedGame.extend(goSolveUrself(gameboard, t1, t2, n-1)) #appends the legal move between A and B by top disk solvedGame array (tower 1 & tower 2)
        solvedGame.extend(goSolveUrself(gameboard, t1, t3, 1)) #appends the legal move between A and C by bottom disk solvedGame array (tower 1 & tower 3)
        solvedGame.extend(goSolveUrself(gameboard, t2, t3, n-1)) #appends the legal move between B and C by top disk to solvedGame array (tower 2 & tower 3)
    return solvedGame

def autoPlayTurn(gameboard, n):
    turtle.hideturtle()
    solvedGame = goSolveUrself(gameboard, 0, 2, n)
    newGameboard = init(n)
    drawBoard(n, R1, G1, B1)
    drawConfig(newGameboard, n, R,G,B)
    for i, j in solvedGame:
        topT1 = lastElem(newGameboard, i)
        if checkMove(newGameboard, i, j) == True:
            eraseDisk(topT1, newGameboard, n) # eraseDisk(lastElem(gameboard, t1), gameboard, n)
            newGameboard[i].pop()
            newGameboard[j].append(topT1)# gameboard[j].append(gameboard[i].pop())
            drawBoard(n, R1, G1, B1)
            drawConfig(newGameboard, n, R,G,B)
    return newGameboard

def autoPlayTurnFast(gameboard, n):
    turtle.tracer(0,0)
    turtle.hideturtle()
    solvedGame = goSolveUrself(gameboard, 0, 2, n)
    print(solvedGame)
    print('\nAbove is the solution.\nAmmount of moves required for',n,'disks',':',len(solvedGame))
    newGameboard = init(n)
    drawBoard(n, R1, G1, B1)
    drawConfig(newGameboard, n, R,G,B)
    turtle.update()
    for i, j in solvedGame:
        topT1 = lastElem(newGameboard, i)
        if checkMove(newGameboard, i, j) == True:
            eraseDisk(topT1, newGameboard, n) # eraseDisk(lastElem(gameboard, t1), gameboard, n)
            newGameboard[i].pop()
            newGameboard[j].append(topT1)# gameboard[j].append(gameboard[i].pop())
            drawBoard(n, R1, G1, B1)
            drawConfig(newGameboard, n, R,G,B)
            turtle.update() #update screen to show changes made by drawing
    drawBoard(n, R1, G1, B1)
    drawConfig(newGameboard, n, R,G,B)
    turtle.update()
    return newGameboard

## MAIN FUNCTION
def main():
    screen = turtle.Screen()
    a = screen.numinput('Towers Of Hanoi','Welcome\nCombien de disques? ')
    #a = int(input('\nCombien de disques? '))
    temp = int(a)
    a = temp
    while a < 2:
        a = screen.numinput('Nombre de disques trop petit','Veuillez reessayer\nCombien de disques?  ') #getting float through turtle input function 'numinput'
        temp = int(a) # so I have to convert it to an int and store it temporarily in a var to pass through all my functions
        a = temp # then move it back to OG var
    gameboard = init(a)
    if a <= 5:
        b = screen.numinput('Play or watch?','Voulez vous jouer, ou regarder jouer? (1/2)')
        temp = int(b)
        b = temp
    if a > 5:
        b = screen.numinput('Play or watch?','Voulez vous jouer, ou regarder jouer? (1/2)\n(Si vous choisissez opt. 2, la partie sera jouée plus rapidement)')
        temp = int(b)
        b = temp
    while not (b == 1 or b == 2):
        b = screen.numinput('Choix impossible. Veuillez reessayer','\nVoulez vous jouer, ou regarder jouer? (1/2)')
        temp = int(b)
        b = temp
    if b == 1:
        gameLoop(gameboard, a)
        save(gameboard, a)
        playAgain(gameboard, a)
    elif b == 2:
        if a <= 5:
            autoPlayTurn(gameboard, a)
            playAgain(gameboard, a)
        elif a > 5:
            autoPlayTurnFast(gameboard, a)
            playAgain(gameboard, a)
    else:
        b = screen.numinput('Choix impossible. Veuillez reessayer','\nVoulez vous jouer, ou regarder jouer? (1/2)')
        temp = int(b)
        b = temp

def startUp():
    buttonClick()
    turtle.onclick(isClicked)#, "Return"
    turtle.listen()
    #main() # calls main to start program
    #allows tracer(0,0) to render when I use update() to show drawings on screen
    #leaves turtle window open when program is done executing

startUp()
turtle.mainloop()
turtle.done()
