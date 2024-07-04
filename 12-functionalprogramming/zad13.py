#2% for 500ml bottle
#3% for 1000ml bottle
#5% for 1500ml bottle

# plus minus x procent

#def correct(tolerance):
 #   def check(bottle):
  #      if x >

def lepsza(bottle):
    if bottle>=0.98*500 and bottle <= 1.02 * 500 : #ta funkcja dziala
        return True
    elif bottle >=1000*0.97 and bottle <=1000*1.03:
        return True
    elif bottle>=1500*0.95 and bottle<=1500*1.05:
        return True
    return False

def better(bottle):
    def check(tolerance):
        if bottle>=0.98*500 and bottle <= 1.02 * 500 : #ta funkcja nie dziala
            return True
        elif bottle >=1000*0.97 and bottle <=1000*1.03:
            return True
        elif bottle>=1500*0.95 and bottle<=1500*1.05:
            return True
        return False
    return check
        

#badamy granice czy ma najbizej do 1500 czy 1000 czy 500
#if bottle between x and y
#podajemy procent do drugiej funckji
#
        

print(lepsza(507)) 
print(lepsza(489)) 
print(lepsza(984)) 
print(lepsza(1032)) 
print(lepsza(1578)) 
print(lepsza(1430)) 

#wrocic do tego