# Write a function that takes two sorted lists as arguments and returns
# a new list that contains all the elements from both input lists in
# ascending sorted order. You may assume that the lists contain either
# all integer values or all string values.

# You may not provide any solution that requires you to sort the result
# list. You must build the result list one element at a time in the
# proper order.

# Your solution should not mutate the input lists.

# input: 2 lists
# output: 1 new list
# algorithm:
# Initialize a pointer for each list to 0
# Loop:
#   Compare the current element for each list
#   Take the one that is lower in sorted order and increment its pointer
#   If the pointer is past the end of one list, exit the loop
#   Append the remainder of both lists (one will have nothing remaining)


def merge(list1, list2):
    result = []
    index1 = index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] <= list2[index2]:
            result.append(list1[index1])
            index1 += 1
        else:
            result.append(list2[index2])
            index2 += 1
    result += list1[index1:] + list2[index2:]
    return result


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

