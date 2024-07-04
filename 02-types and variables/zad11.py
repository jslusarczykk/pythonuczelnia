zarobek_starego= input(" Podaj zarobek starego: ")
zarobek_starego=float(zarobek_starego)
matka= input(" Podaj zarobek matki: ")
matka=float(matka)
osoby=input("Podaj ilosc osob:  ")
osoby=int(osoby)
income = zarobek_starego + matka
srednia = income/osoby

print("Total income: ",income," income per person: ",srednia)