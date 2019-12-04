import turtle
import random
import time
from datetime import datetime, date

## IMPORTANT VARIABLES FOR DRAWING

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

def initButton():
    t = turtle.Turtle()
    t.hideturtle()
    t.fillcolor('white')
    t.begin_fill()
    for i in range(2):
        t.forward(80)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(5,6)
    t.pendown()
    t.write('Initialize', font=('Arial',20,'normal'))

def buttonClick(x, y):
    if x > 2 and x < 81 and y > 9 and y > 27:
        return 0

def isClicked():
    turtle.onscreenclick(buttonClick, 1)
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

def checkInput(Alpha):
    return (Alpha == ' ') or (Alpha == '')

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
    boardSize = 30+80+(3*(40+(30*(n-1))))# 10px towers, gap of 20px between towers, biggestDisk = 40+(30*n-1)
    originX = (-100)-(30*n)
    originY = (-50)-(20*n)
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
    boardSize = 30+80+(3*(40+(30*(n-1))))# 10px towers, gap of 20px between towers, biggestDisk = 40+(30*n-1)
    originX = (-100)-(30*n)
    originY = (-50)-(20*n)
    tHeight = (20*n)+20
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
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
    boardSize = 30+80+(3*(40+(30*(n-1))))
    t1 = (boardSize/4)
    t2 = (boardSize/2)
    t3 = ((boardSize/4)*3)
    diskSize = 40+(30*(nDisk-1))
    originX = (-100)-(30*n)
    originY = (-50)-(20*n)
    tHeight = (20*n)+20
    dPos = diskPosition(gameboard, nDisk) #Position of disk by order of lists
    g = diskPosInList(gameboard, nDisk) #Position of disk within its list
    # get index of elem in the sublist and index of arrival
    if dPos == 0: # if destination tower = 1 and is empty
        t.hideturtle()
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
        t.hideturtle()
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
        t.hideturtle()
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
        boardSize = 30+80+(3*(40+(30*(n-1))))
        t1 = (boardSize/4)
        t2 = (boardSize/2)
        t3 = ((boardSize/4)*3)
        diskSize = 40+(30*(nDisk-1))
        originX = (-100)-(30*n)
        originY = (-50)-(20*n)
        tHeight = (20*n)+20
        dPos = diskPosition(gameboard, nDisk)
        g = diskPosInList(gameboard, nDisk)
        # get index of elem in the sublist and index of arrival
        if dPos == 0: # if destination tower = 1 and is empty
            t.hideturtle()
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
            t.hideturtle()
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
            t.hideturtle()
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
    i = True
    while i:
        t1 = int(input('Choisir 1ere tour: '))
        t2 = int(input('Choisir 2eme tour: '))
        if checkInput(t1) == True or checkInput(t2) == True: #or (checkInput(t1) == True and checkInput(t2) == True):
            t1 = int(input('Choix impossible\nChoisir 1ere tour: '))
            t2 = int(input('Choisir 2eme tour: '))
        else:
            if checkMove(gameboard, t1, t2) == True:
                return t1, t2
            t1 = int(input('Choix impossible\nChoisir 1ere tour: '))
            t2 = int(input('Choisir 2eme tour: '))

        #if checkMove(gameboard, t1, t2) == True:
        #    print('This move is authorized')
        #else:
        #    print('This move is not authorized')
        #if checkVictory(gameboard, a) == True:
        #    print('Game over!')
        #    i = False
        #else:
        #    print('The game goes on!')

        #if isEmpty(gameboard, t1) == True:
            #t1 = int(input('1ere tour vide.\nChoisir 1ere tour: '))
            #t2 = int(input('Choisir 2eme tour: '))
        #elif t1 > 2 or t1 < 0:
            #t1 = int(input('Tour 1 entrée non existante.\nChoisir 1ere tour: '))
            #t2 = int(input('Choisir 2eme tour: '))
        #elif t2 > 2 or t2 < 0:
            #t1 = int(input('Tour 2 entrée non existante.\nChoisir 1ere tour: '))
            #t2 = int(input('Choisir 2eme tour: '))

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
        print('please try again')
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
    return moveCount, startTimeSecs, endTimeSecs
#    print('Game over!')
#    return moveCount

def playAgain(gameboard, n):
    playAgain = str(input('Souhaitez vous rejouer? y/n: '))
    if playAgain == "y":
        eraseAll(gameboard, n)
        eraseBoard(n)
        main()
    elif playAgain == "n":
        print('Thank you for playing!')
        return

