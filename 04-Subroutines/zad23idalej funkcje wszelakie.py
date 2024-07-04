def funcjaE(s): #zad23
    count=0
    for i in range(len(s)):
        if(s[i]=='e'):
            count+=1
    return count

def ifinrange(x): #zad24
    max=int(input("Enter max range: "))
    min=int(input("Enter min range: "))
    if(x>=min and x<=max):
        return "Your number is in range"
    return "NOT IN RANGE"

#def anonymous(x,y):
 #   if(x>y):
  #      return True
   # else:
    #    return False

comparison = lambda x, y: True if x > y else False
zad26 = lambda x: True if x%2==0 else False

def f(card_number):
    print(card_number[:2],"**********",card_number[10:])

def ifbin(s):
    for i in range(len(s)):
        if(s[i]!='1' and s[i]!='0'):
            return False
    return True

def zad29(x):
    count=0
    piec=x//5
    x=x-piec*5
    dwa=x//2
    x=x-dwa*2
    if(x==1):
        count+=1
    count+=piec
    count+=dwa
    return count



if __name__ == "__main__":
    #print(funcjaE("eeeoooeee"))8
    #print(ifinrange(7))
    #print(comparison(34,25))
    #print(comparison(19,23))
    #print(zad26(232))
    #print(f("5290312400019022"))
    #print(ifbin("1110001"))
    #print(ifbin("101014fgfdgdfg01001"))
    print(zad29(0))