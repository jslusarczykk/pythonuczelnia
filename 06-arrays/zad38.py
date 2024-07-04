arr=[1,2,3,4,5,6,7,3,4,5,6,2,4,5,6,8,100,320,234230,324203,320]
x=int(input("Enter number: "))
count=0
for i in range(len(arr)):
    if x<=arr[i]:
        count+=1
print(count)