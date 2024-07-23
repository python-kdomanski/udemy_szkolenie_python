# file = open(r'd:\Projekty\PyCharm\pythonCourse\S06_Generator\data.txt')
#
# data = file.read()
#
# file.close()
#
# for line in data.splitlines():
#     if line.startswith('ACTION'):
#         print(line)

# file = open(r'd:\Projekty\PyCharm\pythonCourse\S06_Generator\data.txt')
#
# for line in file:
#     if line.startswith('ACTION'):
#         print(line.replace("\n",''))
# file.close()

# file = open(r'd:\Projekty\PyCharm\pythonCourse\S06_Generator\data.txt')
#
# records=[]
#
# for line in file:
#     if ':' in line:
#         type, action = line.rstrip("\n").split(':',1)
#         record = (type, action)
#         records.append(record)
# print(records)
#
# file.close()

def get_records(filePath):
    print('----opening file-----')

    file = open(filePath)
    for line in file:
        if ':' in line:
            type, action = line.rstrip("\n").split(':',1)
            record = (type, action)
            yield record

    print('----closing file-----')

    file.close()

for record in get_records(r'd:\Projekty\PyCharm\pythonCourse\S06_Generator\data.txt'):
    print("{} - {}".format(record[0], record[1]))