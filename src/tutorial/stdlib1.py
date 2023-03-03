import glob
import sys
import argparse
import re
import random
from urllib.request import urlopen
from datetime import date
import zlib
from timeit import Timer

print(glob.glob('*.py'))
print(sys.argv)

parser = argparse.ArgumentParser(prog='top', description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

# regexp
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'), 'tea for too'.replace('too', 'two'))

it = re.compile('[a-z]+')
print("Search: ", it.search("some 4 string")[0])

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))   # sampling without replacement
print(random.random())    # random float
print(random.randrange(6))    # random integer chosen from range(6)

now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964, 7, 31)
print("To birthday: ", (now - birthday).days)

s = b'witch which has which witches wrist watch'
print(len(s), end=" ")
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline
            break

print()






