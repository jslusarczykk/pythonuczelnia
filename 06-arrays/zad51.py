# size 3 by 5
arr=[[1,2,3,4,5],[3,5,6,3,2],[0,0,0,1,0]]
#swap the first and last row

arr2=[[0 for j in range(5)]for i in range(3)]
print(arr)
arr2[0]=arr[0]
arr[0]=arr[-1]
arr[-1]=arr2[0]
print(arr)