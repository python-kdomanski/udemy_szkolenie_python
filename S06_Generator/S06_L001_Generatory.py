import datetime as dt
import sys


def MillionDays(year, month, day, maxdays):
    date = dt.date(year, month, day)

    for i in range(maxdays):
        yield (date + dt.timedelta(days=1))  #yeald zwraca wartość o zamraża funkcję


for d in MillionDays(2000, 1, 1,3):
    print(d)

print('-' * 20)

def GetMagicNumbers():
    yield(22)
    yield(4)
    yield(5)

r = GetMagicNumbers()
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

for m in r:
    print(m)