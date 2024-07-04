lista=[-15, 8, -31, 47, -2, 19]
#max and min number from array
max=0
min=999
for i in range(len(lista)):
    if(lista[i]>max):
        max=lista[i]
    if(lista[i]<min):
        min=lista[i]

print(max," ",min)