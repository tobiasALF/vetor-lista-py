frut = ['banana','pera','uva','melão','melancia','laranja','abacate','tangirina']
list = []

for x in frut:
    tamanho = len(x)

    if tamanho > 5:
        list.append(x)

print(list)