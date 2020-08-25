#Exercises on Regular Expression continues
#Program1
import re

file1 = open('file3.txt')
for line in file1:
    line = line.rstrip()
    x = re.findall('[0-9]', line)
    print(line)

#Output ([0-9]	Returns a match for any digit between 0 and 9)
'''
1289045
0
8
71
23
'''
#Program2

x = "cant rember so many descriptions : 123@#"
y = re.findall('^c.*',x)
print(y)