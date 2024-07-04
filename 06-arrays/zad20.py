arr=[34,7,19,4,21,8]
even_sum=0
#using while

i=0
while i<len(arr):
    if(arr[i]%2==0):
        even_sum+=arr[i]
    i+=1
    
print(even_sum)