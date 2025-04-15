# Write a function that takes a list as an argument and sorts that list
# using the bubble sort algorithm described above. The sorting should be
# done "in-place" -- that is, the function should mutate the list. You
# may assume that the list contains at least two elements


def bubble_sort(lst):
    def try_swap(lst, idx):
        if lst[idx] > lst[idx + 1]:
            lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
            return True
        return False

    if len(lst) < 2:
        return lst

    while True:
        swapped = False
        for idx in range(len(lst) - 1):
            swapped |= try_swap(lst, idx)
        if not swapped:
            break



lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True
