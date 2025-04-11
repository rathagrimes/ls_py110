def swap_name(name):

    # My initial solution
    # first, last = name.split()
    # return f"{last}, {first}"

    # Suggested - one liner
    # Learning: you can use slicing on a function return value
    # return ', '.join(name.split()[::-1])

    # Enhanced version
    # Uses asterisk unpacking!
    # *most, last = name.split()
    # return ', '.join([last, ' '.join(most)])

    # Enhanced version - nice peer solution
    # rsplit was made for this
    return ", ".join(name.rsplit(" ", 1)[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

print(swap_name('Karl Oskar Henriksson Ragvals')
      == "Ragvals, Karl Oskar Henriksson")  # True
