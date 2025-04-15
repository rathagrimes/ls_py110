# Given a dictionary, return its keys sorted by the values associated
# with each key.

def order_by_value(dictionary):
    return sorted(dictionary.keys(), key=dictionary.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
