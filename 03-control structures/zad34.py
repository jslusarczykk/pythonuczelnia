amount = int(input("Enter the amount in PLN: "))

number5=amount//5
reszta=amount-number5*5
number2=0
number2=reszta//2
reszta2=reszta-number2*2

if(reszta2==1):
    number1=1
else:
    number1=0

print(number5,number2,number1,amount)

#while(amount>0):
    #if(amount%5==0):
        
        