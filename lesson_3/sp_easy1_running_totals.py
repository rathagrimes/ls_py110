def running_total(lst):
    if not isinstance(lst, list):
        raise TypeError("Argument must be a list")
    if not all([isinstance(elt, (int, float)) for elt in lst]):
        raise TypeError("Argument must be a list of numbers")

    result = []
    accum = 0
    for elt in lst:
        accum += elt
        result.append(accum)
    return result



print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
