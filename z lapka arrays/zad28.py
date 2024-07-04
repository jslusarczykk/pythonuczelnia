def compare(arr1,arr2):
    if(len(arr1)!=len(arr2)):
        return False
    x=""
    y=""
    for i in range(len(arr1)):
        x+=str(arr1[i])
        y+=str(arr2[i])
    if(x==y):
        return True
    return False
        
arr1=["water","book","sky"]   
arr11=["water","book","sky"]
arr2=[True,False]   
arr22=[True,False,True]
arr3=[5,3,1]   
arr33=[5,3,1]
arr4=[3,2,1]   
arr44=[3,2]

print(compare(arr1,arr11))
print()
print(compare(arr2,arr22))
print()
print(compare(arr3,arr33))
print()
print(compare(arr4,arr44))
print()