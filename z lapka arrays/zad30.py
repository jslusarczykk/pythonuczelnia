def bubblesort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

arr=[5,6,4,3,6,7,3,2]
arr2=[8,0,8]
arr3=[3,4,2,2,2,3,4,5,7]

print(bubblesort(arr))
print(bubblesort(arr2))
print(bubblesort(arr3))