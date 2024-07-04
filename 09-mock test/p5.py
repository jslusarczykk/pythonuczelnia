import re

def f(first_letter, last_letter):
    with open("data.txt", "r", encoding="utf-8") as file:
        file_content = file.read()

    pattern = r'\b' + re.escape(first_letter) + r'\w*' + re.escape(last_letter) + r'\b'
    matches = re.findall(pattern, file_content)

    return len(matches)

# Example usage
result = f("w", "d")
print(result)