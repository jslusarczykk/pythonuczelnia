import re

# Calculate the arithmetic mean
with open("grades.txt", 'r') as file:
    file_content=file.read()

# Using re.findall to extract float values from the text
marks = re.findall(r"\b\d+\.\d+\b",file_content)
print(marks)

# Convert the strings to float
marks = [float(mark) for mark in marks]

# Calculate the arithmetic mean
mean = sum(marks) / len(marks)

print("Arithmetic mean:", mean)