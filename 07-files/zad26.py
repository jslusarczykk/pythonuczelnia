import re

text = "To be, or not to be, that is the question"
#vowel - samogloska
vowels = re.findall('[aeiouAEIOU]', text)
vowels_am=0
for i in range(len(vowels)):
    vowels_am+=1

print(vowels_am)