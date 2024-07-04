arr=[-15, 8, -31, 47, -2, 19]
min=9999
max=0
for i in range(len(arr)):
    if(max<arr[i]):
        max=arr[i]
    if(min>arr[i]):
        min=arr[i]
    
print(min," ",max)