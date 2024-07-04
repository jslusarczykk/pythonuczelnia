def f(arr): #jeden raz w tablicy
    sum=0
    arr2=[0 for i in range(len(arr))]
    arr3=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        if arr[i] in arr2 and arr[i] not in arr3 :
            sum-=1
            arr3[i]=arr[i]
        if arr[i] not in arr2 :
            arr2[i]=arr[i]
            sum+=1
    return sum

print(f([11,22,33,11]))
print(f([11,22,11,11,11,35,27,11,11,14]))
