#Ma tran don vi

x = [[1,0,0],
    [0,1,1],
    [0,0,1]]

def CheckIdentityMatrix(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if (i==j and x[i][j]!=1):
                return False
            elif (i!=j and x[i][j] !=0):
                return False   
    return True

print(CheckIdentityMatrix(x))