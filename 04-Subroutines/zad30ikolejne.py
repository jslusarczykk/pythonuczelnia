def funkcja(number, even):
    sum_even_digits=0
    sum_odd_digits=0
    while(number>0):
        if(number%2==0):
            sum_even_digits+=number%10
        else:
            sum_odd_digits+=number%10
        number=number//10

    if even:
        return sum_even_digits
    else:
        return sum_odd_digits

#jesli true to parzysta jesli nie to nieparzysta
def NEN(x,y): #negative even numbers
    count=0
    for i in range(x,y+1):
         if i < 0 and i % 2 == 0:
            count += 1
    return count

def negativ(x,y,z):
    if(x<0 or y<0 or z<0) :
        return True
    return False

def asterix(n):
    ciag=""
    if(n==1):
        return "*"
    for i in range(n-1):
        ciag+="/*"
    return "*"+ciag

def dectostr(n):
    ciag=""
    for i in range(1,n+1):
        i=str(i)
        ciag+=i
    return ciag

def doing(x,y,variable):
    if(variable=="+"):
        return x+y
    if(variable=="-"):
        return x-y
    if(variable=="*"):
        return x*y
    if(variable=="%"):
        return x%y
    if(variable=="**"):
        return x**y    

if __name__ == "__main__":
    #print(funkcja(3124,True))
    #print(funkcja(3124,False))
    #print(funkcja(20576,False))
    #print(funkcja(20576,True))
    #print(funkcja(13115,True))
    #print(NEN(-7,8))
    #print(NEN(-1,11))
    #print(negativ(11,6,4))
    #print(asterix(4))
    #print(dectostr(11))
    #print(dectostr(4))
    print(doing(2,3,"**"))
    