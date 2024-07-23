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

    def __getitem__(self, item):
        if item <= self.maxsdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration() #wyjątek jest ukrywany - kończy się po prostu for



md = MillionDays(2000,1,1,2500000)
print("size of MillionDays is {}".format(sys.getsizeof(md)))

print(md[0], md[1], md[10])

it = iter(md) #stworzenie iteratora dla md (zamiast __next__)

print(next(it))
print(next(it))
print(next(it)) #samo polecenie next nie ukrywa StopIteratiom - "ukrywa" to pętla for

for d in md:
    pass

stop = dt.datetime.now()
print("Stop at: {}".format(stop))
print("Total time: {}".format(stop - start))