import os
path = r'/mydata.txt'

#os.remove(path)
'''
if os.path.isfile(path):
    print('File %s is exists' % path)
else:
    print('Creating file %s' % path)
    open(path,'x').close()
    print('File %s created' % path)
'''
#result=os.path.isfile(path)
result=os.path.isfile(path) or open(path,'x').close()
#result=os.path.isfile(path) and open(path,'x').close()
print(result)