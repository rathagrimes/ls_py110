def halvsies(lst):
    second_half_index = len(lst) // 2
    if (len(lst) % 2 == 1):
        second_half_index += 1
    return [lst[:second_half_index], lst[second_half_index:]]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
