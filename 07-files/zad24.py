
import csv

file = open('studentslist.txt', 'r')

csv_reader = csv.reader(file)

# Skip the header row
header = next(csv_reader)

# Iterate through the rows and print data for students under 30
for row in csv_reader:
    first_name, last_name, age, gender, email = row

    age = int(age)

    if age < 30:
        print(f"{first_name} {last_name} {email}")

file.close()