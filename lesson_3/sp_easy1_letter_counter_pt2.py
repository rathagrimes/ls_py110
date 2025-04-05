def word_sizes(string):
    words = string.split()
    words_by_size = {}
    for word in words:
        word = ''.join([c for c in word if c.isalpha()])
        words_by_size[len(word)] = words_by_size.get(len(word), 0) + 1
    return words_by_size

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
