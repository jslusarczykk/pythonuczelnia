import random
def length(element):
    if(element-99>0):
        return 3
    if element-9 > 0:
        return 2
    return 1

def minus(n):
    return n*"-"
arr=[random.randint(1,999) for i in range(8)]
#print(arr)

total_length=0
total_length+=25 #elementy dalsze
for i in range(len(arr)):
    total_length+=length(arr[i])
print(minus(total_length))
for i in range(len(arr)):
    print("| ",arr[i], end="")
print("|",end="")
print()
print(minus(total_length))

