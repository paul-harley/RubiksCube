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

    
    print(finalResult)
    return finalResult



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


#print(len(myMatrix)) #GIVES ROWS
#print(len(myMatrix[1])) #GIVES COL

multiplyMatrix(myMatrix, myMatrix2)
