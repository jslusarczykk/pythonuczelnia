# check whether all elements of the first array appear in the second array
arr1=[1,2,3,4,5]
arr2=[1,2,3,4,5,6,7]
arr3=[1,2,3,4]

def repeating(arr1,arr2):
    for elem in arr1:
        if elem not in arr2:
            return False
    return True

print(repeating(arr1,arr2))
print(repeating(arr2,arr3))
print(repeating(arr1,arr3))
print(repeating(arr3,arr1))
                
            