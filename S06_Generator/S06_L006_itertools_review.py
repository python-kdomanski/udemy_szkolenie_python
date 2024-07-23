import itertools
import operator

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul) #2 arg - funkcja jaka ma byc wykonana na obiektach z 1 arg (mul-mnożenie)
for each in result:
    print(each)

# data = [1, 2, 13, 4, 5]
# result = itertools.accumulate(data, max)
# for each in result:
#     print(each)

print('-'*100)

#itertools.count(start=0,step=1)
for i in itertools.count(10,3):
    print(i)
    if i > 20:
        break

print('-'*100)

#itertools.cycle(iterable) - przechodzi w nieskończonosć
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# for m in itertools.cycle(months):
#     print(m)

print('-'*100)

color_basic = ['red', 'yellow', 'blue']
color_mix = ['green', 'orange', 'violet']
result = itertools.chain(color_basic, color_mix) #łaczy 2 lub więcej obiekty iterable
for each in result:
    print(each)

print('-'*100)

#itertools.compress(data, selectors)
cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
selections = [True, False, True, False]
result = itertools.compress(cars, selections)
for each in result:
    print(each)

print('-'*100)
#itertools.dropwhile(predicate, iterable) opuszcza wartości dopóki warunek nie zostanie spełniony
data = [1, 2, 3, 4, 5, 6, 7, 8,9,10,1]
result = itertools.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)

print('-'*100)
#itertools.dropwhile(predicate, iterable) opuszcza wartości które nie spełniają warunku
data = [1, 2, 3, 4, 5, 6, 7, 8,9,10,1]
result = itertools.filterfalse(lambda x: x<5, data)
for each in result:
    print(each)

print('-'*100)
#itertools.islice(iterable, start, stop, [step])  - zacznij od 6 skończ na 8 (liczymy 0d 0)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for m in itertools.islice(months, 6, 8):
    print(m)

print('-' * 100)

#itertools.product(iterable,iterable) - iloczyn karteziański
spades = ['Hearts', 'Tiles', 'Clovers', 'Pikes']
figures = ['Ace', 'King', 'Jack', '10']
result = itertools.product(spades, figures)
for each in result:
    print(each)

print('-' * 100)
#itertools.repeat(object[,times])  - powtarzanie tesktu times razy
for i in itertools.repeat("tell me more", 5):
    print(i)

print('-' * 100)
data = [(1,2), (3,4), (5,6)]
#itertools.starmap(function,iterable])  -
result = itertools.starmap(operator.add, data)
for each in result:
    print(each)

print('-'*100)
#itertools.takewhile(predicate, iterable) - weź te elementy, dopóki  warunek jest prawdziwy
data = [1, 2, 3, 4, 5, 6, 7, 8,9,10,1]
result = itertools.takewhile(lambda x: x<5, data)
for each in result:
    print(each)

print('-'*100)

#itertools.tee(iterable, n=2) - utworzy iteratory niezalezne, przechodzące przez 1 wspólny wskazany iteraotor
cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
cars1, cars2 = itertools.tee(cars)

for each in cars1:
    print(each)
print('-------')
for each in cars2:
    print(each)

print('-'*100)
#itertools.zip_longest(*iterables, fillvalue=None)  - łaczy 2 listy (każdy element z jest łaczony z jednym zdrugim, a gdy nie mają jednakowej długości to stosuje fillvalue
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plan = ['busy', 'busy', 'busy', 'busy', 'busy', 'busy', 'free', 'free']
for m in itertools.zip_longest(months, plan, fillvalue='unknown'):
    print(m)