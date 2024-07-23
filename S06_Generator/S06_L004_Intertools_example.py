import itertools as it

mylist = ['a', 'b', 'c', 'd']

# for combination in it.combinations(mylist, 3):
#     print(combination)
#
# for combination in it.permutations(mylist, 3):
#     print(combination)

# for combination in it.combinations_with_replacement(mylist, 3):
#     print(combination)

money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1] #jakie mamy w prortfelu - chcemy wypłacić 100

results =[]

for i in range(1,101):
    for combination in it.combinations(money, i):
        if sum(combination) == 100:
            results.append(combination)

results = set(results) #zamieniamy na set by wykluczyć powtórzenia

for result in results:
    print(result)

print('-'*30)
money = [50, 20, 10, 5]

for i in range(1,101):
    for combination in it.combinations_with_replacement(money, i):
        if sum(combination) == 100:
            print(combination)
