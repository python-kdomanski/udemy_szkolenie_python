#Wykorzystanie Context manager - on pilnuje/zwalnia plik
# with open(r'D:\Projekty\PyCharm\pythonCourse\S08_Contex_Manager\file.txt','w+') as file:
#     file.writelines('SUCCESS')

import time

class time_mesaure:
    def __init__(self):
        pass

    def __enter__(self): #wywoluje sie kiedy obiekt jest tworzony, musi być zaimpl. jak mamy zrobić context manager (wywołanie poprzez with)
        print('entering...')
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): #wywoływane na końcy (gdy obiekt jest zamykany)
        print('exiting...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print('Execution time: {}'.format(self.__difference))

with time_mesaure() as my_timer:
    time.sleep(3)

with time_mesaure(): #nie odwiłujemy sie do obiektu - nie trzeba nawet zatem dodawać as
    time.sleep(3)
