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
            self.sideCords = []
            self.setSides()

        self.cords2D = []
        self.update2DCords()


    def setSides(self):

        #X cords
        if self.scaleCords[0] == 0:
            self.sides.append(globals.cubeSides.get("left"))
        elif self.scaleCords[0] == 2:
            self.sides.append(globals.cubeSides.get("right"))

        #Z cords
        if self.scaleCords[2] == 0:
            self.sides.append(globals.cubeSides.get("back"))
        elif self.scaleCords[2] == 2:
            self.sides.append(globals.cubeSides.get("front"))

        #Y cords
        if self.scaleCords[1] == 0:
            self.sides.append(globals.cubeSides.get("top"))
        elif self.scaleCords[1] == 2:
            self.sides.append(globals.cubeSides.get("bottom"))




        numSides = len(self.sides)
        match numSides:
            case 1:
                self.sideCords.append([self.sides[0],1,1])
            case 2:
                #CHECKS IF BOTH ARE SIDEWALLS - rows will always be 1
                if self.sides[0] < 4 and self.sides[1] < 4:
                    #FRONT 2 WALLS
                    if globals.cubeSides.get("front") in self.sides:
                        #front left
                        if globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("left"), 1, 2])
                            self.sideCords.append([globals.cubeSides.get("front"), 1, 0])
                        #front right
                        else:
                            self.sideCords.append([globals.cubeSides.get("right"), 1, 0])
                            self.sideCords.append([globals.cubeSides.get("front"), 1, 2])
                    #BACK 2 WALLS 
                    else:
                        #back left
                        if globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("left"), 1, 0])
                            self.sideCords.append([globals.cubeSides.get("back"), 1, 2])
                        #back right
                        else:
                            self.sideCords.append([globals.cubeSides.get("right"), 1, 2])
                            self.sideCords.append([globals.cubeSides.get("back"), 1, 0])
                
                #THEY CONNECT SIDE TO TOP/BOTTOM 
                else:
                    #TOP
                    if globals.cubeSides.get("top") in self.sides:
                        #front middle top                      
                        if globals.cubeSides.get("front") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("front"), 0, 1])
                            self.sideCords.append([globals.cubeSides.get("top"), 2, 1])
                        
                        #back middle top
                        elif globals.cubeSides.get("back") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("back"), 0, 1])
                            self.sideCords.append([globals.cubeSides.get("top"), 0, 1])

                        #left middle top
                        elif globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("left"), 0, 1])
                            self.sideCords.append([globals.cubeSides.get("top"), 1, 0])
                            
                        #right middle top
                        else:
                            self.sideCords.append([globals.cubeSides.get("right"), 0, 1])
                            self.sideCords.append([globals.cubeSides.get("top"), 1, 2])

                    #BOTTOM
                    else:
                        #front middle bottom                      
                        if globals.cubeSides.get("front") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("front"), 2, 1])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 0, 1])
                        
                        #back middle bottom
                        elif globals.cubeSides.get("back") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("back"), 2, 1])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 2, 1])

                        #left middle bottom
                        elif globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("left"), 2, 1])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 0, 1])
                            
                        #right middle bottom
                        else:
                            self.sideCords.append([globals.cubeSides.get("right"), 2, 1])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 1, 2])

            case 3: #CORNER PIECES
                if globals.cubeSides.get("top") in self.sides:
                    #front--top corners
                    if globals.cubeSides.get("front") in self.sides:
                        #front-left-top                         
                        if globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("front"), 0, 0])
                            self.sideCords.append([globals.cubeSides.get("left"), 0, 2])
                            self.sideCords.append([globals.cubeSides.get("top"), 2, 0])

                        #front-right-top
                        else:
                            self.sideCords.append([globals.cubeSides.get("front"), 0, 2])
                            self.sideCords.append([globals.cubeSides.get("right"), 0, 0])
                            self.sideCords.append([globals.cubeSides.get("top"), 2, 2])

                    #back--top corners
                    else:
                        #back-left-top 
                        if globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("back"), 0, 2])
                            self.sideCords.append([globals.cubeSides.get("left"), 0, 0])
                            self.sideCords.append([globals.cubeSides.get("top"), 0, 0])

                        #back-right-top
                        else:
                            self.sideCords.append([globals.cubeSides.get("back"), 0, 0])
                            self.sideCords.append([globals.cubeSides.get("right"), 0, 2])
                            self.sideCords.append([globals.cubeSides.get("top"), 0, 2])
                    
                #BOTTOM CORNERS
                else:
                    #front--bottom corners
                    if globals.cubeSides.get("front") in self.sides:
                        #front-left-bottom                         
                        if globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("front"), 2, 0])
                            self.sideCords.append([globals.cubeSides.get("left"), 2, 2])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 0, 0])

                        #front-right-bottom
                        else:
                            self.sideCords.append([globals.cubeSides.get("front"), 2, 2])
                            self.sideCords.append([globals.cubeSides.get("right"), 2, 0])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 0, 2])

                    #back--bottom corners
                    else:
                        #back-left-bottom 
                        if globals.cubeSides.get("left") in self.sides:
                            self.sideCords.append([globals.cubeSides.get("back"), 2, 0])
                            self.sideCords.append([globals.cubeSides.get("left"), 2, 2])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 2, 2])

                        #back-right-bottom
                        else:
                            self.sideCords.append([globals.cubeSides.get("back"), 2, 2])
                            self.sideCords.append([globals.cubeSides.get("right"), 2, 0])
                            self.sideCords.append([globals.cubeSides.get("bottom"), 2, 0])

                    


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

        visibleSides = self.findVisibleSides()
        self.drawColours(screen, visibleSides)

        #edges
        for i in range(len(self.linesToDraw)):
            xCordStart = self.cords2D[self.linesToDraw[i][0]][0][0]
            yCordStart = self.cords2D[self.linesToDraw[i][0]][0][1]
    
            xCordEnd = self.cords2D[self.linesToDraw[i][1]][0][0]
            yCordEnd = self.cords2D[self.linesToDraw[i][1]][0][1]
    
            pygame.draw.line(screen, globals.WHITE, [xCordStart, yCordStart], [xCordEnd, yCordEnd])
        

    def findVisibleSides(self):
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

        return visibleSides

    def drawColours(self, screen, visibleSides):

        if visibleSides[0] == 'front':
            if globals.cubeSides.get("front") in self.sides:
                pygame.draw.polygon(screen, self.pickColour(globals.cubeSides.get("front")), [(self.cords2D[1][0]), (self.cords2D[3][0]), (self.cords2D[5][0]), (self.cords2D[7][0])])
        else:
            if globals.cubeSides.get("back") in self.sides:
                pygame.draw.polygon(screen, self.pickColour(globals.cubeSides.get("back")), [(self.cords2D[0][0]), (self.cords2D[2][0]), (self.cords2D[4][0]), (self.cords2D[6][0])])
        
        if visibleSides[1] == 'right':
            if globals.cubeSides.get("right") in self.sides:
                pygame.draw.polygon(screen, self.pickColour(globals.cubeSides.get("right")), [(self.cords2D[2][0]), (self.cords2D[3][0]), (self.cords2D[5][0]), (self.cords2D[4][0])])
        else:
            if globals.cubeSides.get("left") in self.sides:
                pygame.draw.polygon(screen, self.pickColour(globals.cubeSides.get("left")), [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])

        if visibleSides[2] == 'top':
            if globals.cubeSides.get("top") in self.sides:
                pygame.draw.polygon(screen, self.pickColour(globals.cubeSides.get("top")), [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[3][0]), (self.cords2D[2][0])])
        else:
            if globals.cubeSides.get("bottom") in self.sides:
                pygame.draw.polygon(screen, self.pickColour(globals.cubeSides.get("bottom")), [(self.cords2D[4][0]), (self.cords2D[5][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])


        #if globals.cubeSides.get("left") in self.sides:
        #   pygame.draw.polygon(screen, globals.RED, [(self.cords2D[0][0]), (self.cords2D[1][0]), (self.cords2D[7][0]), (self.cords2D[6][0])])
        #if globals.cubeSides.get("right") in self.sides:
        #    pygame.draw.polygon(screen, globals.ORANGE, [(self.cords2D[2][0]), (self.cords2D[3][0]), (self.cords2D[5][0]), (self.cords2D[4][0])])


    def pickColour(self, side):
        colourToDraw = (0,0,0)
        if side in self.sides:
            for cord in self.sideCords:
                if cord[0] == side:
                    colourIndex = globals.fullCube[cord[0]][cord[1]][cord[2]]
                    colourToDraw = globals.coloursDict.get(colourIndex)
        
    
        return colourToDraw


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
    