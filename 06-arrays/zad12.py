lista=[1,2,3,4,5,6,7,8,100,101]
even_sum=0
odd_sum=0
for i in range(len(lista)):
    if(lista[i]%2==0):
        even_sum+=lista[i]
    if(lista[i]%2==1):
        odd_sum+=lista[i]

print(even_sum," ",odd_sum) 

even_sum=0
odd_sum=0
while(i<len(lista)):
    if(lista[i]%2==0):
        even_sum+=lista[i]
    if(lista[i]%2==1):
        odd_sum+=lista[i]
print(even_sum," ",odd_sum) 