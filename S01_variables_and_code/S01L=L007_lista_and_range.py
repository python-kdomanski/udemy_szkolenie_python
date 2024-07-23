'''
for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)

list = range(10)
print('List:', list, type(list))
'''
list = list(range(10))
print('List:', list, type(list), id(list))

print(list[5:7])
print(list[5:])
print(list[:-1])
print(list[:8:2]) #od zerowego do 8 co 2
print(list[-1:0:-1]) #od końca )-1) do poczaytku (0) cofając się o -1
print(list[-1::-1])

list2=list[:] #kopia listy czyli to samo co list2=list.copy()