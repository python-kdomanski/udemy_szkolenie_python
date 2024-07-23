import datetime
import functools

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args,**kwargs):
        print('Function "{}" started at {}'.format(func.__name__,datetime.datetime.now().isoformat()))
        print('Following arguments were used:')
        print(args,kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper #dekorowanie funkcji - sam wywołuje wraper przy użyciu funkcji
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name,new_salary,is_bonus))
    return new_salary

print(ChangeSalary('Jonson',20000, True))

print(ChangeSalary('Jonson',20000, is_bonus=True))