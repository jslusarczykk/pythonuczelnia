name = input("What is your name?: ")  

for char in name:
    numeric_representation = ord(char)
    print(f"{char}","(",{numeric_representation},")")