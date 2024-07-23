f = lambda x: len(x)

print(f('a 19-letters string'))

text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

print(list(map(f, text_list)))

print(list(map(lambda s: len(s), text_list)))

'''
Wykorzystasz przy tym funkcję map, która pozwala uruchomić wskazywaną przez pierwszy argument funkcję dla listy przekazanej jako drugi argument.
Uwaga: funkcja map nie zwraca listy, ale zwracany obiekt można łatwo skonwertować do listy.
'''