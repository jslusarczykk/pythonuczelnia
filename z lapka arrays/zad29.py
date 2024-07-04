arr1=[4,36,12,28,9,44,5] 
arr2=[5,1,36]

numbers="" #numbers from the first array that do not appear in the second array

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr1[i]==arr2[j]):
            break
        if(j==len(arr2)-1):
            numbers+=str(arr1[i])
            numbers+=" "
            
print(numbers)
