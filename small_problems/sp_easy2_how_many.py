def count_occurrences(items):
    data = {k: items.count(k) for k in set(items)}
    for k, v in data.items():
        print(f'{k} => {v}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Expected output
# your output sequence may appear in a different sequence
#
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2
