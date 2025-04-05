# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }

# # for m in munsters:
# #     print(f'{m} is a {munsters[m]["age"]}-year-old {munsters[m]["gender"]}')

# total_age = 0
# for m in munsters:
#     if munsters[m]['gender'] == 'male':
#         total_age += munsters[m]['age']
# print(total_age)

# print(sum([v['age'] for k, v in munsters.items() if v['gender'] == 'male']))

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# #print([sorted(v) for v in lst])
# print([sorted(v, key=str) for v in lst])

# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# d = {}
# for elt in lst:
#     d[elt[0]] = elt[1]
# print(d)

# print({elt[0]: elt[1] for elt in lst})

# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# def sum_odd(lst):
#     return sum([v for v in lst if v % 2 == 1])
# #print(sorted(lst, key=sum_odd))
# print(sorted(lst, key=lambda lst: sum([v for v in lst if v % 2 == 1])))


# -------------------------------------------------------------------
# NESTED COMPREHENSION!!
#
# Given the following data structure, return a new list identical in
# structure to the original but, with each number incremented by 1. Do
# not modify the original data structure. Use (a) comprehension(s).

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

print([{key: value + 1 for key, value in dictionary.items()}
                       for dictionary in lst])
# -------------------------------------------------------------------

# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# print([[v for v in sublist if v % 3 == 0] for sublist in lst])



# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# def extract(v):
#     if v['type'] == 'fruit':
#         #return list(map(str.capitalize, v['colors']))
#         return [c.capitalize() for c in v['colors']]
#     if v['type'] == 'vegetable':
#         return v['size'].upper()

# print([extract(v) for v in dict1.values()])

# print([[c.capitalize() for c in v['colors']] if v['type'] == 'fruit'
#        else v['size'].upper()
#        for v in dict1.values()])

# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]

# def all_even(d):
#     for value_list in d.values():
#         #if len([v for v in value_list if v % 2 == 1]) > 0:
#         if not all([v % 2 == 0 for v in value_list]):
#             return False
#     return True
# print([d for d in lst if all_even(d)])



import random

# v1 = random.randint(0, 0xffffffff)
# print(int('0x'+('f'*length), base=16))

def generate_uuid():
    def make_random_hex(length):
        max = int('0x'+('f'*length), base=16)
        return f'{random.randint(0, max):0{length}x}'
    sections = [8, 4, 4, 4, 12]
    uuid = []
    for s in sections:
        uuid.append(make_random_hex(s))
    return '-'.join(uuid)

print(generate_uuid())
print(generate_uuid())
print(generate_uuid())

# print(f'{make_random_hex(8)}-'+
#       f'{make_random_hex(4)}-'+
#       f'{make_random_hex(4)}-'+
#       f'{make_random_hex(4)}-'+
#       f'{make_random_hex(12)}')



dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# words = [word for lst in dict1.values() for word in lst]
# vowels = [char for word in words for char in word if char in 'aeiou']

vowels = [char
          for lst in dict1.values()
          for word in lst
          for char in word if char in 'aeiou']
print(vowels)
