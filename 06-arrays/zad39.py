arr=[1,2,3,4,5,6,7,3,4,5,6,2,4,5,6,8,100,320,234230,324203,320]
dl=len(arr)
x=""
      
for i in range(dl):
    if(arr[i]%2==1):
        x+=str(arr[i])
        x+=","

for i in range(dl):
    if(arr[i]%2==0):
        x+=str(arr[i])
        x+=","
    
print(x)