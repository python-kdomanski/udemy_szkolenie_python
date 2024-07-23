import datetime as dt
import sys

start = dt.datetime.now()
print("Start at: {}".format(start))

'''
dates = [dt.date(2000,1,1)+ dt.timedelta(days=1) for i in range(2500000)]
print("size of dates is {}".format(sys.getsizeof(dates)))

for d in dates
    pass
'''
class MillionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxsdays = maxdays

    def __next__(self):
        if self.maxsdays <= 0:
            raise StopIteration() #gdy dojdziemy do limitu - zwracamy błąd i to zatrzymuje iterable
        ret = self.date
        self.date+=dt.timedelta(days=1)
        self.maxsdays -= 1
        return ret

    def __iter__(self): #tak by był iterable
        return self #zwracamy obiek, który ma zaimplemetowany __next__ (zwraca następną wartość)

md = MillionDays(2000,1,1,2500000)
print("size of MillionDays is {}".format(sys.getsizeof(md)))

for d in md: #iterable - to mozna po nim przejść funkcją for
    pass
#print(next(md)) #funkcja next jest wywołana na rzecz iteratora - md jest ineratorem bo w klasie zaimplementowaliśmy funkcję __next___
#print(next(md))
#print(next(md))

# for i in range(2500000):
#     next(md)

stop = dt.datetime.now()
print("Stop at: {}".format(stop))
print("Total time: {}".format(stop - start))