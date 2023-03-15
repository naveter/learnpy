import glob
import sys
import argparse
import random
import zlib
from timeit import Timer

print(glob.glob('*.py'))
print(sys.argv)

parser = argparse.ArgumentParser(prog='top', description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))   # sampling without replacement
print(random.random())    # random float
print(random.randrange(6))    # random integer chosen from range(6)

s = b'witch which has which witches wrist watch'
print(len(s), end=" ")
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print()






