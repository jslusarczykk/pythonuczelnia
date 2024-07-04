lista=[1,2,3,4,5]

lista[0]-=1
print(lista[0])

lista[len(lista)-1]+=4
print(lista[len(lista)-1])

lista[len(lista)//2]*=2
print(lista[len(lista)//2])

for i in range(len(lista)):
    lista[i]+=3
    print(lista[i], end=" ")