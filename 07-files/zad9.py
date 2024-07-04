file = open('countries.txt', 'r')
#nie dajemy file content
#r - read w-write(tworzy nowy plik i kasuje stary) a - append dodaje do istniejacego juz pliku
counter = 0
for line in file:
    counter += 1
    print(f"{counter}. {line}", end="")
file.close()