# PART 1
#
# Write a function that rotates a list by moving the first element to
# the end of the list. Do not modify the original list; return a new
# list instead.
# - If the input is an empty list, return an empty list.
# - If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.


def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    return lst[1:] + lst[:1]



# All of these examples should print True

print("PART 1")
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])


# PART 2
#
# Write a function that rotates the last count digits of a number. To
# perform the rotation, move the first of the digits that you want to
# rotate to the end and shift the remaining digits to the left.

# Assumption: Positive numbers only

# Input: int
# Output: int

# Approach: Reuse rotate_list
# 1. Convert input to string
# 2. Convert string to list
# 3. Split the list into 2 parts, a prefix and a suffix, based on 'count'
# 4. Perform rotate_list on the suffix list
# 5. Append the lists back together
# 6. Join back to a string
# 7. Convert back to an int

def rotate_rightmost_digits(number, count):
    if not isinstance(number, int) or number < 0:
        raise ValueError(f"Positive integer required for 'number': {number} found")
    if not isinstance(count, int) or number < 0:
        raise ValueError(f"Positive integer required for 'count': {count} found")

    lst = list(str(number))
    prefix, suffix = lst[:-count], lst[-count:]

    lst = prefix + rotate_list(suffix)

    return int(''.join(lst))

print("PART 2")
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True


# PART 3

# Take the number 735291 and rotate it by one digit to the left, getting 352917.
# Next, keep the first digit fixed in place and rotate the remaining digits to
# get 329175. Keep the first two digits fixed in place and rotate again to get
# 321759. Keep the first three digits fixed in place and rotate again to get
# 321597. Finally, keep the first four digits fixed in place and rotate the
# final two digits to get 321579. The resulting number is called the maximum
# rotation of the original number.

# Write a function that takes an integer as an argument and returns the maximum
# rotation of that integer. You can (and probably should) use the
# rotate_rightmost_digits function from the previous exercise.


def get_number_len(number):
    # there is probably a more efficient numerical way to do this
    # log base 10
    return len(str(number))

def max_rotation(number):
    number_len = get_number_len(number)
    for count in range(number_len, 1, -1):
        number = rotate_rightmost_digits(number, count)
    return number


print("PART 3")
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
