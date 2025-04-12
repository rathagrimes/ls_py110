

# Build the rows of the new matrix by:
# a) Progress left to right through the columns
# b) Progress right to left through the rows
def rotate90(matrix):
    result = []
    for old_col_idx in range(len(matrix[0])):
        new_row = []
        # Iterate backwards through the rows
        for old_row_idx in range(len(matrix)-1, -1, -1):
            new_row.append(matrix[old_row_idx][old_col_idx])
        result.append(new_row)
    return result
            

# Using list comprehensions (from peer solutions)
#def rotate90(matrix: list):
#    return [[row[i] for row in reversed(matrix)] for i in range(len(matrix[0]))]
#    return [list(row) for row in zip(*reversed(matrix))]

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))


# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
