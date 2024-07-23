import datetime as dt
import sys

class MillionDaysIterator:
    def __init__(self, date, max):
        self.date = date
        self.maxsdays = max

    def __next__(self):
        if self.maxsdays <= 0:
            raise StopIteration() #gdy dojdziemy do limitu - zwracamy błąd i to zatrzymuje iterable
        ret = self.date
        self.date+=dt.timedelta(days=1)
        self.maxsdays -= 1
        return ret

    # def __iter__(self): #tak by był iterable
    #     return self #zwracamy obiek, który ma zaimplemetowany __next__ (zwraca następną wartość)

class MillionDays:
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxsdays = maxdays
        self.iterator = MillionDaysIterator(self.date, self.maxsdays)

    # def __next__(self):
    #     if self.maxsdays <= 0:
    #         raise StopIteration() #gdy dojdziemy do limitu - zwracamy błąd i to zatrzymuje iterable
    #     ret = self.date
    #     self.date+=dt.timedelta(days=1)
    #     self.maxsdays -= 1
    #     return ret

    def __iter__(self): #tak by był iterable
        return self.iterator #zwracamy obiek, który ma zaimplemetowany __next__ (zwraca następną wartość)

md = MillionDays(2000,1,1,10)
print(next(iter(md)))

for d in md: #iterable - to mozna po nim przejść funkcją for
    pass

