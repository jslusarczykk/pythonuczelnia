
def person3(x):
    count=0
    for i in range(len(x)):
        if(x[i]=="-"):
            count=0
        if(x[i]=="+"):
            count+=1
        if(count==3):
            return True
    return False

def NFIB(x):
    first=0
    second=1
    for i in range(x-1):
        first+=second
        second+=second+first
    return first+second

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    
def f(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

# Test cases
print(f(5))  # Output: 3
print(f(9))  # Output: 21


def palindrom(x):
    for i in range(len(x)):
        if(x[i]!=x[len(x)-i-1]):
            return False
    return True

def seqnospace(x):
    ciag=""
    for i in range(len(x)):
        if(x[i]==" "):
            x
        else:
            ciag+=x[i]
    return ciag

def sord(x):
    lista=[]
    lista2=[]
    counter=0
    for i in range(x):
        y=x%10
        x=x//10
        if(y not in lista):
            lista.append(y)
            lista2.append(y)
        else:
            counter+=y
    for i in range(x):
        for j in range(j):
            if(lista2[i]==lista2[j]):
                lista[i].remove()
    for i in range(x):
        counter+=lista2[i]
    return counter

def f(number):
    number_str = str(number)
    repeated_sum = 0

    for digit in number_str:
        if number_str.count(digit) > 1:
            repeated_sum += int(digit)

    return repeated_sum

# Test cases
#print(f(1027))      # Output: 0
#print(f(230335))    # Output: 9
#print(f(513553007)) # Output: 21



if __name__ == "__main__":
    #print(person3("++-----++---++"))
    #print(NFIB(9))
    #print(fibonacci(9))
    #print(palindrom("12-11-21"))
    #print(seqnospace("A programming language is a system of notation for writing computer programs"))
    #print(SORD(1027))
    #print(sord(230335))
    print()