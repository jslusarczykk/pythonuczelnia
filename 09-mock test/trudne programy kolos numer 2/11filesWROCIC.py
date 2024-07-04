file=open("numbers.txt",'r')
sum=0
for line in file:
    sum+=int(file.readline)
print(sum)
file.close()

