lista=[[1,3,5],[8,7,2]]
print(lista[0][0]+lista[len(lista)-1][len(lista[len(lista)-1])-1]) #a
print(lista[0][0]+lista[-1][-1])
#suma elementow srodkowych
suma_sr=0
for i in range(len(lista)):
    suma_sr+=(lista[i][len(lista[i])//2])
#suma elementow w ostatnim rzedzie
suma_ost=0
for i in range(len(lista[i])):
    suma_ost+=lista[-1][i]

#suma_ost=0
for i in lista[-1]:
    suma_ost+=i

print(suma_sr," ",suma_ost)
#w liscie dzialaja rozne dlugosci w tablicy nie ! 
# [[1,3,5],[8,7,2]] last row = [8,7,2]