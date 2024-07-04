def occurs(number,arr):
    for i in range(len(arr)):
        if(number==arr[i]):
            return True
    return False

def occur(number,arr):
    if number in arr:
        return True
    return False

arr=[15, 38, 7, 23, 14]
print(occurs(23,arr))
print()
print(occur(23,arr))