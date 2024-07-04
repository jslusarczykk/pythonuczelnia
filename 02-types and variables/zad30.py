import random
x=random.randint(1,6) 

print(f"Dice rolled: {x}")
if(x==1 or x==6):
    print("Special number: True")
else:
    print("Special number: False")