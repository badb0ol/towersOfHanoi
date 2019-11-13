def init(n):
    t = 3 # tower constant
    #a = []# 2d array generation
    a = [[] for i in range(t)]
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
    pos = 0
    pos = gameboard.index(numDisk)
    print(pos)
    return pos

    #for i in range(len(gameboard)):
    #    print(gameboard[i])
    #    for j in range(numDisk):
    #        print(gameboard[j])
    #        #if gameboard[i][j] == numDisk:
    #        pos = gameboard[i][j]

    #if gameboard[i][j] == numDisk:
    #    pos = gameboard[i][j]

def movement(gameboard, nt1, nt2):
    return 0 #allowMove

def victoryCondition(gameboard, n):
    return 0

def isInList(gameboard, elem):
    i = 0
    while i < len(gameboard):
        return elem in gameboard

def isEmpty(nbTower):
    if nbTower >= 0 and nbTower <= 2:
        for i in gameboard:
            return 0

def lastElem(gameboard, nbTower):
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        for i in gameboard:
            lastElem = i[-1] #lastElem is the 1st element starting from the end
            return lastElem
    else:
        return -1

def firstElem(gameboard, nbTower):# FONCTION DISQUE_SUPERIEUR
    if nbTower >= 0 and nbTower <= 2: # check towerNb is correct
        for i in gameboard:
            firstElem = i[0] #firstElem is simply on index 0
            return firstElem
    else:
        return -1

def diskPos(gameboard,f):
    if isInList(gameboard, f) == True:
        g = diskPosition(gameboard, f)
        print('Le disque', f,'est situe sur la tour ', g)
    else:
        return -1

def main():
    i = True
    while i:
        print('\n\n\t\tBienvenue dans les Tours de Hanoi!')
        a = int(input('\nCombien de disques? '))
        gameboard = init(a)
        b = int(input('Quelle tour souhaitez vous checker (0, 1, 2)? '))
        c = firstElem(gameboard, b)
        print('La tour', b,'a pour disque superieur: ', c)
        d = lastElem(gameboard, b)
        print('La tour', b,'a pour disque inferieur: ', d)
        e = diskAmount(gameboard, b)
        print('La tour', b,'contient', e,'disques')
        f = int(input('Quel disque cherchez vous? '))
        diskPos(gameboard,f)
        i = False
        #game()

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
