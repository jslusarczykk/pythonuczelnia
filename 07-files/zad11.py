file = open("numbers.txt", "r")

total_sum = 0
for line in file:
    number = int(line) #rstrip z prawej strony strip calosc
    total_sum += number

file.close()

print("Sum of numbers:", total_sum)

#wrocic do tego zadania