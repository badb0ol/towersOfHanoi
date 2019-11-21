import turtle

## IMPORTANT VARIABLES FOR DRAWING

def init(n):
    t = 3 # tower constant
    a = [[] for i in range(t)] # 2d array generation
    #a = [[1],[6],[3]] debugging
    for i in range(n): # first cell
        a[0].append(n-i) # decrement disk nb in descending order
    #print(len(a[]))
    return(a)

def diskAmount(gameboard, nbTower):
    count = 0
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

def diskPos(gameboard, f, n):
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
    #if isEmpty(gameboard, nt1) == False:
    #    if isEmpty(gameboard, nt2) == True:
    #        return True
    #    elif firstElem(gameboard, nt2) > firstElem(gameboard, nt1):
    #        return True
    #return False
    return (isEmpty(gameboard, nt1) == False and (isEmpty(gameboard, nt2) == True or (firstElem(gameboard, nt2) > firstElem(gameboard, nt1))))

def checkVictory(gameboard, n):
    #moveCount = (2**n)+1
    if isEmpty(gameboard, 0) == True and isEmpty(gameboard, 1) == True:
        if firstElem(gameboard, 2) == n and lastElem(gameboard, 2) == 1:
            if diskAmount(gameboard, 2) == n:
                return True
    return False
    #if n%2 == 0:
    #    while i:
    #        if checkMove(gameboard, )
    #        checkMove(gameboard, 0, 1)
    #        checkMove(gameboard, 0, 2) or checkMove(gameboard, 2, 0)
    #        checkMove(gameboard, 1, 2)
    #else:
    #    while i:
    #        checkMove(gameboard, 0, 2)
    #        checkMove(gameboard, 0, 1)
    #        checkMove(gameboard, 1, 2)

## EXTRA FUNCTIONS

def firstElem(gameboard, nbTower):# FONCTION DISQUE_SUPERIEUR
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        if isEmpty(gameboard, nbTower) == True:
            return 0
        return gameboard[nbTower][0] #lastElem is the 1st element starting from the end
    return -1

def diskPosInList(gameboard, nDisk):
    nTower = diskPosition(gameboard, nDisk)
    for towerIndex, tower in enumerate(gameboard):
        if len(tower) >= 0:
            for diskIndex, disk in enumerate(tower):
                if nDisk == disk:
                    return diskIndex
    return -1

def lastElem(gameboard, nbTower):
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        if isEmpty(gameboard, nbTower) == True:
            return 0
        return gameboard[nbTower][-1]
    return -1

def checkInput(Alpha):
    return Alpha.isspace()

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

def drawBoard(n):
    boardSize = 30+80+(3*(40+(30*(n-1))))# 10px towers, gap of 20px between towers, biggestDisk = 40+(30*n-1)
    originX = (-100)-(30*n)
    originY = (-50)-(20*n)
    tHeight = (20*n)+20
    t = turtle.Turtle()
    turtle.ht()
    t.speed(10)
    t.penup()
    t.goto(originX,originY)
    t.pendown()
    i = 0
    while i < 2:
        t.forward(boardSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        i += 1
    t1 = (boardSize/4)
    t2 = (boardSize/2)
    t3 = ((boardSize/4)*3)
    t.penup()
    t.goto(originX+t1,originY+20) #goto tower 1
    t.pendown()

    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)

    t.penup()
    t.goto(originX+t2,originY+20) #goto tower 2
    t.pendown()

    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)

    t.penup()
    t.goto(originX+t3,originY+20) #goto tower 3
    t.pendown()

    t.forward(5)            #tower draw
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(tHeight)
    t.left(90)
    return t1, t2, t3

