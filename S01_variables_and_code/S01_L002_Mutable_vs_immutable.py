number=10
print('Value number: ', number, id(number))

number+=2
print('Value number: ', number, id(number))

text = 'Africa'
print('Value text: ', text, id(text))
text=text + ' is hot'
print('Value text: ', text, id(text))

list = [1,2,3]
print('Value list: ', list, id(list))
list.append(4)
print('Value list: ', list, id(list))

list2=list
print('Value list2: ', list2, id(list2))
list2.append(5)
print('Value list: ', list, id(list))
print('Value list2: ', list2, id(list2))

list3 = list.copy()
print('Value list: ', list, id(list))
print('Value list3: ', list3, id(list3))
list3.append(6)
print('Value list: ', list, id(list))
print('Value list3: ', list3, id(list3))
