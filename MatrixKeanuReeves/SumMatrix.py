M = [[1,2,2],[1,1,1],[1,1,1]]

sum = 0

for i in range(len(M)):
    for j in range(len(M)):
        sum = sum + M[i][j]

print(sum)