## CANCEL HITS

def lastHit():
    return 0

def cancelLastHit():
    return 0

## GAME FILES

def save(gameboard, n):
    username = input('Enter your username: ')
    diskCount = n
    moveCount, startTimeSecs, endTimeSecs = gameLoop(gameboard, n)
    print(moveCount)
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
    return 0

def displayScores():
    return 0

# RECURSIVE SOLVE

def Draw(gameboard, t1, t2, n):
    topT1 = lastElem(gameboard, t1)
    topT2 = lastElem(gameboard, t2)
    eraseDisk(topT1, gameboard, n)
    #gameboard[t2].append(gameboard[t1].pop())
    drawDisk(topT2, gameboard, n, R,G,B)
    #gameboard[t3].append(lastElem(gameboard, t1))
    #gameboard[t1].pop()

def drawMe(gameboard, t1):
    drawBoard(a, R1, G1, B1)
    drawConfig(gameboard, a, R,G,B)
    startTimeSecs = time.mktime(time.localtime())
    while (checkVictory(gameboard, n) == False):
        for i in gameboard:
            print('Game over!')
            endTimeSecs = time.mktime(time.localtime())
        return moveCount, startTimeSecs, endTimeSecs
        popnDraw(gameboard, nt1, nt2, n)

def goSolveUrself(gameboard, t1, t3, n):
    maxSize = (2**n)-1
    solvedGame = [] #[[] for i in range(maxSize)]
    #T1Array = [] for i in range(maxSize)
    #T2Array = [] for i in range(maxSize)
    #assert len(gameboard[t1]) >= n
    if n == 0:
        return solvedGame
    if n == 1:
        #Draw(gameboard, t1, t3, n)
        gameboard[t3].append(gameboard[t1].pop())
        #gameboard[t1].pop()
        #gameboard[t3].append(gameboard[t1])
        #lastElem(gameboard, t1)gameboard[].pop()
        print(t1,'->',t3,':',gameboard)
        solvedGame.append(tuple([t1,t3]))
        #Draw(gameboard, lastElem(gameboard, t1), lastElem(gameboard, t3), n)
    else: # FINALLY FUCKING WORKS
          # I chose to use extend because appending a new tuple as a list made it very inconvenient to traverse
        t2 = 3 - t1 - t3 # t1+t3+t2 = 3
        #topT2 = lastElem(gameboard, t2)
        #Draw(gameboard, t1, t2, n)
        solvedGame.extend(goSolveUrself(gameboard, t1, t2, n-1))
        #Draw(gameboard, t1, t3, n)
        #Draw(gameboard, t1, t2, n)
        #solvedGame += goSolveUrself(gameboard, t1, t2, n-1)
        #goSolveUrself(gameboard, t1, t2, n-1) # move disk from source to aux
        solvedGame.extend(goSolveUrself(gameboard, t1, t3, 1))
        #Draw(gameboard, t2, t3, n)
        #Draw(gameboard, t1, t3, n)
        #solvedGame += goSolveUrself(gameboard, t1, t3, n-1)
        #goSolveUrself(gameboard, t1, t3, 1) # move disk from source to target
        solvedGame.extend(goSolveUrself(gameboard, t2, t3, n-1))
        #Draw(gameboard, t2, t3, n)
        #solvedGame += goSolveUrself(gameboard, t2, t3, n-1)
        #goSolveUrself(gameboard, t2, t3, n-1) # move disk from aux to target.
    return solvedGame
    #else:
        #eraseDisk(lastElem(gameboard, t2), gameboard, n)
        #drawDisk(lastElem(gameboard, t3), gameboard, n, R,G,B)
        #if len(gameboard[t1]) >= 1:

def autoPlayTurn(gameboard, n):
    solvedGame = goSolveUrself(gameboard, 0, 2, n)
    newGameboard = init(n)
    drawBoard(n, R1, G1, B1)
    drawConfig(newGameboard, n, R,G,B)
    for i, j in solvedGame:
        topT1 = lastElem(newGameboard, i)
        topT2 = lastElem(newGameboard, j)
        #drawConfig(newGameboard, n, R,G,B)
        if checkMove(newGameboard, i, j) == True:
            eraseDisk(topT1, newGameboard, n) # eraseDisk(lastElem(gameboard, t1), gameboard, n)
            newGameboard[i].pop()
            drawDisk(topT2, newGameboard, n, R,G,B) #drawDisk(lastElem(gameboard, t2), gameboard, n, R,G,B)
            newGameboard[j].append(topT1)
            drawBoard(n, R1, G1, B1)
            drawConfig(newGameboard, n, R,G,B)
    return newGameboard

