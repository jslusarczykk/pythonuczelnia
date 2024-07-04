# Create the dictionary
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Display contents of the dictionary
print("a. Contents of the dictionary:")
print(person)
print()

# Display name
print("b. Name:", person["name"])
print()

# Display hobby
print("c. Hobby:", person["hobby"])
print()

# Change surname to 'Nowak'
person["surname"] = "Nowak"
print("d. Surname changed to 'Nowak':", person["surname"])
print()

# Change person's marriage status
person["married"] = not person["married"]
print("e. Marriage status changed. Now married:", person["married"])
print()

# Add gender: 'male'
person["gender"] = "male"
print("f. Gender added:", person["gender"])
print()

# Add a new hobby: 'bicycle'
person["hobby"].append("bicycle")
print("g. New hobby added:", person["hobby"])
print()

# Add work phone to existing phones: '313131444'
person["phone"]["work"] = "313131444"
print("h. Work phone added:", person["phone"])