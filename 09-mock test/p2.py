#f([7,7,7,7,7,5,7,7]) 
def f(arr): #szuka numeru innego niz reszta
    if(arr[0]!=arr[1]):
        if(arr[0]!=arr[2]):
            return arr[0]
        else:
            return(arr[1])

    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            return arr[i]

print(f([7,7,7,7,7,5,7,7]))