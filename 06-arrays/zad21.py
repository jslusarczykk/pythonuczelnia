arr=[15, 8, 31, 47, 2, 19]
#reverse array
arr2=[0 for i in range(len(arr))]
print(arr2)

for i in range(len(arr)):
    arr2[i]=arr[len(arr)-i-1]
print(arr2)

print()
arr3 = [15, 8, 31, 47, 2, 19]
arr4 = arr3[::-1]

print(arr4)