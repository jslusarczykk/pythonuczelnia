#kod dziala do poprawy jest zakres
def f(x):
    dl=len(x)
    dozwolone=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dozwolone2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dozwolone3=['1','2','3','4','5','6','7','8','9','0']
    if dl < 2 :
        return False
    elif dl == 2 :
        if x[0] in dozwolone or x[0] in dozwolone2 and x[1] in dozwolone3:
            return True
        else:
            return False
    elif dl == 3 :
        if x[0] in dozwolone or x[0] in dozwolone2 and x[2] in dozwolone3 and x[1] in dozwolone or x[1] in dozwolone2 or x[1] in dozwolone3:
            return True
        else:
            return False
    elif dl>3 and dl<6:
        if x[0] in dozwolone or x[0] in dozwolone2 and x[1] in dozwolone or x[1] in dozwolone2 or x[1] in dozwolone3:
            for i in range(2,dl):
                if(x[i] not in dozwolone3):
                    return False
        return True
    elif dl==6:
        if x[0] in dozwolone or x[0] in dozwolone2 and x[1] in dozwolone or x[1] in dozwolone2: #dwuznakowy
            return True
        elif x[1] in dozwolone3: #dlaczego ten kod nie dziala? nie ma false
            return False
    elif dl>7:
        return False

print(f("A4"))
print(f("a4"))
print(f("4a"))
print(f("bc123"))
print(f("bcd555"))
print(f("g80915"))