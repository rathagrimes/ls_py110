# A triangle is classified as follows:
#
# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is different.
# Scalene: All three sides have different lengths.
#
# To be a valid triangle, the sum of the lengths of the two shortest
# sides must be greater than the length of the longest side, and every
# side must have a length greater than 0. If either of these conditions
# is not satisfied, the triangle is invalid.
#
# Write a function that takes the lengths of the three sides of a
# triangle as arguments and returns one of the following four strings
# representing the triangle's classification: 'equilateral',
# 'isosceles', 'scalene', or 'invalid'.

# approach:

# - first validate the triangle. Sort to find the longest side and
#   compare to the sum of the other two.
# - make a derivative array of diffs and use that to check for type


def triangle(*args):
    if len(args) != 3 or not all([isinstance(arg, (int, float)) for arg in args]):
        raise ValueError("Argument must be 3 numbers")

    # First validate all sides > 0
    if not all(args):
        return 'invalid'

    # Next validate lengths
    largest, *rest = sorted(args, reverse=True)
    if largest >= sum(rest):
        return 'invalid'

    # Now check triangle type
    diffs = [second - first for (first, second) in zip(args, args[1:])]
    if not any(diffs):
        return 'equilateral'
    if not all(diffs):
        return 'isosceles'
    return 'scalene'
        
    


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
