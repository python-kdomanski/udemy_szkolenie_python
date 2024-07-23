var_x = 10
password = 'My secret password'

source = 'var_x + 2'

result = eval(source)
print(result)

source = 'password'
result = eval(source)
print(result)

#print(globals())

globals = globals().copy()
result = eval(source, globals)
print(result)

del globals['password']
source = 'var_x + 2'
result = eval(source, globals)
print(result)

globals = {}
#source = '__import__("os").getcwd()'
result = eval(source, globals)
print(result)