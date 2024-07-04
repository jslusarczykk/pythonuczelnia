import random
file = open("zad22.txt",'w')

for i in range(50):
    x=random.randint(100,999)
    x=str(x)
    file.write(x)
    file.write("\n")

file.close()