decimal = int(input("Enter decimal number: "))
binary = ""

while decimal>0 :
    remainder=decimal%2
    decimal=decimal//2
    if(remainder==1):
        binary+='1'
    else:
        binary+='0'

binary=binary[::-1]
print(binary)