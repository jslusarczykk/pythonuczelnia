import re

file = open("sample3.txt", 'r')
file2 = open("zad28.txt", 'w')

for line in file:
    line2 = re.findall(r'\b(\w{6})\b', line)
    #line2 = re.findall("\w{6}", line)     #                                                               
    if line2:
        file2.write('\n'.join(line2) + '\n')

file.close()
file2.close()