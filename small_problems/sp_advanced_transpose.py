# Input: 2-level nested list of elements. Outer list has length h, inner
# lists all have length w.

# Output: New 2-level nested list of elements. Outer list has length w,
# inner lists all have length h.

# Assumptions:
# - All inner lists have the same length.
# - There is at least one row.

# Algorithm:
# 1. Find out the length of the first row = w
# 2. Outer loop: Iterate from 0 to w
# 3. Inter loop: Iterate from 0 to h
# 4. Build the new matrix.

def transpose(matrix):
    result = []
    # TODO: validate that the input is an non-empty list of non-empty lists

    # Columns of matrix will become rows of result.
    # Outer loop, to build rows of result, will therefore iterate over
    # columns of matrix.
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        result.append(new_row)
    return result

# List comprehension way to do the same thing
# return [[sub[i] for sub in matrix] for i in range(len(matrix[0]))]

# Clever!
# def transpose(matrix: list):
#     return([list(row) for row in zip(*matrix)])


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True


# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)
