arr=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest=0
longest_str=""
for i in range(len(arr)):
    if(len(arr[i])>longest):
        longest=len(arr[i])
        longest_str=arr[i]
        
print(longest_str)