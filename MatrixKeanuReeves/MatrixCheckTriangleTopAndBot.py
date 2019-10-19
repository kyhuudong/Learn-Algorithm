M1 = [
    [2,3,4],
    [0,5,7],
    [0,0,7]]

M2 = [[7,0,0],
      [7,5,0],
      [4,3,2]]


def TriangleTopMatrix(M):
    for i in range(1,len(M)):
        for j in range(i):
            if(M[i][j] != 0):
                return False
    return True

def TriangleBotMatrix(M):
    for i in range(len(M)):
        for j in range(i+1,len(M)):
            if(M[i][j] != 0):
                return False
    return True


print(TriangleTopMatrix(M1))
print(TriangleBotMatrix(M2))
