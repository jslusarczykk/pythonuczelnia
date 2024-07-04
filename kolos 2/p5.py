def f(arr): #[4,15] [3,9], [-3,-9] returns 1 
    sum=0
    for i in range(len(arr)):
        numer=int(arr[i][0])
        if numer ** 2 == arr[i][1] :
            sum+=1
    return sum

print(f([[4,16],[3,9],[-3,9]]))
print(f([[4,15],[3,9],[-3,-9]]))