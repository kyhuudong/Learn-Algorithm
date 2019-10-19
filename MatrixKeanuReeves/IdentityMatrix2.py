r = int(input("Enter the row size: "))
c = int(input("Enter the column size: "))

M = []

for i in range(r):
    M.append([0]*c)
    for j in range(c):
        M[i][j] = int(input("Enter the element: "))

def CheckIndentityMatrix(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if(i==j and x[i][j]!=1):
                return False
            elif(i!=j and x[i][j]!=0):
                return False
    return True

print(M)
print(CheckIndentityMatrix(M))