file = open("sample3.txt",'r')
file2 = open("zad18.txt",'w')

file2.write(file.read())

file.close()
file2.close()