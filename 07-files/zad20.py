file = open("meatandfish.txt",'r')
file2 = open("grainsandbread.txt",'r')
file3 = open("zad20allproducts.txt",'w')
file3.write(file.read())
file3.write(file2.read())

file.close()
file2.close()
file3.close()
