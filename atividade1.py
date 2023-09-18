lis = [1,2,3,4,5,6,7,8,9,10]
vaz = []

for n in range(0,10):
    vaz.append(n)
    
    if n % 2 == 0:
        vaz.remove(n)

print(vaz)