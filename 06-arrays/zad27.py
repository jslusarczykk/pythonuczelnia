def star(n):
    return n*"*"

arr=[12, 6, 4, 9, 10]

for i in range(len(arr)):
    print(arr[i],":",star(arr[i]))