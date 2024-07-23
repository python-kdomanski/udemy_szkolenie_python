import os

class ini_file:

    def __init__(self, path):
        print('__init__')
        self.path = path
        self.parameters = {}
        self.read_from_disk()

    def read_from_disk(self):
        if os.path.isfile(self.path):
            with open(self.path) as file:
                for line in file:
                    parts = line.replace("\n",'').split('=')
                    self.parameters[parts[0]] = parts[1]

    def read_parameter(self, key):
        if key in self.parameters.keys():
            return self.parameters[key]
        else:
            return None

    def write_parameter(self, key, value):
        self.parameters[key] = value

    def save_on_disk(self):
        with open(self.path, "w") as file:
            for key, value in self.parameters.items():
                line = "{}={}\n".format(key, value)
                file.writelines(line)

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): #jak zwrócimy true to ukrywamy błąd
        print('__exit__')
        print('exc_type={}'.format(exc_type))
        print('exc_val={}'.format(exc_val))
        print('exc_tb={}'.format(exc_tb))

        if exc_type == OSError:
            return False #nie ukrywamy - standardowa obsługa 
        else:
            return True #ukryway bład


with ini_file(r'D:\Projekty\PyCharm\pythonCourse\S08_Contex_Manager\my2.ini') as myini:
    myini.write_parameter('mode','strict')
    myini.write_parameter('loglevel','light')
    myini.save_on_disk()
    print(10/0)


