# Given a sequence of integers, filter out instances where the same
# value occurs successively, retaining only the initial occurrence.
# Return the refined sequence.

# def unique_sequence(original):
#     result = []
#     last = 'nope'
#     for elt in original:
#         if elt != last:
#             result.append(elt)
#             last = elt
#     return result

# noice
def unique_sequence(numbers):
    return [value
            for idx, value in enumerate(numbers)
            if idx == 0 or value != numbers[idx-1]]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
