produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit_v1(produce):
    result = {}
    for k, v in produce.items():
        if v == 'Fruit':
            result[k] = v
    return result

def select_fruit(produce, criterion):
    return {k: v for k, v in produce.items() if v == criterion}


print(select_fruit(produce, 'Vegetable'))  # { apple: 'Fruit', pear: 'Fruit' }

# -----------------------------------------------------
def mult_list(lst, factor):
    return list(map(lambda x: x*factor, lst))

print(mult_list([1, 2, 3], 5))

# -----------------------------------------------------

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(sum(ages.values()))
print(min(ages.values()))


# -----------------------------------------------------

def freq(string):
    result = {}
    for c in string:
        if c.isalnum():
            result[c] = result.get(c, 0) + 1
    return result

print(freq('The Flintstones Rock'))
