decimal = int(input("Enter decimal number: "))
binary = ""
x=decimal

while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print(x, "(10) =", binary, "(2)")