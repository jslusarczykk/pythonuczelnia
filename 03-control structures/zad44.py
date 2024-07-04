quantity=0
sum=0
while(1==1):
    number=int(input("Enter number: "))
    if(number==0):
        break    
    quantity+=1
    sum+=number
    

mean=sum//quantity
print(quantity,sum,mean)

