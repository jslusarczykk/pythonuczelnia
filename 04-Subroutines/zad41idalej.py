
def ifprime(x):
    for i in range(2,x-1):
        if(x%i==0):
            return False
    return True
def Nprime(x):
    counter=0
    number=2
    while(counter<x):
        if(ifprime(number)):
            counter+=1
        number+=1
    return number-1

def difference(x,y,z):
    big=max(x,y,z)
    small=min(x,y,z)
    return big-small

def acronym(x):
    acr=x[0]
    for i in range(1,len(x)):
        if(x[i]==" "):
            acr+=x[i+1]
    return acr

def f(number):
    number_str = str(number)
    repeated_sum = 0

    for digit in number_str:
        if number_str.count(digit) > 1:
            repeated_sum += int(digit)

    return repeated_sum

def truepassword(x):
    if(len(x)<6):
        return False
    
    seen_chars = set()

    for char in x:
        if char in seen_chars:
            return False
        seen_chars.add(char)

    return True

def zad45(expression):
    result = 0
    current_number = 0
    current_operator = 1  # 1 represents addition, -1 represents subtraction

    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '+':
            result += current_operator * current_number
            current_number = 0
            current_operator = 1
        elif char == '-':
            result += current_operator * current_number
            current_number = 0
            current_operator = -1

    # Add the last number in the expression
    result += current_operator * current_number

    return result


#def addsubtr(x):
 #   suma=0
  #  number1=0
   # number2=0
    #suma=0
    #for i in range(1,len(x)):
     #   if(x[i]==)
      #  if(x[i]=='+'):
       #   suma+=x[i-1]+x[i+1] 
        #if(x[i]=='-'):
         # suma-=x[i+1]
    #return suma  

#string = "Hello, world!"
#string_without_spaces = string.replace(" ", "")
#print(string_without_spaces)

def zad46(x,y):
    suma=0
    for i in range(x,y+1):
        if(i%2==0 and i%3==0 and i%4!=0):
            suma+=i
    return suma

def zad47(tekst):
    znak=""
    for i in range(len(tekst)):
        znak+=tekst[i]+"-"
    return znak[:-1]

def iloscyfr(x):
    counter=0
    while(x>0):
        counter+=1
        x=x//10
    return counter


def zad48(x):
    x=int(x)
    y=x%10 #remainder of 7
    x=x//10
    sum_digits=0
    for i in range(iloscyfr(x)):
        sum_digits+=x%10
        x=x//10
    if(sum_digits%7==y):
        return True
    return False

#def zad49(number):
#    number_str = str(number)
#    highest_repeated
#    repeated_sum = 0
#    seen_chars = set()

    #for char in x:
       # if char in seen_chars:
      #      return False
     #   seen_chars.add(char)

    #return True
   # for digit in number_str:
  #      if number_str.count(digit) > 1:
 #           repeated_sum += int(digit)

 #   return repeated_sum

if __name__ == "__main__":
    print()
    #print(ifprime(1))
    #print(Nprime(9))
    #print(difference(2,12,8))
    #print(acronym("Python"))
    #print(truepassword("booo3sdf"))
    #print(addsubtr("2+3"))
    #print(zad47("Uni"))
    #print(zad48("1082"))
    #print(zad48("2035"))
    #print(zad48("1114"))
    #print(zad48("1114"))
    #print(zad46(10,30))
    #print(iloscyfr(1082))
    #print(zad45("2+3-4+2"))