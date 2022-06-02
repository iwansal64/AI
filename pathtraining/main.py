def findInPaths(item):
    for indexY, path in enumerate(paths):
        for indexX, i in enumerate(path):
            if i == item:
                return [indexX, indexY]
    
    return False

def checkPath(pathAround, xPlus, yPlus, coordinate):
    value = ''

    cost = 0
    if yPlus != 0 and xPlus != 0:
        cost = 14
    else:
        cost = 10
    
    try:
        yVal = coordinate[1] + yPlus
        xVal = coordinate[0] + xPlus
        if yVal < 0 or xVal < 0:
            value = None
        else :
            value = paths[yVal][xVal]
    except:
        value = None

    pathAround.append([value, [xVal, yVal], cost])

def checkAround(coordinate): # current agent coordinate index
    pathAround = []
    checkPath(pathAround, 1, 0, coordinate) # kanan
    checkPath(pathAround, 1, 1, coordinate) # kanan bawah
    checkPath(pathAround, 0, 1, coordinate) # bawah
    checkPath(pathAround, -1, 1, coordinate) # kiri bawah
    checkPath(pathAround, -1, 0, coordinate) # kiri
    checkPath(pathAround, -1, -1, coordinate) # kiri atas
    checkPath(pathAround, 0, -1, coordinate) # atas
    checkPath(pathAround, 1, -1, coordinate) # kanan atas

    return pathAround

def printTable(table):
    for row in table:
        for column in row:
            print(column, end=" ")
        print()

from copy import deepcopy
import random
import time

START = "S"
PLAYER = "P"
TRAVELEDPATH = "X"
FINISH = "F"


paths1 = [
            [START," "," "   ," "," "," "],
            [" "  ," "," "   ," "," "," "],
            [" "  ," "," "   ," "," "," "],
            [" "  ," ",FINISH," "," "," "],
            [" "  ," "," "   ," "," "," "],
        ]

paths = deepcopy(paths1)

finished = False

curpos = findInPaths(START)
finsihpos = findInPaths(FINISH)
print(finsihpos)
time.sleep(5)
traveledpath = []
x = 0
resultPaths = deepcopy(paths)
steps = [0]
while True:
    cursteps = 0
    beforeDistance = []
    while not finished:
        around = checkAround(curpos)
        nextCoordinate = []
        around = [x for x in around if x[0] != None]
        for index, path in enumerate(around):
            pos = path[1]
            cost = path[2]
            path = path[0]
            if index <= len(around) - 2:
                if random.randint(0, 1) == 1:
                    nextCoordinate = pos
                    break
                else:
                    continue
            else:
                nextCoordinate = pos
            

        resultPaths[curpos[1]][curpos[0]] = " "
        curpos = nextCoordinate
        resultPaths[curpos[1]][curpos[0]] = PLAYER
        printTable(resultPaths)
        time.sleep(0.5)
        cursteps += 1

        if curpos == finsihpos:
            print("STEPS : "+str(cursteps))
            curpos = findInPaths(START)
            steps.append(cursteps)
            resultPaths[finsihpos[1]][finsihpos[0]] = FINISH
            cursteps = 0
            with open(r'D:\Dev\Python\Codev2\AI\pathtraining\record\stepsRecord.txt', 'w+') as f:
                f.write('steps = '+str(steps))
            time.sleep(1)
            break


