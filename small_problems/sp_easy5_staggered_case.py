# Write a function that takes a string as an argument and returns that
# string with a staggered capitalization scheme. Every other character,
# starting from the first, should be capitalized and should be followed
# by a lowercase or non-alphabetic character. Non-alphabetic characters
# should not be changed, but should be counted as characters for
# determining when to switch between upper and lower case.


def staggered_case(string):
    cap = True
    result = []
    for c in string:
        if c.isalpha():
            result.append(c.upper() if cap else c.lower())
            cap = not cap
        else:
            result.append(c)
    return ''.join(result)


## For part 1

# string = 'I Love Launch School!'
# result = "I LoVe lAuNcH ScHoOl!"
# print(staggered_case(string) == result)  # True

# string = 'ALL_CAPS'
# result = "AlL_CaPs"
# print(staggered_case(string) == result)  # True

# string = 'ignore 77 the 4444 numbers'
# result = "IgNoRe 77 ThE 4444 nUmBeRs"
# print(staggered_case(string) == result)  # True

# print(staggered_case('') == "")          # True


## For part 2

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
