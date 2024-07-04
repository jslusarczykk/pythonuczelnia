file = open("zad21.txt",'w')

for i in range(1,51):
    i=str(i)
    file.write(i)
    file.write("\n")

file.close()