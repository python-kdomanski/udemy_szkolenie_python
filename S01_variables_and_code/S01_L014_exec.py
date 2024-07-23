var_x = 10
source = 'var_x + 4'

result = eval(source)
print(result)

#eval umożliwia  tylko wykonać wyrażenie - coś będzie później przypisane do zmiennej
#eval - 1 linijka tekstu
'''
source = 'var_x = 4'

result = eval(source)
print(result)
'''

source = 'var_x = 4'
result = exec(source)
print(result)
#exec - wykonuje kod, zwraca zawsze None
print(var_x)

var_x = 10

source = '''
new_var=1
for i in range(var_x):
    print('-'*i)
    new_var+=i
'''
result = exec(source)
print(var_x)
print(new_var)

source = input ('Wprowadz wyrażenie:')
print(eval(source))