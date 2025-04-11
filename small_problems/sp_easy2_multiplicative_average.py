import functools

def multiplicative_average(lst):
    product = functools.reduce(lambda x, y: x * y, lst)
    avg = product / len(lst)
    return f"{avg:.3f}"
    
print(multiplicative_average([3, 5]))
print(multiplicative_average([2, 5, 8]))
print(multiplicative_average([2, 5]))
print(multiplicative_average([1, 1, 1, 1]))
print(multiplicative_average([2, 5, 7, 11, 13, 17]))

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
