listaA = list(range(6))
listaB = list(range(6))

print(listaA,listaB)

product=[]

for a in listaA:
    for b in listaB:
        product.append((a,b))

print(product)

product = [(a,b) for a in listaA for b in listaB]
print(product)

product = [(a,b) for a in listaA for b in listaB if a % 2==1 and b % 2==0]
print(product)

product = {a:b for a in listaA for b in listaB if a % 2==1 and b % 2==0}
print(product)

gen = ((a,b) for a in listaA for b in listaB if a % 2==1 and b % 2==0)
print(gen)
print(next(gen)) #generator zwraca daną wartość tylko raz (jakby licznik)
print(next(gen))
print('-'*30)
for x in gen:
    print(x)
print('-'*30)
for x in gen:
    print(x)

gen = ((a,b) for a in listaA for b in listaB if a % 2==1 and b % 2==0)

print('-'*30)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('Wszytskie pozycje z generatora zostały wykorzystane')
        break
