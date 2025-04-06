def integer_to_string(integer):
    if not isinstance(integer, int):
        raise TypeError("argument must be an int")
    if integer < 0:
        raise ValueError("argument should be positive")
    if integer == 0:
        return '0'

    DIGIT_VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    digits = []
    while integer > 0:
        digits.append(DIGIT_VALUES[integer % 10])
        integer //= 10

    digits.reverse()
    return ''.join(digits)

def signed_integer_to_string(integer):
    if not isinstance(integer, int):
        raise TypeError("argument must be an int")

    # My solution
    if integer == 0:
        return '0'
    positive = True
    if integer < 0:
        positive = False
        integer = abs(integer)
    return ('+' if positive else '-') + integer_to_string(integer)

    # Suggested solution
    # Doesn't work well with guard on integer_to_string...
    # if integer < 0:
    #     return '-' + integer_to_string(integer)
    # elif integer > 0:
    #     return '+' + integer_to_string(integer)
    # else:
    #     return 0

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
