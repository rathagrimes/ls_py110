# Write a function that takes a list argument and returns a new list
# that contains the values from the input list in sorted order. The
# function should sort the list using the merge sort algorithm as
# described above. You may assume that every element of the list will
# have the same data type: either all numbers or all strings.

# [9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
# [[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
# [[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
# # repeat until each sub-list contains only 1 value
# [[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]

# [[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] -->
# [[[2, 9], [6, 7]], [[5, 8], [0, 1]]] -->
# [[2, 6, 7, 9], [0, 1, 5, 8]] -->
# [0, 1, 2, 5, 6, 7, 8, 9]



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

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle_index = len(lst) // 2
    partition1, partition2 = lst[:middle_index], lst[middle_index:]
    return merge(merge_sort(partition1), merge_sort(partition2))


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)
