
def zad49(x):
    return 0

def factorial(n):

    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)

def suma(n): #suma od 1 do N
    suma=0
    for i in range(1,n+1):
        suma+=i
    return suma

def suma2(n): #suma od 1 do N using recursion
    if n == 1:
        return 1
    else:
        return n + suma2(n-1)

def power(x,n):
    return x ** n

def power2(x,n):
        return x * power(x,n-1) #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

if __name__ == "__main__":
    print(factorial(5))
    print(suma(3))
    print(suma2(3))
    print(power(5,3))
    print(power2(5,3))