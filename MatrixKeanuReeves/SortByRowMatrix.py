M = [[4,6,34],
    [22,53,23],
    [11,12,23],
    [44,22,11]]



def Sort(a,b):
    a = a+b
    b = a-b
    a = a-b

def SortMatrixByRow(m):
    temp = [100]
    idx = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            idx+=1
            temp[idx] = m[i][j]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(temp[i] > temp[j]):
                Sort(temp[i],temp[j])
    idx = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            idx+=1
            M[i][j] = temp[idx]

print(M)
SortMatrixByRow(M)
print(M)

           


