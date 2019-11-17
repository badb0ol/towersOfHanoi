import turtle

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
        # works except value of tower = 3 because 3 zeros in array when empty
        return len(gameboard[nbTower])

def diskPosition(gameboard, numDisk):
    for i in gameboard:
        if len(i) >= 0:
            if numDisk in i:
                return gameboard.index(i)
    return -1

def diskPos(gameboard, f, a):
    z = True
    while z:
        if f <= 0:
            print('disque trop petit')
            f = int(input('Quel disque cherchez vous? '))
        z = False
    if isInList(gameboard, f, a) == True:
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
            if diskAmount(gameboard, 2) == n
            return True
    else:
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

## MAIN FUNCTION

def main():
    i = True
    while i:
        print('\n\n\t\tBienvenue dans les Tours de Hanoi!')
        a = int(input('\nCombien de disques? '))
        gameboard = init(a)
        b = int(input('Quelle tour souhaitez vous checker (0, 1, 2)? '))
        c = firstElem(gameboard, b)
        print('La tour', b,'a pour disque superieur:', c)
        d = lastElem(gameboard, b)
        print('La tour', b,'a pour disque inferieur:', d)
        e = diskAmount(gameboard, b)
        print('La tour', b,'contient', e,'disques')
        f = int(input('Quel disque cherchez vous? '))
        diskPos(gameboard, f, a)
        #g = diskPosition(gameboard, f)
        #g = diskPos(gameboard, f))
        #print('Le disque', f,'est situe sur la tour ', g)
        t1 = int(input('Choisir 1ere tour: '))
        t2 = int(input('Choisir 2eme tour: '))
        print(checkMove(gameboard, t1, t2))
        print(checkVictory(gameboard, a))
        print(gameboard)
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
