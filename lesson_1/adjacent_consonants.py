# *** p ***
#
# input: list of strings
# output: sorted list of strings
#
# sort by highest number of adjacent consonants. For ties, maintain input order.
#
# adjacent consonants means: next to each other in the same word OR
# separated by a space in adjacent words.
#
# Qs:
# - does the built in sorted(key=) function meet the required behavior for ties?
# - is y a consonant?
# - for adjacent words, can there be any number of spaces between the words?
#   how about other whitespace?

# *** e ***
#
# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']
#
# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']
#
# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']
#
# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']
#
# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']


# *** d ***
#
# Not really relevant

# *** a ***
#
# Define a funtion to use as a sort key. This should:
# - input: string
# - output: int
# 1. remove spaces
# 2. split on vowels - use re.split() with pattern r'[aeiou]+'
# 3. sort the list of strings by len descending
# 4. return the len of the first element in the list
#
# Then, utilize this in the main function:
# sorted(input, key=helper)
#
# Another way? Set up a dict, do the tranformations on the dict values,
# sort by the dict values.
#
# If we can't use re.split()? Can run through a string and count


# ** c **

import re

def count_adjacent_consonants(string):
    string = string.replace(' ', '')
    consonant_blocks = re.split(r'[aeiou]+', string)
    if len(consonant_blocks) == 0:
        return 0
    consonant_blocks = sorted(consonant_blocks, key=len, reverse=True)
    return len(consonant_blocks[0])


def sort_by_consonant_count(strings):
    return sorted(strings, key=count_adjacent_consonants, reverse=True)

# print(count_adjacent_consonants('dddaa'))       # 3
# print(count_adjacent_consonants('ccaa'))        # 2
# print(count_adjacent_consonants('baa'))         # 0 <-- actually, 1
# print(count_adjacent_consonants('aa'))          # 0
# print(count_adjacent_consonants('rstafgdjecc')) # 4


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
