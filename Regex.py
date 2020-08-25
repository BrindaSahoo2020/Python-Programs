#Exercise on Regular Expression

#Program1
import re

file3 = open('file3.txt')
for line in file3:
    line = line.rstrip()
    if re.search('I',line):
        print(line)
#Output
'''
I learnt to use it!!!!
 I can use it in many codes(line has a spaceat the beginnig)
'''
#Program2
file3 = open('file3.txt')
for line in file3:
    line = line.rstrip()
    if re.search('^I',line):
        print(line)

#Output
#I learnt to use it!!!!(^ : Starts with)

#Program3

file3 = open('file3.txt')
for line in file3:
    line = line.rstrip()
    if re.search('.',line):
        print(line)

#Output
'''
a : 2.3
b : aaabbbb4*7.0 = 28.0@#rtyu
'''
#Program3

file3 = open('file3.txt')
for line in file3:
    line = line.rstrip()
    if re.search('$',line):
        print(line)

#Output($)