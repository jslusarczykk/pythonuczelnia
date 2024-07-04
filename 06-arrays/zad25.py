arr=[15, 8, 31, 47, 2, 19]
#aritchmetic mean srednia using while

sum=0
#for i in range(len(arr)):
#    sum+=arr[i]
i=0
while i<len(arr):
    sum+=arr[i]
    i+=1



mean=sum/len(arr)
print(mean)