# Write a function that takes a list as an argument and reverses its
# elements, in place. That is, mutate the list passed into the function.
# The returned object should be the same object used as the argument.
# You may not use the list.reverse method nor may you use a slice ([::-1]).

# Approach:
# Pop last element, and insert it at an increasing index each time.
# ["a", "b", "c", "d", "e"]
#    pop "e"
#    insert at 0
#    pop "d"
#    insert at 1
# etc.

def reverse_list(lst):
    # for index in range(len(lst)):
    #     lst.insert(index, lst.pop())
    # return lst

    # The suggested solution uses indexes -
    # we can do it that way too
    # (exercises the swap capability!)
    for front in range(len(lst) // 2):
        back = -(front + 1)
        lst[front], lst[back] = lst[back], lst[front]
    return lst
    

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
