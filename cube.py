import matrix
import globals
import math
import pygame

class Cube:
    def __init__(self, scale, size):

        #Basic cube shape
        self.position = [
            [[0,0,0]],
            [[0,0,1]],
            [[1,0,0]],
            [[1,0,1]],
            [[1,1,0]],
            [[1,1,1]],
            [[0,1,0]],
            [[0,1,1]],
        ]
        self.linesToDraw = self.linesToDrawIndicies()
        self.scale = scale
        self.size = size
        self.scalePos()
        

        self.cords2D = []
        self.update2DCords()


    def scalePos(self):
        if self.size == 'b':
            for p in self.position:
                for i in range(3):
                    p[0][i] = p[0][i] * self.scale
        elif self.size == 's':
            #smallCubes
            for p in self.position:
                for i in range(3):
                    p[0][i] = (p[0][i] * (globals.cubeScale/3))
                    #CONTROLS X CORDS
                    if i == 0:
                        p[0][i] += globals.cubeScale*(0/3)
                    #Y
                    if i == 1:
                        p[0][i] += globals.cubeScale*(0/3)
                    #Z
                    if i == 2:
                        p[0][i] += globals.cubeScale*(2/3)

        
    def update2DCords(self):
        self.cords2D.clear()
        for p in self.position:
            self.cords2D.append(matrix.multiplyMatrix(p, matrix.orthographicProjectionMatrix))

        for p in self.cords2D:
            p[0][0] += globals.SCREEN_WIDTH/2
            p[0][1] += globals.SCREEN_HEIGHT/4
            p[0].pop()


    def rotateCube(self, axisToRotate, angle):

        if axisToRotate == 'x':

            rotateXDirection = [
                [1,       0,                    0       ],
                [0, math.cos(angle),    -math.sin(angle)],
                [0, math.sin(angle),    math.cos(angle) ]
            ]

            newPoints = []

            for point in self.position:
                newPoints.append(matrix.multiplyMatrix(point, rotateXDirection))

            self.position = newPoints

        elif axisToRotate == 'y':

            rotateYDirection = [
                [math.cos(angle),  0 , math.sin(angle)],
                [       0,         1,         0       ],
                [-math.sin(angle), 0,  math.cos(angle)]
            ]

            newPoints = []

            for point in self.position:
                newPoints.append(matrix.multiplyMatrix(point, rotateYDirection))

            self.position = newPoints

        if axisToRotate == 'z':

            rotateZDirection = [
                [math.cos(angle),  -math.sin(angle), 0],
                [math.sin(angle),  math.cos(angle),  0],
                [0,                     0,           1]
            ]

            newPoints = []

            for point in self.position:
                newPoints.append(matrix.multiplyMatrix(point, rotateZDirection))

            self.position = newPoints

    def draw(self, screen):
        #verticies
        for p in self.cords2D:
            pygame.draw.circle(screen, globals.WHITE, (p[0][0], p[0][1]), 2)

        #edges
        for i in range(len(self.linesToDraw)):
            xCordStart = self.cords2D[self.linesToDraw[i][0]][0][0]
            yCordStart = self.cords2D[self.linesToDraw[i][0]][0][1]
    
            xCordEnd = self.cords2D[self.linesToDraw[i][1]][0][0]
            yCordEnd = self.cords2D[self.linesToDraw[i][1]][0][1]
    
            pygame.draw.line(screen, globals.WHITE, [xCordStart, yCordStart], [xCordEnd, yCordEnd])

    #GOING TO MAKE A SET OF INDICIES THAT A LINE SHOULD BE DRAWN BETWEEN
    #DISTANCE IS A GOOD WAY TO FIGUIRE IT OUT I THINK

    def findDis2Points3D(self, point1, point2):
        difX = (point1[0][0] - point2[0][0]) * (point1[0][0] - point2[0][0])
        difY = (point1[0][1] - point2[0][1]) * (point1[0][1] - point2[0][1])
        difZ = (point1[0][2] - point2[0][2]) * (point1[0][2] - point2[0][2])

        #technically for actual Distance this needs to be 
        #square rooted but i just need which number is smaller 
        #to draw a line between them - hypotenuse bigger doesnt need line
        return difX + difY + difZ


    def linesToDrawIndicies(self):
        linesToDraw = []
        cubePoints = self.position
        for i in range(len(cubePoints)):
            for j in range(len(cubePoints)):
                if self.findDis2Points3D(cubePoints[i], cubePoints[j]) == 1:
                    if [i,j] not in linesToDraw and [j,i] not in linesToDraw:
                        linesToDraw.append([i,j])
        return linesToDraw 
