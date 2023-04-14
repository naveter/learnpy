import math

squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]
print(squares)


combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# The following list comprehension will transpose rows and columns:

print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(list(zip(*matrix)))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('orange' in basket)                 # fast membership testing

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both
print( {x for x in 'abracadabra' if x not in 'abc'} )

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x**2 for x in (2, 4, 6)})
print(dict(sape=4139, guido=4127, jack=4098))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

# Array keys like array
# Keys are (x, y) tuples of ints, values the character at that position on the canvas:
# canvas = {}
# canvas[(canvasX, canvasY)] = dieFace[dy][dx]
# canvas.get((cx, cy), ' ')




