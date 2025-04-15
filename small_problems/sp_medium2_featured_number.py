# A featured number (something unique to this exercise) is an odd number
# that is a multiple of 7, with all of its digits occurring exactly once
# each. For example, 49 is a featured number, but 98 is not (it is not
# odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit
# 3 appears twice).
#
# Write a function that takes an integer as an argument and returns the
# next featured number greater than the integer. Issue an error message
# if there is no next featured number.
#
# NOTE: The largest possible featured number is 9876543201.

ERROR_MSG = ("There is no possible number that fulfills those requirements.")
MAX_FEATURED = 9876543201

def to_odd_multiple_of_7(num):
    while num % 2 == 0 or num % 7 > 0:
        num += 1
    return num

def check_unique(num):
    # Must be odd
    # if num % 2 == 0:
    #     return False
    # Must be a multiple of 7
    # Don't need this as calling function has it handled
    # if num % 7 > 0:
    #     return False
    # Check if digits are unique
    digits = list(str(num))
    return len(digits) == len(set(digits))

def next_featured(num):
    if num < 0:
        return ERROR_MSG
    candidate = to_odd_multiple_of_7(num + 1)
    while candidate <= MAX_FEATURED:
        if check_unique(candidate):
            return candidate
        candidate += 14
    return ERROR_MSG


print(next_featured(2) == 7)                    # True
print(next_featured(7) == 21)                   # True
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
