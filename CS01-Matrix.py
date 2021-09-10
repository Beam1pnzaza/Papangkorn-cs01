import numpy as np
MatrixOne = []
MatrixTwo = []
loop = 1
MatrixColumns = int(input("EnterYourColumns : "))
MatrixRows = int(input("EnterYourRows : "))
while( loop <2):
    print("EnterrYourMatrix",loop)
    for i in range(MatrixRows) :
        for j in range(MatrixColumns) :
            print("MatrixColumns [",i,",",j,"] :",end ="")
            if(loop == 1):
                MatrixOneInput = int(input(""))
                MatrixOne.append(MatrixOneInput)
            else:
                MatrixTwoInput = int(input(""))
                MatrixTwo.append(MatrixTwoInput)
    loop += 1
NumpyMatrixOne = np.asarray(MatrixOne)
NumpyMatrixTwo = np.asarray(MatrixTwo)
NewMatrixOne=NumpyMatrixOne.reshape(MatrixRows,MatrixColumns)
NewMatrixTwo=NumpyMatrixTwo.reshape(MatrixRows,MatrixColumns)
print(NewMatrixOne,"\n=========================")
print(NewMatrixTwo,"\n=========================")
sum = np.add(NewMatrixOne, NewMatrixTwo)
print(sum)