import random
x=random.randint(1,6) 
guess=int(input("Guess from 1 to 6: "))

if(x==guess):
    print(True)
else:
    print(False)