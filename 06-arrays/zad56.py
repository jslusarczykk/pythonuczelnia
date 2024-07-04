#convert 2d into 1d
def convertTo1d(arr):
    dl=len(arr)
    dl2=len(arr[0])
    arr2=[0 for i in range(dl*dl2)]
    for j in range(len(arr)):
        for k in range(len(arr[0])):
            arr2[j]=arr[j][k]
            
    return arr2

print(convertTo1d([[2,3],[1,5]]))