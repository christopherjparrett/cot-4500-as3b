import numpy as np

def gaussianElim(inputMatrix):
    #scale everything so first row is 1
    newMatrix = inputMatrix
    divisor = newMatrix[0][0]
    for x in range(len(newMatrix)):
        for y in range(len(newMatrix[x])):
            newMatrix[x][y]/=divisor

    correctRows=1
    for x in range(len(newMatrix)-1): #now we must make more zeros
        for y in range(correctRows,len(newMatrix)): #we remove the cth column
            if(newMatrix[y][correctRows-1]!=0):
                #this row must be corrected
                multiplier = newMatrix[y][correctRows-1]/newMatrix[correctRows-1][correctRows-1]
                for m in range(correctRows-1,len(newMatrix[y])):
                    newMatrix[y][m]-= multiplier*newMatrix[correctRows-1][m]
        correctRows+=1
    for x in range(len(newMatrix)-1):
        temp = newMatrix[x][x]
        for y in range(x,len(newMatrix)+1):
            newMatrix[x][y]/=temp
    backSub(newMatrix)
    #print(newMatrix)

def backSub(inputMatrix):
    values = [0 for x in range(len(inputMatrix))]
    crigne = len(inputMatrix)-1
    for x in range(len(inputMatrix)-1,-1,-1):
        temp=0
        for y in range(crigne,x,-1):
            temp += values[y]*inputMatrix[x][y]
        values[x] = (inputMatrix[x][-1]-temp)/inputMatrix[x][x]
    print(values)
    

def LUDecomp(inputMatrix):
    identityMatrix = [[0 for x in range(len(inputMatrix))] for y in range(len(inputMatrix))]
    newMatrix = inputMatrix
    for x in range(len(inputMatrix)):
        identityMatrix[x][x] =1
    correctRows=1
    
    #print(identityMatrix)
    for x in range(len(newMatrix)-1): #now we must make more zeros
        for y in range(correctRows,len(newMatrix)): #we remove the cth column
            if(newMatrix[y][correctRows-1]!=0):
                #this row must be corrected
                multiplier = newMatrix[y][correctRows-1]/newMatrix[correctRows-1][correctRows-1]
                
                identityMatrix[y][correctRows-1] =  multiplier
                for m in range(correctRows-1,len(newMatrix[y])):
                    newMatrix[y][m]-= multiplier*newMatrix[correctRows-1][m]
        correctRows+=1
        
    #print determinant
    det=1
    for x in range(len(newMatrix)):
        det*= newMatrix[x][x]
    print(det)
    print()

    for x in identityMatrix:
        print(x)
    print()


    for x in newMatrix:
        print(x)
            
def diagonalDeterminance(inputMatrix):
    for x in range(len(inputMatrix)):
        #looking at each row we find the max that isnt pivot
        max=-999999
        for y in range(len(inputMatrix[x])):
            if(x!=y and max<inputMatrix[x][y]):
                max=inputMatrix[x][y]
        if(max>inputMatrix[x][x]):
            print("nah")
            return
    print("yeah")
    return

def positiveDeter(matrix):
    # Calculate the eigenvalues of the matrix
    eigenvalues = np.linalg.eigvals(matrix)
    # Check if all eigenvalues are positive
    for x in range(len(matrix)):
        if eigenvalues[x] <= 0:
            print("Not Pos Deter")
            return
    print("Pos Deter")
    return 

#test cases

gaussMatrix = [[2,-1,1,6],[1,3,1,0],[-1,5,4,-3]]
# gaussMatrix2 = [[2,3,-4,-5],[5,2,3,16],[3,6,1,-2]]
# gaussMatrix3 = [[1,2,1,7],[2,-1,1,4],[3,1,1,10]]
print()
gaussianElim(gaussMatrix)
print()

# backSub([[1,2,1,7],[0,-5,-1,-10],[0,0,-1,-1]])

#number 2
LUDMatrix = [[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]
# LUD2 = [[2,4,3,5],[-4,-7,-5,-8],[6,8,2,9],[4,9,-2,14]]
LUDecomp(LUDMatrix)
print()

#number 3
Diag = [[9,0,5,2,1],[3,9,1,2,1],[0,1,7,2,3],[4,2,3,12,2],[3,2,4,0,8]]
# diag2 = [[7,2,0],[3,5,-1],[0,5,-6]]
diagonalDeterminance(Diag)
print()

#number 4
posDef = np.array([[2,2,1],[2,3,0],[1,0,2]])
positiveDeter(posDef)