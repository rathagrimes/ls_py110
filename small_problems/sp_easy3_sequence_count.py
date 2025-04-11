# Inputs: (1) count (int > 0), (2) factor (any int)
# Output: List of ints of length 'count'
# List starts with 'factor' and every element is a multiple of 'factor'
#
# Approach:
# 1) create a range of the appropriate length that starts with 1
# 2) multiple each element of the range by the factor using a list comprehension

def sequence(count, factor):
    # Initial version
    # base = range(1, count + 1)
    # transformed = [val * factor for val in base]
    # print (transformed)
    # return transformed

    # Cleaned up
    return [val * factor for val in range(1, count + 1)]


print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
