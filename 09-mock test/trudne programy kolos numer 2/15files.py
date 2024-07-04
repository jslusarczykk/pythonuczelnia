#f = open("numbers.txt")
#for line in f:
#     print(line, end="")
#f.close()

with open("numbers.txt",'r') as file:
    for line in file:
        print(line, end="")