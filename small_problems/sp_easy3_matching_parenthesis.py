# Write a function that takes a string as an argument and returns True
# if all parentheses in the string are properly balanced, False
# otherwise. To be properly balanced, parentheses must occur in matching
# '(' and ')' pairs.
# Note that balanced pairs must start with a (, not a ).

# approach: keep a counter, count up for (, count down for )
# trick is that we must not go negative, automatic fail if we do


def is_balanced(string):
    counter = 0
    for char in string:
        match char:
            case '(':
                counter += 1
            case ')':
                if counter == 0:
                    return False
                counter -= 1
    return counter == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
