import datetime
import functools

#logFilePath = r'd:\Projekty\PyCharm\pythonCourse\S02_Functions\function_logs.txt'

def CreateFunctionWithWrapper_LogToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args,**kwargs):
            file = open(logFilePath,"a")
            file.write("-"*20 + "\n")
            file.write('Function "{}" started at {}\n'.format(func.__name__,datetime.datetime.now().isoformat()))
            file.write('Following arguments were used:\n')
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k,v) for (k,v) in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            file.write('Function returned {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper
@CreateFunctionWithWrapper_LogToFile(r'd:\Projekty\PyCharm\pythonCourse\S02_Functions\function_log1.txt') #dekorowanie funkcji - sam wywołuje wraper przy użyciu funkcji
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name,new_salary,is_bonus))
    return new_salary

@CreateFunctionWithWrapper_LogToFile(r'd:\Projekty\PyCharm\pythonCourse\S02_Functions\function_log2.txt') #dekorowanie funkcji - sam wywołuje wraper przy użyciu funkcji
def ChangePosition(emp_name, new_position):
    print('CHANGING POSITION FOR {} TO {}'.format(emp_name,new_position))
    return new_position
print(ChangeSalary('Jonson',20000, True))

print(ChangeSalary('Jonson',20000, is_bonus=True))
print(ChangePosition('Kowalski','architect'))
