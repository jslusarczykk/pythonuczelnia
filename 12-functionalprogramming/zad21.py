arr=[i+1 for i in range(20)]
#divisible by 2 and 3 without remainder

arr2 = list(filter(lambda x: x%2==0 and x%3==0, arr))
print(arr2)