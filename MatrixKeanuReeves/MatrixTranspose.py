x = [[12,7],
    [5,2],
    [7,10]]

result = [[0,0,0]
        ,[0,0,0]]

for i in range(len(x[0])):
    for j in range(len(x)):
        result[i][j] = x[j][i]

for r in result:
    print(r)


