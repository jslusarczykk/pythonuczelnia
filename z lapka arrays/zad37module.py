def a(arr): #a.	A function that returns the second largest element in an array
    arr=sorted(arr)
    return arr[len(arr)-2]

def b(arr): #b.	A function that returns the difference between the largest and smallest values in an array
    min=999
    max=0
    for i in range(len(arr)):
        if min>arr[i]:
            min=arr[i]
        if max<arr[i]:
            max=arr[i]
    return max-min

def c(arr): #c.	A function that returns the median of numbers in an array. Do not use built-in functions.
    arr=sorted(arr)
    if(len(arr)%2==0):
        return (arr[len(arr)//2]+arr[len(arr)//2-1])/2
    return arr[len(arr)//2]

def d(arr): #d.	A function that returns a two-element array containing the smallest and largest values in an array
    min=999
    max=0
    arr1=[0,0]
    for i in range(len(arr)):
        if min>arr[i]:
            min=arr[i]
        if max<arr[i]:
            max=arr[i]
    arr1[0]=min
    arr1[1]=max
    return arr1

def e(arr): #e.	A function that returns array elements as a string, separated by the minus sign
    x=""
    for i in range(len(arr)):
        x+=str(arr[i])
        x+="-"
    return x[:-1]

if __name__ == '__main__': 
    arr3=[3,4,2,2,2,3,4,5,7,6]
    arr2=[7,3,8,5,2]
    print(b(arr2))
    print(a(arr2))
    #print(sorted(arr3))
    print(c(arr2))
    print(d(arr2))
    print(e(arr2))