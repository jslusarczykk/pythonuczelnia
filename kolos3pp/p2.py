def f(arr):
    for i in range(len(arr)):
        if(arr.count(arr[i])==1):
            return arr[i]
