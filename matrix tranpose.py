matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[i][j] = matrix[j][i]

print(result)
