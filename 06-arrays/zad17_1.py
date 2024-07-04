def arrtostr(arr):
    x=""
    for row in arr:
        for elem in row:
            elem=str(elem)
            x+=elem 
            #x+=" "
    return x


arr=[[0,0,0],[0,0,0],[0,0,0]]

length=len(arr)

for row in range(length):
    if(row==0):
        arr[row][0]="1"
    elif(row==1):
        arr[row][1]="1"
    else:
        arr[row][2]="1"
print(arr)

allelementsofarraycount=0
for row in arr:
    for elem in row:
        allelementsofarraycount+=1

tablicastr=arrtostr(arr)
print(tablicastr)

for i in range(1,allelementsofarraycount+1):
    print(tablicastr[i-1], end=" ")
    if(i%3==0):
        print()