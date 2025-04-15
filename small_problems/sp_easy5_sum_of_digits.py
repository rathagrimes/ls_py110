# Write a function that takes one argument, a positive integer, and
# returns the sum of its digits.

def sum_digits(num):
    return sum([int(digit) for digit in str(num)])


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
