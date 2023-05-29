from decimal import *
from heapq import heapify, heappop, heappush
import locale
from string import Template
import time, os.path
import logging
from collections import deque
import bisect
import random

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))

t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))


class BatchRename(Template):
    delimiter = '%'


photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
t = BatchRename("%d-%n-%f")
date = time.strftime('%d%b%y')
# enumerate - auto count for cycles
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
print([heappop(data) for i in range(3)])  # fetch the three smallest entries

print(round(Decimal('0.70') * Decimal('1.05'), 2), round(.70 * 1.05, 2))
print(Decimal('1.00') % Decimal('.10'), sum([Decimal('0.1')]*10) == Decimal('1.0'), sum([0.1]*10) == 1.0)

getcontext().prec = 36
print(Decimal(1) / Decimal(7))

# array of hashtables
ants = []
for i in range(3):
    ant = {
    'x': random.randint(0, 3 + 1),
    'y': random.randint(0, 2 + i),
    'orig': i,
    }
    ants.append(ant)

print(ants)



