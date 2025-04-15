# Write a function that takes a string and returns a dictionary
# containing the following three properties:
#
# * the percentage of characters in the string that are lowercase letters
# * the percentage of characters that are uppercase letters
# * the percentage of characters that are neither
#
# All three percentages should be returned as strings whose numeric
# values lie between "0.00" and "100.00", respectively. Each value
# should be rounded to two decimal points.

# You may assume that the string will always contain at least one
# character.

#f'{num:.2f}'

# approach:
# - iterate through the characters in the string and increment three counters
# - return the dict as a literal, with calculations and string formatting

def letter_percentages(string):
    lc = 0
    uc = 0
    neither = 0
    for c in string:
        if not c.isalpha():
            neither += 1
        elif c == c.upper():
            uc += 1
        elif c == c.lower():
            lc += 1
    return {'lowercase': f'{(100 * lc/len(string)):.2f}',
            'uppercase': f'{(100 * uc/len(string)):.2f}',
            'neither': f'{(100 * neither/len(string)):.2f}'}
                

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
