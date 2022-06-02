from copy import deepcopy
import time
import os

START = 'S'
END = 'E'
OBSTACLE = '-'
TRAVELEDPATH = 'X'
SEEKEDPATH = 'O'
PLAYER = 'P'
speed = 0.5

path1 = [
            ["-", "-", "-", "-", "-", "-", END],
            ["-", "-", "-", "-", "-", " ", " "],
            ["-", " ", " ", " ", "-", " ", "-"],
            ["-", " ", "-", "-", " ", " ", "-"],
            ["-", " ", "-", "-", "-", " ", " "],
            ['-', " ", " ", START, "-", " ", " "],
        ]

path2 = [
            ["-", "-", "-", "-", "-", "-", END],
            ["-", " ", " ", " ", " ", " ", " "],
            ["-", " ", "-", " ", " ", " ", " "],
            ["-", " ", "-", " ", " ", " ", " "],
            ["-", START, "-", " ", " ", " ", " "],
            ['-', " ", " ", " ", "-", " ", " "],
        ]

path3 = [
            ["-", "-", "-", "-", "-", "-", END],
            ["-", " ", " ", "-", "-", " ", " "],
            ["-", " ", "-", " ", " ", "-", " "],
            ["-", " ", "-", " ", " ", "-", " "],
            ["-", " ", "-", " ", "-", " ", " "],
            ['-', " ", " ", " ", "-", " ", START],
        ]

path4 = [
            ["-", "-", "-", "-", "-", "-", END, " ", " ", " "],
            ["-", " ", " ", "-", "-", "-", " ", " ", "-", " "],
            ["-", " ", "-", " ", " ", "-", "-", " ", "-", " "],
            ["-", " ", "-", " ", " ", "-", " ", " ", " ", " "],
            ["-", " ", "-", " ", "-", " ", " ", " ", " ", " "],
            ['-', " ", " ", " ", "-", " ", " ", " ", " ", " "],
            ["-", " ", "-", " ", " ", "-", " ", " ", " ", " "],
            ["-", " ", "-", " ", "-", " ", " ", " ", " ", " "],
            ['-', START, " ", " ", "-", " ", " ", " ", " ", " "],
        ]

path5 = [
            [START, "-", "-", "-", "-", "-", " ", " ", " ", " "],
            ["-", " ", "-", "-", "-", END, " ", " ", "-", " "],
            ["-", " ", "-", " ", " ", "-", "-", " ", "-", " "],
            ["-", " ", "-", " ", "-", " ", " ", " ", " ", " "],
            ["-", " ", "-", "-", " ", " ", " ", " ", " ", " "],
            ['-', " ", " ", " ", "-", " ", " ", " ", " ", " "],
            ["-", " ", "-", "-", " ", "-", " ", " ", " ", " "],
            ["-", " ", "-", " ", "-", " ", " ", " ", " ", " "],
            ['-', " ", " ", " ", "-", " ", " ", " ", " ", " "],
        ]

pathChoices = {
    "path1":deepcopy(path1),
    "path2":deepcopy(path2),
    "path3":deepcopy(path3),
    "path4":deepcopy(path4),
    "path5":deepcopy(path5)
}

data = input("What path do u wanna try?")
if data in pathChoices:
    print("Okay")
    paths = pathChoices[data]
else:
    print("Not found")
    exit()

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')


startPathIndex = []
def findInPaths(item):
    for indexY, path in enumerate(paths):
        for indexX, i in enumerate(path):
            if i == item:
                return [indexX, indexY]
    
    return False

startPathIndex = findInPaths(START)
if startPathIndex == False:
    print(f"Harus ada start nya '{START}'")
    exit()

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

def getDistanceBetweenTwo(coordinate, coordinate2): # current agent coordinate index
    return [abs(coordinate2[0] - coordinate[0]), abs(coordinate2[1] - coordinate[1])]

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

finishCoordinate = findInPaths(END)

if finishCoordinate == False:
    print(f"Harus ada end nya '{END}'")
    exit()


print("Start Coordinate : "+str(startPathIndex))

print("Finish Coordinate : "+str(finishCoordinate))
print("<--------------->")
printTable(paths)

def pathReverse():
    global paths
    resultPaths = deepcopy(paths)
    totalCost = 0
    FinishReverse = False
    currentCoordinate = finishCoordinate.copy()
    timeBefore = time.time()
    while not FinishReverse:
        pathAround = checkAround(currentCoordinate)
        bestDistance = [100, 100]
        bestCoordinate = [0, 0]
        cost = 0
        for i in pathAround:
            value = i[0]
            if value != None and value != OBSTACLE:
                distanceCoordinate = getDistanceBetweenTwo(i[1], startPathIndex)
                restX = distanceCoordinate[0] - bestDistance[0]
                if restX <= bestDistance[1] - distanceCoordinate[1]:
                    cost = i[2]
                    bestDistance = distanceCoordinate
                    bestCoordinate = i[1]

        if bestDistance == [100, 100]:
            break

        totalCost += cost
        currentCoordinate = bestCoordinate
        resultPaths[bestCoordinate[1]][bestCoordinate[0]] = SEEKEDPATH
        print("---------------")
        printTable(resultPaths)
        print("Coordinate", currentCoordinate, sep=" : ")
        print("Cost",totalCost, sep=" : ")
        print("---------------")

        time.sleep(speed)

        if currentCoordinate == startPathIndex:
            FinishReverse = True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


    if FinishReverse:
        print("FINISH REVERSED!")
        # print("TIME : "+str(time.time() - timeBefore))
    else :
        print("Not Finish Reverse :(")
        print("I got stuck...")


def findPath():
    global paths
    resultPaths = deepcopy(paths)
    totalCost = 0
    currentCost = 0
    Finish = False
    currentCoordinate = startPathIndex.copy()
    timeBefore = time.time()
    while not Finish:
        pathAround = checkAround(currentCoordinate)
        bestDistance = [100, 100]
        bestCoordinate = [0, 0]
        for i in pathAround:
            value = i[0]
            coordinate = i[1]
            if value != None and value != OBSTACLE:
                if resultPaths[coordinate[1]][coordinate[0]] != TRAVELEDPATH:
                    distance = getDistanceBetweenTwo(coordinate, finishCoordinate)
                    restX = bestDistance[0] - distance[0] # rest x = best current distance x - current distance x
                    if restX >= distance[1] - bestDistance[1]: # if rest x is more than best current distance y - current distance y
                        bestDistance = distance
                        bestCoordinate = coordinate
                        currentCost = i[2]
                else:
                    continue
            else:
                continue
        
        if bestDistance == [100, 100]:
            break

        totalCost += currentCost
        resultPaths[currentCoordinate[1]][currentCoordinate[0]] = TRAVELEDPATH
        currentCoordinate = bestCoordinate
        resultPaths[bestCoordinate[1]][bestCoordinate[0]] = PLAYER
        print("---------------")
        printTable(resultPaths)
        print("---------------")
        print("Coordinate", currentCoordinate, sep=" : ")
        print("Cost", totalCost, sep=" : ")
        time.sleep(speed)
        os.system('cls' if os.name == 'nt' else 'clear')

        if currentCoordinate == finishCoordinate:
            Finish = True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            

    if Finish:
        print("FINISH!")
        # print("TIME : "+str(time.time() - timeBefore))
    else :
        print("Not Finish :(")
        print("I got stuck... trying finish reversed... in 5 seconds")
        timeLeft = 5
        while timeLeft > 0:
            print(f"{timeLeft} left\r")
            time.sleep(1)
            timeLeft -= 1
            
        pathReverse()

time.sleep(speed + 0.5)
findPath()





















    