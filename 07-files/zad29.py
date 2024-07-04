import re

# Calculate the arithmetic mean
file = open("grades.txt", 'r')

# Use a raw string for the regular expression pattern
float_pattern = r"\b\d+\.\d+\b"

# Using re.findall to extract float values from the text
marks = re.findall(float_pattern, file.read())
print(marks)
# Convert the strings to float
marks = [float(mark) for mark in marks]

# Calculate the arithmetic mean
mean = sum(marks) / len(marks)

print("Arithmetic mean:", mean)

file.close()