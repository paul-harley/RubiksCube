SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

#COLOURS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)

coloursDict = {
        0: WHITE,
        1: RED,
        2: ORANGE,
        3: BLUE,
        4: YELLOW,
        5: GREEN
    }


rotateAngle = 0
cubeScale = 200



#TESTING STUFF
fullCube = []
for sideID in range(6):
    sideOfCube = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(sideID)
        sideOfCube.append(row)
    fullCube.append(sideOfCube)

cubeSides = {
            "left" : 0,
            "front" : 1,
            "right": 2,
            "back": 3,
            "top": 4,
            "bottom": 5
        }
sideWalls = ["left", "front", "right", "back"]


#ANGLES BEING ROTATED
# (1 h right) (-1 h left)
# (2 v up) (-2 v down)   

def rotateRight(sideRotated, angleRotated, sideWalls, rowToRotate):
    if sideRotated in sideWalls:
        index = sideWalls.index(sideRotated)
        if angleRotated == 1:   #RIGHT
            rowsBeingRotated = []
            for i in range(len(sideWalls)):
                rowsBeingRotated.append(fullCube[i][rowToRotate])
            rowsBeingRotated.insert(0, rowsBeingRotated[len(rowsBeingRotated) - 1])
            rowsBeingRotated.pop()
            
            #saving change
            for i in range(4):
                fullCube[i][rowToRotate] = rowsBeingRotated[i]

            if rowToRotate == 0:
                fullCube[4] = fixPerpendicularSide(fullCube[4]) #CHANGING TOP SIDE 


def fixPerpendicularSide(startingPos):
    newPos = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]

    oldRow = 0
    oldCol = 0
    for newCol in range(3):
        for newRow in range(2, -1, -1):
            newPos[newRow][newCol] = startingPos[oldRow][oldCol]
            oldCol +=1
            if oldCol == 3:
                oldRow += 1
                oldCol = 0
    
    return newPos


rotateRight("left", 1, sideWalls, 0)
print(fullCube)

