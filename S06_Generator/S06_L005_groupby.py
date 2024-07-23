import itertools as it

filepath = r'd:\Projekty\PyCharm\pythonCourse\S06_Generator\data.txt'

data = []

with open(filepath) as file:
    for line in file:
        elements = line.rstrip("\n").split(':')
        d = {'type' : elements[0], 'action' : elements[1]}
        data.append(d)

print(data)

data = sorted(data, key = lambda x: x['type'])

for key, elements in it.groupby(data, key = lambda x: x['type']):
    #print('The key is {} and the group is {}'.format(key, list(elements)))
    print('The key is {} and the number of elements {}'.format(key, len(list(elements))))