aTuple = (1,2,3,4,5) #jest iterable ale nie ma własnego iteratora

for x in aTuple:
    print(x)

#print(next(aTuple))
it = iter(aTuple)
print(next(it))
print(next(it))
print(next(it))

aList = [1,2,3,4,5]
for x in aList:
    print(x)

#print(next(aList))
it = iter(aList)
print(next(it))
print(next(it))
print(next(it))

aSet = {1,2,(3,4),'another element',3,4}
for x in aSet:
    print(x)

#print(next(aSet))

it = iter(aSet)
print(next(it))
print(next(it))
print(next(it))

# with open('d:\Projekty\PyCharm\pythonCourse\S05_Iterators\lines.txt', "r") as file:
#     for line in file:
#         print(line)

with open('d:\Projekty\PyCharm\pythonCourse\S05_Iterators\lines.txt', "r") as file:
    while True:
        try:
            print(next(file))
        except StopIteration:
            break