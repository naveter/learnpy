import re

# regexp
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'), 'tea for too'.replace('too', 'two'))

it = re.compile('[a-z]+')
print("Search: ", it.search("some 4 string")[0])

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1), mo.group(2), mo.group(0), mo.group(), mo.groups());
areaCode, mainNumber = mo.groups()
print(areaCode, mainNumber)

# Non greedy
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print("Non greedy: ", mo2.group())

phoneNumRegex = re.compile(r'(\d\d\d)-'     # First
                           r'(\d\d\d)-'     # Second
                           r'(\d\d\d\d)'    # Third
                           , re.VERBOSE)
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

agentNamesRegex = re.compile(r'Agent (\w)\w*', re.IGNORECASE)
print(
    agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
)

print(re.search('foo$', 'foo\nbar', flags=re.MULTILINE).group())
print(re.search('foo.', 'foo\nbar', flags=re.DOTALL).group())














