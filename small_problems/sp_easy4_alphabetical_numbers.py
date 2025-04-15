# Write a function that takes a list of integers between 0 and 19 and
# returns a list of those integers sorted based on the English word for
# each number:

# zero, one, two, three, four, five, six, seven, eight, nine, ten,
# eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
# eighteen, nineteen

# PEDAC:
# Input: List of numbers
# Output: new list, consisting of the input list of numbers in a sorted order
# Rules
# - the output list must be sorted alphabetically by the name of each number.
# Algorithm
# - Use sorted() with a key function
# - Place the number words into a dict with the corresponding number as a key.
# - The key function can be dict.get


number_words_list = ['zero', 'one', 'two', 'three', 'four', 'five',
                     'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                     'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
                     'seventeen', 'eighteen', 'nineteen']

number_words_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
                     4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                     8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
                     12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                     15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                     18: 'eighteen', 19: 'nineteen'}

# easier way to create number_words_dict
number_words_dict2 = {idx: word for idx, word in enumerate(number_words_list)}



def alphabetic_number_sort(lst):
    return sorted(lst, key=number_words_dict.get)


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
