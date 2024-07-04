binary=str(input("Enter binary number: "))

sum=0
potega=0
y=len(binary)-1

for i in range(len(binary)):
    if(binary[y]=='1'):
        sum+=2**potega
    potega+=1
    y=y-1

print(f"Binary number in dec is:{sum}")