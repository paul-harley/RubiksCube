import globals
import math

#COMMON MATRICES

orthographicProjectionMatrix = [
    [1,0,0],
    [0,1,0],
    [0,0,0]
]




def multiplyMatrix(matrixA, matrixB):
    
    #Checking if multipication is possible
    if len(matrixA[0]) != len(matrixB):
        return -1
    
    #Multiplying Them
    curentElement = 0
    finalResult = []
    row = []

    for i in range(len(matrixA)):       #Each row in first matrix
        row = []

        for k in range(len(matrixB[0])):  #Each col in second 
            curentElement = 0
            for j in range(len(matrixA[0])):
                curentElement += (matrixA[i][j] * matrixB[j][k])
            row.append(curentElement)

        finalResult.append(row)

    
    return finalResult


def rotateCube(cubePoints, axisToRotate, angle):

    if axisToRotate == 'x':

        rotateXDirection = [
            [1,       0,                    0       ],
            [0, math.cos(angle),    -math.sin(angle)],
            [0, math.sin(angle),    math.cos(angle) ]
        ]

        newPoints = []

        for point in cubePoints:
            newPoints.append(multiplyMatrix(point, rotateXDirection))

        return newPoints
        
    elif axisToRotate == 'y':
        
        rotateYDirection = [
            [math.cos(angle),  0 , math.sin(angle)],
            [       0,         1,         0       ],
            [-math.sin(angle), 0,  math.cos(angle)]
        ]

        newPoints = []

        for point in cubePoints:
            newPoints.append(multiplyMatrix(point, rotateYDirection))

        return newPoints

    if axisToRotate == 'z':
        
        rotateZDirection = [
            [math.cos(angle),  -math.sin(angle), 0],
            [math.sin(angle),  math.cos(angle),  0],
            [0,                     0,           1]
        ]

        newPoints = []

        for point in cubePoints:
            newPoints.append(multiplyMatrix(point, rotateZDirection))

        return newPoints

    



#TEST AREA
myMatrix = [     
    [4,2,-1], 
    [3,2,0]   
]

myMatrix2 = [        
    [0,1],    
    [2,3],
    [7,4]
]

myMatrix3 = [
    [-1,1,0]
]
#print(len(myMatrix)) #GIVES ROWS
#print(len(myMatrix[1])) #GIVES COL

#print(multiplyMatrix(myMatrix3, orthographicProjectionMatrix))
