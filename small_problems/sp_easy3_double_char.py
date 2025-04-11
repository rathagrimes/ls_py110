def repeater(string):
    # My solution
    #return ''.join([doubled for char in string for doubled in [char, char]])
    # Suggested - simpler
    return ''.join([char * 2 for char in string])

CONSONANTS = {chr(i + ord('a')) for i in range(26)} - {'a', 'e', 'i', 'o', 'u'}

def is_consonant(char):
    return char.casefold() in CONSONANTS

def double_consonants(string):
    return ''.join([char * (2 if is_consonant(char) else 1) for char in string])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
