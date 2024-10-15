import globals

rotationsDict = {
    "right": 1,
    "left": -1, 
    "up": 2,
    "down": -2
}

class Puzzle:

    def __init__(self):
        self.fullCube = []
        self.resetCube()
        #self.fullCube = [
        #    [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
        #    [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 
        #    [[2, 2, 2], [2, 2, 2], [2, 2, 2]], 
        #    [[3, 3, 3], [3, 3, 3], [3, 3, 3]], 
        #    [[4, 3, 1], [5, 4, 4], [1, 2, 4]],
        #    [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        #]

    

    def resetCube(self):
        self.fullCube = []
        for sideID in range(6):
            sideOfCube = []
            for i in range(3):
                row = []
                for j in range(3):
                    row.append(sideID)
                sideOfCube.append(row)
            self.fullCube.append(sideOfCube)

    def rotateHorizontal(self, sideRotated, angleRotated, rowIndex):

        if sideRotated in globals.sideWalls:
            #index = globals.sideWalls.index(sideRotated)
            if angleRotated == rotationsDict.get("right"):   #RIGHT
                rowsBeingRotated = []
                for i in range(len(globals.sideWalls)):
                    rowsBeingRotated.append(self.fullCube[i][rowIndex])
                rowsBeingRotated.insert(0, rowsBeingRotated[len(rowsBeingRotated) - 1])
                rowsBeingRotated.pop()

                #saving change
                for i in range(4):
                    self.fullCube[i][rowIndex] = rowsBeingRotated[i]

                if rowIndex == 0:
                    self.fullCube[4] = self.fixPerpendicularSide('right', self.fullCube[4]) #CHANGING TOP SIDE 
            
            #rotate LEFT
            else:
                rowsBeingRotated = []
                for i in range(len(globals.sideWalls)):
                    rowsBeingRotated.append(self.fullCube[i][rowIndex])
                rowsBeingRotated.insert(len(rowsBeingRotated), rowsBeingRotated[0])
                rowsBeingRotated.pop(0)

                #saving change
                for i in range(4):
                    self.fullCube[i][rowIndex] = rowsBeingRotated[i]

                if rowIndex == 0:
                    self.fullCube[4] = self.fixPerpendicularSide('left', self.fullCube[4]) #CHANGING TOP SIDE 

                elif rowIndex == 2:
                    self.fullCube[5] = self.fixPerpendicularSide('left', self.fullCube[5]) #CHANGING BOTTOM SIDE 
    
    def rotateVertical(self, sideRotated, dirRotated, colIndex):
        if sideRotated in globals.sideWalls:
            if dirRotated ==  rotationsDict.get('up'):
                #SIDES THAT WILL BE AFFECTED
                #SIDE ENTERED - TOP - OPPOSITE OF SIDE ENTERED - BOTTOM- PERPENDICLAR SIDE
                colsBeingRotated = self.findColsBeingRotated(sideRotated, colIndex)

                #changing order of cols 
                colsBeingRotated.insert(0, colsBeingRotated[len(colsBeingRotated) - 1])
                colsBeingRotated.pop()
                print(colsBeingRotated)

                #saving changes
                self.saveColChanges(sideRotated, colIndex, colsBeingRotated)

    def saveColChanges(self, sideRotated, colIndex, colsToSave):
        
        #col specified
        for i in range(3):
            globals.fullPuzzle.fullCube[globals.cubeSides.get(sideRotated)][i][colIndex] = colsToSave[0][i]

        #top col
        for i in range(3):
            globals.fullPuzzle.fullCube[globals.cubeSides.get('top')][i][colIndex] = colsToSave[1][i]

        #opposite col specified
        for i in range(3):
            globals.fullPuzzle.fullCube[globals.cubeSides.get(sideRotated) + 2][i][-(colIndex) + 2] = colsToSave[2][i]

        #bottom col
        for i in range(3):
            globals.fullPuzzle.fullCube[globals.cubeSides.get('bottom')][i][colIndex] = colsToSave[3][i]


    def findColsBeingRotated(self, sideRotated, colIndex):
        allCols = []

        #col specified
        firstCol = []
        for i in range(3):
            firstCol.append(globals.fullPuzzle.fullCube[globals.cubeSides.get(sideRotated)][i][colIndex])
        allCols.append(firstCol)

        #col top side
        topCol = []
        for i in range(3):
            topCol.append(globals.fullPuzzle.fullCube[globals.cubeSides.get('top')][i][colIndex])
        allCols.append(topCol)

        #col opposite side to specified
        oppCol = []
        for i in range(3):
            oppCol.append(globals.fullPuzzle.fullCube[globals.cubeSides.get(sideRotated) + 2][i][colIndex])
        allCols.append(oppCol)

        #col bottom side
        bottomCol= []
        for i in range(3):
            bottomCol.append(globals.fullPuzzle.fullCube[globals.cubeSides.get('bottom')][i][colIndex])
        allCols.append(bottomCol)

        return allCols





    def fixPerpendicularSide(self, dirRotated, startingPos):
        newPos = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]

        oldRow = 0
        oldCol = 0

        if dirRotated == 'right':
            for newCol in range(3):
                for newRow in range(2, -1, -1):
                    newPos[newRow][newCol] = startingPos[oldRow][oldCol]
                    oldCol +=1
                    if oldCol == 3:
                        oldRow += 1
                        oldCol = 0

        #LEFT
        else:
            for newCol in range(2, -1, -1):
                for newRow in range(3):
                    newPos[newRow][newCol] = startingPos[oldRow][oldCol]
                    oldCol +=1
                    if oldCol == 3:
                        oldRow += 1
                        oldCol = 0

        return newPos
    



