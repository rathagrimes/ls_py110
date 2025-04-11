def reverse_number(num):
    if not isinstance(num, int) or num < 1:
        raise ValueError("Give me a positive int please")
    # My initial solution
    # chars = list(str(num))
    # chars.reverse()
    # return int(''.join(chars))

    # Suggested - more elegant
    return int(str(num)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
