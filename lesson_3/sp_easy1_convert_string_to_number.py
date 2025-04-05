# Write a function that takes a string of digits and returns the appropriate
# number as an integer. You may not use any of the standard conversion functions
# available in Python, such as int. Your function should calculate the result by
# using the characters in the string.
#
# For now, do not worry about leading + or - signs, nor should you worry about
# invalid characters; assume all characters are numeric.

def string_to_integer(string):
    if not string:
        return 0
    if not isinstance(string, str):
        raise TypeError("argument must be string")
    if not all('0' <= c <= '9' for c in string):
        raise ValueError("argument did not contain all-numeric characters")
    # could probably do something cleverer with ord()
    digit_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    result = 0

    # My original approach
    # multiplier = 10 ** (len(string)-1)
    # for c in string:
    #     value = digit_values.index(c)
    #     result += value * multiplier
    #     multiplier //= 10

    # Suggested solution
    for c in string:
        result = (10 * result) + digit_values.index(c)

    return result
        
def hexadecimal_to_integer(string):
    if not string:
        return 0
    if not isinstance(string, str):
        raise TypeError("argument must be string")
    if not all(('0' <= c <= '9') or ('A' <= c.upper() <= 'F') for c in string):
        raise ValueError("argument did not contain all-numeric characters")

    digit_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', \
                    'A', 'B', 'C', 'D', 'E', 'F']
    result = 0
    for c in string:
        result = (16 * result) + digit_values.index(c.upper())

    return result


def string_to_signed_integer(string):
    if not string:
        return 0
    if not isinstance(string, str):
        raise TypeError("argument must be string")

    positive = True
    if string[0] in ('-', '+'):
        positive = string[0] == '+'
        string = string[1:]

    return string_to_integer(string) * (1 if positive else -1)

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

print(hexadecimal_to_integer('4D9f') == 19871)  # True

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
