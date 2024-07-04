import json

def f(years, course):
    with open("data.json", "r") as file:
        data = json.load(file)

    # Filter students based on the criteria
    filtered_students = [
        student for student in data
        if student["age"] >= years and any(course_data["name"] == course and calculate_average_grade(course_data["grades"]) >= 4 for course_data in student["studies"]["courses"])
    ]

    # Remove duplicates based on the student's name
    unique_filtered_students = {student["name"]: student for student in filtered_students}.values()

    return len(unique_filtered_students)

def calculate_average_grade(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

# Example usage
result = f(21, "programming")
print(result)
