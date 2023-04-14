
def func_max_value(weed_matrix):

    row_len = len(weed_matrix)
    col_len = len(weed_matrix[0])

    col = []
    d = []

    for i in range (col_len + 1):
        col.append(0)

    for v in range(row_len + 1):
        d.append(col)

    for i in range(1, row_len + 1):
        for j in range(1, col_len + 1):
            d[i][j] = max(d[i - 1][j], d[i][j - 1]) + weed_matrix[i - 1][j - 1]

    return d[row_len][col_len]

weed_matrix =  [[1, 0, 1, 0, 0, 0],
               [0, 1, 0, 1, 0, 0],
               [0, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 0, 1]]

print(func_max_value(weed_matrix))
