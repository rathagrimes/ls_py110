# Problem: Find all substrings of an input string that are at least 2
# characters and which are palindromes.
#
# Requirements:
# - Palindrome detection is case sensitive
# - Substrings must be at least 2 characters long
#
# Approach:

# Observation that every longer palindrome contains smaller palindromes
# Observation that a palindrome pivots around one character (odd length) or two characters (doubled)
# Theory: walk through the letters of the string, checking if each one is at the center of a palindrome
# 'xabac' => aba
# 'foofoo' => foof, oofoo => oo, ofo
# 'neeee' => 'eee', 'eeee' => 'ee'


def detect_palindrome_helper(string, left_bound, right_bound):
    while left_bound > 0 and right_bound < len(string) - 1 and string[left_bound - 1] == string[right_bound + 1]:
    #                                                    ^ tricky bit!
        left_bound -= 1
        right_bound += 1
    if left_bound != right_bound:
        return string[left_bound:right_bound+1]
    return None

def detect_palindromes_at_index(string, index):
    result = []

    odd_palindrome = detect_palindrome_helper(string, index, index)
    if odd_palindrome:
        result.append(odd_palindrome)

    if string[index] == string[index+1]:
        even_palindrome = detect_palindrome_helper(string, index, index+1)
        if even_palindrome:
            result.append(even_palindrome)

    return result


# input must be a palindrome
def generate_subpalindromes(string):
    result = []
    while len(string) > 3:
        string = string[1:-1]
        result.append(string)
    return result

def substring_palindromes(string):
    maximal_palindromes = []

    # Special case: input is a 2 or 3 letter palindrome
    if len(string) <= 3 and string == string[::-1]:
        maximal_palindromes.append(string)
        # special special case: 3 of the same letter, there is a 2-letter substr
        if len(string) == 3 and string[0] == string[1]:
            maximal_palindromes.append(string[:2])
    else:
        for i in range(1, len(string)-2):
            maximal_palindromes.extend(detect_palindromes_at_index(string, i))

    # Use a set to weed out duplicate substrings
    result = set(maximal_palindromes)
    for p in maximal_palindromes:
        result.update(generate_subpalindromes(p))
    return list(result)


#print(substring_palindromes('afoxxofiealycabacx'))
# print(generate_subpalindromes('qxabaxq'))
# print(generate_subpalindromes('qxabbaxq'))
# print(detect_palindromes('xabac', 2))
# print(detect_palindromes('xabac', 3))

print(substring_palindromes("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(substring_palindromes("palindrome")) # []
print(substring_palindromes("")) # []
print(substring_palindromes("repaper"))    # ['repaper', 'epape', 'pap']
print(substring_palindromes("repapEr"))    # ['pap']
print(substring_palindromes("supercalifragilisticexpialidocious")) # ["ili"]

print(substring_palindromes("zzzzz")) #
print(sorted(substring_palindromes("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"), key=len))


