# Write a function that takes a string argument and returns a list of
# substrings of that string. Each substring should begin with the first
# letter of the word, and the list should be ordered from shortest to
# longest.

# input: string
# output: list of strings
# approach: use slicing with a changing slice value. can do it with a
#           list comprehension.


def leading_substrings(string):
    return [string[:x] for x in range(1, len(string)+1)]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
