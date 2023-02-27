from dataclasses import dataclass

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


class Complex:
    """A simple example class"""
    field1 = 12345

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    @staticmethod
    def method1():
        return 'hello world'


x = Complex(3.0, -4.5)
print(x.r, x.i, x.field1, x.method1(), Complex.method1(), sep=", ", end="\n")
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print("Complex.counter = ", x.counter)
del x.counter

class Dog:
    # tricks = []   behavior like static filed

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d, e = Dog('Fido'), Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks, e.tricks)


class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


john = Employee('john', 'computer lab', 1000)
print(john.dept, john.salary)


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

"""
sum(i*i for i in range(10))                 # sum of squares
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product
unique_words = set(word for line in page  for word in line.split())
valedictorian = max((student.gpa, student.name) for student in graduates)
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
"""

