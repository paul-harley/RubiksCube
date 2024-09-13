import matrix
import globals
import math
import pygame

class Cube:
    def __init__(self, scale, size, scaleCords):

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
        # front - 1,3,5,7
        # top- 0,1,3,2 
        self.sides = []

        self.linesToDraw = self.linesToDrawIndicies()
        self.scale = scale
        self.size = size
        self.scaleCords = scaleCords
        self.scalePos()

        if self.size == 's': 
            self.setSides()

        self.cords2D = []
        self.update2DCords()


    def setSides(self):

        #X cords
        if self.scaleCords[0] == 0:
            self.sides.append(globals.cubeSides.get("left"))
        elif self.scaleCords[0] == 2:
            self.sides.append(globals.cubeSides.get("right"))

        #Y cords
        if self.scaleCords[1] == 0:
            self.sides.append(globals.cubeSides.get("top"))
        elif self.scaleCords[1] == 2:
            self.sides.append(globals.cubeSides.get("bottom"))


        #Z cords
        if self.scaleCords[2] == 0:
            self.sides.append(globals.cubeSides.get("back"))
        elif self.scaleCords[2] == 2:
            self.sides.append(globals.cubeSides.get("front"))


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
                        p[0][i] += globals.cubeScale*(self.scaleCords[0]/3)
                    #Y
                    if i == 1:
                        p[0][i] += globals.cubeScale*(self.scaleCords[1]/3)
                    #Z
                    if i == 2:
                        p[0][i] += globals.cubeScale*(self.scaleCords[2]/3)

        
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


        visibleSides = []
        if self.position[1][0][2] > self.position[0][0][2]:
            visibleSides.append("front")
        else:
            visibleSides.append("back")

        if self.position[2][0][2] > self.position[0][0][2]:
            visibleSides.append("right")
        else:
            visibleSides.append("left")

        if self.position[1][0][2] > self.position[7][0][2]:
            visibleSides.append("top")
        else:
            visibleSides.append("bottom")

        self.drawColours(screen, visibleSides)

        #edges
        for i in range(len(self.linesToDraw)):
            xCordStart = self.cords2D[self.linesToDraw[i][0]][0][0]
            yCordStart = self.cords2D[self.linesToDraw[i][0]][0][1]
    
            xCordEnd = self.cords2D[self.linesToDraw[i][1]][0][0]
            yCordEnd = self.cords2D[self.linesToDraw[i][1]][0][1]
    
            pygame.draw.line(screen, globals.WHITE, [xCordStart, yCordStart], [xCordEnd, yCordEnd])
        


        #JUST TESTING DIFFERENT SHAPES

        
        #top plane
        #pygame.draw.polygon(screen, globals.RED, [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[3][0]), (self.cords2D[2][0])])
        
        #bottom plane
        #pygame.draw.polygon(screen, globals.RED, [(self.cords2D[4][0]), (self.cords2D[5][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])

        #right plane
        #pygame.draw.polygon(screen, globals.RED, [(self.cords2D[2][0]), (self.cords2D[3][0]), (self.cords2D[5][0]), (self.cords2D[4][0])])

        #left plane
        #pygame.draw.polygon(screen, globals.RED, [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])


    #GOING TO MAKE A SET OF INDICIES THAT A LINE SHOULD BE DRAWN BETWEEN
    #DISTANCE IS A GOOD WAY TO FIGUIRE IT OUT I THINK

    def drawColours(self, screen, visibleSides):
        if visibleSides[0] == 'front':
            if globals.cubeSides.get("front") in self.sides:
                pygame.draw.polygon(screen, globals.WHITE, [(self.cords2D[1][0]), (self.cords2D[3][0]), (self.cords2D[5][0]), (self.cords2D[7][0])])
        else:
            if globals.cubeSides.get("back") in self.sides:
                pygame.draw.polygon(screen, globals.RED, [(self.cords2D[0][0]), (self.cords2D[2][0]), (self.cords2D[4][0]), (self.cords2D[6][0])])
        
        if visibleSides[1] == 'right':
            if globals.cubeSides.get("right") in self.sides:
                pygame.draw.polygon(screen, globals.ORANGE, [(self.cords2D[2][0]), (self.cords2D[3][0]), (self.cords2D[5][0]), (self.cords2D[4][0])])
        else:
            if globals.cubeSides.get("left") in self.sides:
                pygame.draw.polygon(screen, globals.BLUE, [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])

        if visibleSides[2] == 'top':
            if globals.cubeSides.get("top") in self.sides:
                pygame.draw.polygon(screen, globals.GREEN, [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[3][0]), (self.cords2D[2][0])])
        else:
            if globals.cubeSides.get("bottom") in self.sides:
                pygame.draw.polygon(screen, globals.YELLOW, [(self.cords2D[4][0]), (self.cords2D[5][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])


        #if globals.cubeSides.get("left") in self.sides:
        #   pygame.draw.polygon(screen, globals.RED, [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])
        #if globals.cubeSides.get("right") in self.sides:
        #    pygame.draw.polygon(screen, globals.ORANGE, [(self.cords2D[2][0]), (self.cords2D[3][0]), (self.cords2D[5][0]), (self.cords2D[4][0])])


        

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

