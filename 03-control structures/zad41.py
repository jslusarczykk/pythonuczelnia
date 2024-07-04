correct_pin=805
x=0

for i in range(3):
    user_pin=int(input("Enter the PIN code: "))
    if(user_pin==correct_pin):
        print("Your pin is correct")
        x+=1
        break
    else:
        print("Incorrect")

if(x==0):
    print("Sorry your payment card has been blocked")


