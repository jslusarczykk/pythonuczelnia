file = open("zad23.txt",'w')

for i in range(1,11):
    i2=i**2
    i3=i**3
    i=str(i)
    i2=str(i2)
    i3=str(i3)
    file.write(i)
    file.write(",")
    file.write(i2)
    file.write(",")
    file.write(i3)
    file.write("\n")

file.close()

#druga wersja lepsza
file = open("zad23.txt", 'w')

for i in range(1, 11):
    i2 = i**2
    i3 = i**3
    file.write(f"{i},{i2},{i3}\n")

file.close()