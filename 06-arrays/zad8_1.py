lista=[2,3,7,5,4]

print(lista) #a
print(len(lista)) #b
print(lista[0])
print(lista[1])
print(lista[len(lista)-1])
print((lista[0]+lista[len(lista)-1]))
print(lista[(len(lista)-1)//2])

#i  
for i in range(len(lista)):
    print(lista[i], end=" ")
#j
print()
for i in range(len(lista)//2+1):
    print(lista[i], end=" ")