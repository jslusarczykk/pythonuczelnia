lista=[[2,5,4],[9,0,3]]
print(lista) #a
print(len(lista))

print(len(lista),len(lista[0]))

print(lista[0][1])
print(lista[1][2])
print(lista[1]) #poprawic e

x=""
for i in range(len(lista[1])):
    x+=str(lista[1][i])
for i in range(len(x)):
    print(x[i], end=" ")

print()

for n in lista[1]:
    print(n, end=" ")