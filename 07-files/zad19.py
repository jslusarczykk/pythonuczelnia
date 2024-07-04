file = open("sample3.txt",'r')
file2 = open("zad19.txt",'w')
for line in file:
    file2.write(line)

file.close()
file2.close()