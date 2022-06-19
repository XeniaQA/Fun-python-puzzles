school = {'1A' : 30, '1B' : 25, '2B' : 40, '3A' : 32, '4D' : 21}
print(school['1A'])

school['1A'] = 32
school['1B'] = 30
school['4D'] = 40

school['5A'] = 13
school['5B'] = 15

del school['2B']

print(school)