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
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[i][j] == numDisk:
                return i

def diskPos(gameboard,f):
    z = True
    while z:
        if f <= 0:
            print('disque trop petit')
            f = int(input('Quel disque cherchez vous? '))
        elif f > (len(gameboard)+1):
            print('disque trop grand')
            f = int(input('Quel disque cherchez vous? '))
        else:
            z = False
    if isInList(gameboard, f) == True:
        g = diskPosition(gameboard, f)
        print('Le disque', f,'est situe sur la tour', g)
    else:
        return -1

def movement(gameboard, nt1, nt2):
    return 0 #allowMove

def victoryCondition(gameboard, n):
    return 0

## EXTRA FUNCTIONS


def firstElem(gameboard, nbTower):# FONCTION DISQUE_SUPERIEUR
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        for i in gameboard:
            lastElem = i[0] #lastElem is the 1st element starting from the end
        return lastElem
    return -1

def lastElem(gameboard, nbTower):
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        for i in range(len(nbTower)):
            for j in range(len(gameboard)):
                lastElem = i[-1] #lastElem is the 1st element starting from the end
            return lastElem
    else:
        return -1

def checkInput(Alpha):
    return Alpha.isspace()

def isEmpty(nbTower):
    if nbTower >= 0 and nbTower <= 2:
        for i in gameboard:
            return 0

def isInList(gameboard, elem):
    if elem <= 0 or elem > len(gameboard):
        return False
    else:
        for i in range(len(gameboard)):
            if elem in gameboard[i]:
                return True
        return False


## MAIN FUNCTION


def main():
    i = True
    while i:
        print('\n\n\t\tBienvenue dans les Tours de Hanoi!')
        a = int(input('\nCombien de disques? '))
        gameboard = init(a)
        print(gameboard)
        b = int(input('Quelle tour souhaitez vous checker (0, 1, 2)? '))
        c = firstElem(gameboard, b)
        print('La tour', b,'a pour disque superieur:', c)
        d = lastElem(gameboard, b)
        print('La tour', b,'a pour disque inferieur:', d)
        e = diskAmount(gameboard, b)
        print('La tour', b,'contient', e,'disques')
        f = int(input('Quel disque cherchez vous? '))
        diskPos(gameboard, f)
        #g = diskPosition(gameboard, f)
        #g = diskPos(gameboard, f))
        #print('Le disque', f,'est situe sur la tour ', g)
        print(gameboard)
        i = False

        # i = True
        # while i:
        #   process_input()
        #   update()
        #   draw()
        #

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
