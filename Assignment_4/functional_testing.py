def func_max_value(weed_matrix):
    row_len = len(weed_matrix)
    col_len = len(weed_matrix[0])

    col = []
    d = []

    for i in range(col_len + 1):
        col.append(0)

    for v in range(row_len + 1):
        d.append(col)

    for i in range(1, row_len + 1):
        for j in range(1, col_len + 1):
            d[i][j] = max(d[i - 1][j], d[i][j - 1]) + weed_matrix[i - 1][j - 1]

    return d[row_len][col_len]


# expected result == 6

weed_matrix1 = [[1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0, 1]]

print(func_max_value(weed_matrix1))
result1 = func_max_value(weed_matrix1)
if (result1 == 6):
    print("correct!")

# To test all 0 values (expected result = 0)

weed_matrix2 = [[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]

print(func_max_value(weed_matrix2))
result2 = func_max_value(weed_matrix2)
if (result2 == 0):
    print("correct!")

# To test all values 1  (expected result = r*c - 1)

weed_matrix3 = [[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]

print(func_max_value(weed_matrix3))
result3 = func_max_value(weed_matrix3)

if (result3 == (len(weed_matrix3) + len(weed_matrix3[0]) - 1)):
    print("correct!")

# Different values to change result (expected result = 3)

weed_matrix4 = [[0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0]]

print(func_max_value(weed_matrix4))
result4 = func_max_value(weed_matrix4)
if (result4 == 3):
    print("correct!")

# path with 1's (expected result = r*c - 1)

weed_matrix5 = [[1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1]]

print(func_max_value(weed_matrix5))
result5 = func_max_value(weed_matrix5)
if (result5 == (len(weed_matrix5) + len(weed_matrix5[0]) - 1)):
    print("correct!")

# random 1 and 0 (expected result = 8)

weed_matrix6 = [[1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1]]

print(func_max_value(weed_matrix6))
result6 = func_max_value(weed_matrix6)
if (result6 == 8):
    print("correct!") 

#1 row (expected result = 4)
weed_matrix7 = [[1, 1, 1, 0, 1, 0]]

print(func_max_value(weed_matrix7)) 
result7 = func_max_value(weed_matrix7)
if(result7 == 4):
  print("correct!") 

#no element (expected result = 0)
weed_matrix8 = [[]]

print(func_max_value(weed_matrix8)) 
result8 = func_max_value(weed_matrix8)
if(result8 == 0):
  print("correct!") 