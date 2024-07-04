text = "To be, or not to be, that is the question"

words=0
for i in range(len(text)):
    if(text[i]==" "):
        words+=1

words+=1
print(words)

import re

#za pomocą re

def count_words(text):
    # Use a regular expression to find all words in the text
    words = re.findall(r'\b\w+\b', text)

    # Count the number of words
    num_words = len(words)

    return num_words

# Sample text
text = "To be, or not to be, that is the question"

# Call the function and print the result
result = count_words(text)
print(f"The number of words in the text is: {result}")