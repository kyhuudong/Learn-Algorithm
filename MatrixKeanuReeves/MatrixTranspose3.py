c = int(input("Enter the column size: "))
r = int(input("Enter the row size: "))

M = []

for i in range(r):
    M.append([0]*c)
    for j in range(c):
        print("M[",i,"][",j,"]",end=" "),
        M[i][j]=int(input(": "))


def transposeSquare(M,m):
    for i in range(r):
        for j in range(c):
            m[i][j] = M[j][i]

def transposeInplace(M):
    for i in range(r):
        for j in range(i+1,c):
            M[i][j] , M[j][i] = M[j][i], M[i][j]


m = [[0 for i in range(r)] for j in range(c)]

transposeSquare(M,m)
print(M)
transposeInplace(M)
print(M)
print(m)