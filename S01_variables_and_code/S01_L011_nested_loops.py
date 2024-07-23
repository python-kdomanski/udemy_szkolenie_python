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