def animateVictory(solvedGame, n):
    gameboard = init(n)
    drawBoard(n, R1, G1, B1)
    drawConfig(gameboard, n, R,G,B)
    print(solvedGame)
    for i, j in gameboard:
        topT1 = lastElem(gameboard, i)
        topT2 = lastElem(gameboard, j)
        eraseDisk(topT1, gameboard, n) # eraseDisk(lastElem(gameboard, t1), gameboard, n)
        #gameboard[i].pop()
        drawDisk(topT2, gameboard, n, R,G,B) #drawDisk(lastElem(gameboard, t2), gameboard, n, R,G,B)
        #gameboard[t2].append(topT1)

def readSolvedGame(gameboard, t1, t3, n):
    drawBoard(n, R1, G1, B1)
    drawConfig(gameboard, n, R,G,B)
    solvedGame = goSolveUrself(gameboard, 0, 2, n)
    moveCount = 0
    print(solvedGame)
    #lastElem(gameboard, i)
    #lastElem(gameboard, j)
    startTimeSecs = time.mktime(time.localtime())
    #drawBoard(n, R1, G1, B1)
    #drawConfig(solvedGame, n, R,G,B)
    #for i in solvedGame:
    #    for j in i:
            #eraseDisk(lastElem(gameboard, j), gameboard, n)
            #drawDisk(lastElem(gameboard, j), gameboard, n, R,G,B)
        #topT1 = lastElem(gameboard, i)
        #topT3 = lastElem(gameboard, j)
        #print(topT1)
        #print(j)
        #print(topT3)
        #print(j)
        #if checkMove(gameboard, i, j) == True:
        #eraseDisk(lastElem(gameboard, t1), gameboard, n)

        #drawDisk(topT3, gameboard, n, R,G,B)
        #Draw(gameboard, i, j, n)
        #print(i, j)
        #for j in i:
            #eraseDisk(lastElem(gameboard, j), gameboard, n)
            #drawDisk(lastElem(gameboard, j), gameboard, n, R,G,B)
            #Draw(gameboard, t1, t2, n)
    #print('Game over!')
    #endTimeSecs = time.mktime(time.localtime())
    #return moveCount, startTimeSecs, endTimeSecs

def recursiveLoop(gameboard, t1, t3, n):
    goSolveUrself(gameboard, t1, t3, n)
    moveCount = 0
    startTimeSecs = time.mktime(time.localtime())
    while i:
        if checkVictory(gameboard, n) == True:
            eraseDisk(lastElem(gameboard, t1), gameboard, n)
            drawDisk(lastElem(gameboard, t2), gameboard, n, R,G,B)
            gameboard[nt2].append(gameboard[nt1].pop())
            drawBoard(n, R1, G1, B1)
            drawConfig(gameboard, n, R,G,B)
    print('Game over!')
    endTimeSecs = time.mktime(time.localtime())
    return moveCount, startTimeSecs, endTimeSecs

## MAIN FUNCTION

def main():
    i = True
    while i:
        print('\n\n\t\tBienvenue dans les Tours de Hanoi!')
        #print(time.localtime([secs]))
        a = int(input('\nCombien de disques? '))
        gameboard = init(a)
        b = int(input('Voulez vous jouer, ou regarder jouer? (1/2) '))
        if b == 1:
            gameLoop(gameboard, a)
            save(gameboard, a)
            playAgain(gameboard, a)
        elif b == 2:
            #goSolveUrself(gameboard, 0, 2, a)
            #goSolveUrself(gameboard, 0, 2, a)
            #readSolvedGame(gameboard, 0, 2, a)
            #solvedGame = goSolveUrself(gameboard, 0, 2, a)
            autoPlayTurn(gameboard, a)
            #animateVictory(solvedGame, a)
            #recursiveLoop(gameboard, 0, 2, a)
            save(gameboard, a)
            playAgain(gameboard, a)
            print(gameboard)
        else:
            b = int(input('Choix non recconu.\nVoulez vous jouer, ou regarder jouer? (1/2)'))

main()
turtle.done()
