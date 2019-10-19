A = [[1,4,5],
    [-5,8,9],
    [5,3,5]]

print("A=",A)
print("A[1]=" , A[1])
print("A[0][2]=" , A[0][2])
print("A[1][-1]=",A[1][-1])

column = []
for row in A:
    column.append(row[1])

print("3rd column =",column)