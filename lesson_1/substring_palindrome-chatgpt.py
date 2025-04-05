def detect_palindrome_helper(string, left_bound, right_bound):
    # Fix: Correct the condition to avoid out-of-bound access
    while left_bound >= 0 and right_bound < len(string) and string[left_bound] == string[right_bound]:
        left_bound -= 1
        right_bound += 1
    # Return the palindrome found
    return string[left_bound + 1:right_bound]

def detect_palindromes_at_index(string, index):
    result = []

    # Check for odd-length palindromes
    odd_palindrome = detect_palindrome_helper(string, index, index)
    if odd_palindrome:
        result.append(odd_palindrome)

    # Check for even-length palindromes (ensure no index error)
    if index + 1 < len(string) and string[index] == string[index + 1]:
        even_palindrome = detect_palindrome_helper(string, index, index+1)
        if even_palindrome:
            result.append(even_palindrome)

    return result

def generate_subpalindromes(string):
    result = []
    # Reduce size while checking if the string is a palindrome at each step
    while len(string) > 3:
        if string == string[::-1]:  # Ensure it's a palindrome
            result.append(string)
        string = string[1:-1]
    return result

def substring_palindromes(string):
    maximal_palindromes = []

    # Special case: input is a 2 or 3 letter palindrome
    if len(string) <= 3 and string == string[::-1]:
        maximal_palindromes.append(string)
        # Special case for 3 of the same letter, assure a 2-letter substr
        if len(string) == 3 and string[0] == string[1]:
            maximal_palindromes.append(string[:2])
    else:
        for i in range(len(string)):
            maximal_palindromes.extend(detect_palindromes_at_index(string, i))

    # Use a set to weed out duplicate substrings
    result = set(maximal_palindromes)
    for p in maximal_palindromes:
        result.update(generate_subpalindromes(p))
    return list(result)

print(substring_palindromes("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(substring_palindromes("palindrome")) # []
print(substring_palindromes("")) # []
print(substring_palindromes("repaper"))    # ['repaper', 'epape', 'pap']
print(substring_palindromes("repapEr"))    # ['pap']
print(substring_palindromes("supercalifragilisticexpialidocious")) # ["ili"]

print(substring_palindromes("zzzzz")) #
print(sorted(substring_palindromes("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"), key=len))

