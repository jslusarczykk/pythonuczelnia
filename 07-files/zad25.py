import re
temp = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

temperature = re.findall("\d{2}",temp)
print(temperature)
suma=0
for i in range(len(temperature)):
    temperature[i]=int(temperature[i])
    suma+=temperature[i]
print(suma/len(temperature))