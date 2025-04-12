# Implement a binary_search function that takes a list and a search item
# as arguments, and returns the index of the search item if found, or -1
# otherwise. You may assume that the list argument will always be
# sorted.

def binary_search(lst, item, offset=0):
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        return offset if lst[0] == item else -1
    middle_index = len(lst) // 2
    if lst[middle_index] == item:
        return offset + middle_index
    elif lst[middle_index] > item:
        return binary_search(lst[:middle_index], item, offset)
    else:
        return binary_search(lst[middle_index + 1:], item,
                             offset + middle_index + 1)



# def validate(result, expected):
#     print(f'{"PASS" if result == expected else "FAIL"}: result={result} expected={expected}')
# validate(binary_search([3], 3), 0)
# validate(binary_search([1,3,5], 1), 0)
# validate(binary_search([1,3,5], 3), 1)
# validate(binary_search([1,3,5], 5), 2)
# validate(binary_search([1,3,5], 0), -1)
# validate(binary_search([1,3,5], 2), -1)
# validate(binary_search([1,3,5], 4), -1)
# validate(binary_search([1,3,5], 6), -1)
# validate(binary_search([1,3,5,7], 1), 0)
# validate(binary_search([1,3,5,7], 3), 1)
# validate(binary_search([1,3,5,7], 5), 2)
# validate(binary_search([1,3,5,7], 7), 3)
# validate(binary_search([1,3,5,7], 0), -1)
# validate(binary_search([1,3,5,7], 2), -1)
# validate(binary_search([1,3,5,7], 4), -1)
# validate(binary_search([1,3,5,7], 6), -1)
# validate(binary_search([1,3,5,7], 8), -1)

# print("--")

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)
