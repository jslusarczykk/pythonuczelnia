with open("numbers.txt",'r') as file:
    file_content=file.read()

with open("numberscopy.txt",'w') as plik:
    plik.write(file_content)