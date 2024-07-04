# size 3 by 5
arr=[[1,2,3,4,5],[3,5,6,3,2],[0,0,0,1,0]]
#swap the first and last column
#1 3 0 - 5 2 0
arr2=[[0 for j in range(5)]for i in range(3)]

for i in range(len(arr)):
    arr2[i][0]=arr[i][0]
    
for i in range(len(arr)):
    arr[i][0]=arr[i][-1]
    
for i in range(len(arr)):
    arr[i][-1]=arr2[i][0]

print(arr)