def drawDisk(nDisk, gameboard, n):
    t = turtle.Turtle()
    t.speed(10)
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
    print(dPos)
    if dPos == 0: # if destination tower = 1 and is empty
        t.penup()
        t.goto(originX+t1,originY+20+(g*20)) #goto tower 1
        t.pendown()
        t.forward(diskSize/2)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(diskSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.left(diskSize/2)
    elif dPos == 1: # if destination tower = 2 and is empty
        t.penup()
        t.goto(originX+t2,originY+20+(g*20)) #goto tower 1
        t.pendown()
        t.forward(diskSize/2)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(diskSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.left(diskSize/2)
    elif dPos == 2: # if destination tower = 3 and is empty
        t.penup()
        t.goto(originX+t3,originY+20+(g*20)) #goto tower 1
        t.pendown()
        t.forward(diskSize/2)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(diskSize)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.left(diskSize/2)

def eraseDisk(nDisk, gameboard, n):
    return 0

def drawConfig(gameboard, n):
    return 0

def eraseAll(gameboard, n):
    return 0

## MOVE FUNCTIONS

def readCoords(gameboard):
    i = True
    t1 = int(input('Choisir 1ere tour: '))
    t2 = int(input('Choisir 2eme tour: '))
    while i:
        if isEmpty(gameboard, t1) == True:
            print('1ere tour vide')
            t1 = int(input('Choisir 1ere tour: '))
        elif t1 > 2 or t2 < 0:
            t1 = int(input('Tour 1 entrée non existante.\nChoisir 1ere tour: '))
        elif t2 > 2 or t2 < 0:
            t2 = int(input('Tour 2 entrée non existante.\nChoisir 2eme tour: '))
        else:
            if checkMove(gameboard, t1, t2) == True:
                i = False
    return t1, t2

def playTurn(gameboard, n):
    t1, t2 = readCoords(gameboard)
    return 0

def gameLoop(gameboard, n):
    return 0

## CANCEL HITS

def lastHit():
    return 0

def cancelLastHit():
    return 0

## GAME FILES

def save():
    return 0

def readScores():
    return 0

def displayScores():
    return 0

## MAIN FUNCTION

def main():
    i = True
    while i:
        print('\n\n\t\tBienvenue dans les Tours de Hanoi!')
        a = int(input('\nCombien de disques? '))
        gameboard = init(a)
        drawBoard(a)
        for j in range(a+1):
            drawDisk(j, gameboard, a)
        b = int(input('Quelle tour souhaitez vous checker (0, 1, 2)? '))
        c = firstElem(gameboard, b)
        print('La tour', b,'a pour disque inferieur:', c)
        d = lastElem(gameboard, b)
        print('La tour', b,'a pour disque superieur:', d)
        e = diskAmount(gameboard, b)
        print('La tour', b,'contient', e,'disques')
        f = int(input('Quel disque cherchez vous? '))
        diskPos(gameboard, f, a)
        #g = diskPosition(gameboard, f)
        #g = diskPos(gameboard, f))
        #print('Le disque', f,'est situe sur la tour ', g)
        t1 = int(input('Choisir 1ere tour: '))
        t2 = int(input('Choisir 2eme tour: '))
        if checkMove(gameboard, t1, t2) == True:
            print('This move is authorized')
        else:
            print('This move is not authorized')
        if checkVictory(gameboard, a) == True:
            print('Game over!')
            i = False
        else:
            print('The game goes on!')
        print(readCoords(gameboard))

        drawBoard(a)
        d1 = int(input('Quel disque voulez vous placer? '))
        drawDisk(d1 ,gameboard, a)
        d2 = int(input('Quel disque voulez vous placer? '))
        drawDisk(d2 ,gameboard, a)
        d3 = int(input('Quel disque voulez vous placer? '))
        drawDisk(d3 ,gameboard, a)

        #print(playTurn(gameboard, a))
        i = False
        # i = True
        # while i:
        #   process_input()
        #   update()
        #   draw()

def game():
    i = True
    while i:
        game()
        playAgain = str(input('Souhaitez vous rejouer? y/n: '))
        if playAgain == "y":
            continue
        else:
            print('Thank you for playing!')
            i = False

main()
turtle.hideturtle()
turtle.done()
