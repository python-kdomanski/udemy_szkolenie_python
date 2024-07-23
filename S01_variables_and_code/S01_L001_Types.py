myVar="Test"
myVar2=myVar
print(myVar, myVar2)
print(type(myVar), type(myVar2))
print("Is the same value?",myVar==myVar2)
print('Is the same?', myVar is myVar2)
print(id(myVar), id(myVar2))

myVar2=myVar+"AA"
print(myVar, myVar2)
print(type(myVar), type(myVar2))
print("Is the same value?",myVar==myVar2)
print('Is the same?', myVar is myVar2)
print(id(myVar), id(myVar2))

myVar2=myVar2[:-2]
print(myVar, myVar2)
print(type(myVar), type(myVar2))
print("Is the same value?",myVar==myVar2)
print('Is the same?', myVar is myVar2)
print(id(myVar), id(myVar2))