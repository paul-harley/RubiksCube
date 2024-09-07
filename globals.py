SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

#COLOURS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)


rotateAngle = 0
cubeScale = 200

#standard cube setup
def getBasicCube():
    return [
        [[0,0,0]],
        [[0,0,1]],
        [[1,0,0]],
        [[1,0,1]],
        [[1,1,0]],
        [[1,1,1]],
        [[0,1,0]],
        [[0,1,1]],
    ]

#GOING TO MAKE A SET OF INDICIES THAT A LINE SHOULD BE DRAWN BETWEEN
#DISTANCE IS A GOOD WAY TO FIGUIRE IT OUT I THINK

def findDis2Points3D(point1, point2):
    difX = (point1[0][0] - point2[0][0]) * (point1[0][0] - point2[0][0])
    difY = (point1[0][1] - point2[0][1]) * (point1[0][1] - point2[0][1])
    difZ = (point1[0][2] - point2[0][2]) * (point1[0][2] - point2[0][2])

    #technically for actual Distance this needs to be 
    #square rooted but i just need which number is smaller 
    #to draw a line between them - hypotenuse bigger doesnt need line
    return difX + difY + difZ


def linesToDrawIndicies():
    linesToDraw = []
    cubePoints = getBasicCube()
    for i in range(len(cubePoints)):
        for j in range(len(cubePoints)):
            if findDis2Points3D(cubePoints[i], cubePoints[j]) == 1:
                if [i,j] not in linesToDraw and [j,i] not in linesToDraw:
                    linesToDraw.append([i,j])
    return linesToDraw 