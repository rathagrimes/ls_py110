
def interleave(lst1, lst2):
    # Orig solution
    # result = []
    # common_length = min(len(lst1), len(lst2))
    # for i in range(common_length):
    #     result.append(lst1[i])
    #     result.append(lst2[i])
    # result.extend(lst1[common_length:])
    # result.extend(lst2[common_length:])
    # return result

    # Zip based solution
    return [elt
        for item in zip(lst1,lst2)
        for elt in item]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
