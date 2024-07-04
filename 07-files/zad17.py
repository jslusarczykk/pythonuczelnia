#sample3.txt
file = open("sample3.txt",'r')

for i in range(5):
    print(file.readline())

counter=0
for line in file:
    if(counter%5==0):
        input() #enter
    print(file.readline())
    counter+=1

    

file.close()