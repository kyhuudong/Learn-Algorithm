r = int(input("Enter the row size: "))
c = int(input("Enter the column size: "))

M = []

for i in range(r):
    M.append([0]*c)
    for j in range(c):
        print("M[",i,"][",j,"]: ",end="")
        M[i][j] = int(input())

def CheckCrossMatrix(m):
    if(r != c):
        return False
    else:
        for i in range(len(m)):
            for j in range(len(m)):
                if(i==j and M[i][j] == 0):
                    return False
                elif(i!=j and M[i][j]!=0):
                    return False
    return True

print(M)
print(CheckCrossMatrix(M))