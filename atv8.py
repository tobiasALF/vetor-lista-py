list = [2,5,7,8,4,5,7,3,6,78]
maior = 0
menor = lista[0]

for x in list:
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print(maior )
print(menor)