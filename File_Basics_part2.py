#File Basics

#Program1(Searching Through a File without NewLine(\n))
xfile = open('file1.txt') #file1.txt contains newlines(\n)
for line in xfile:
    line = line.rstrip()
    if line.startswith('U'):
        print(line)

#Program2(Skip with Continue)
xfile = open('file1.txt') #Input file contains aline strats with space 
for line in xfile:
    line = line.rstrip()
    if not line.startswith(' '):
        continue
    print(line)

#Output (It will print the lines which are starting with space)

#Program3(Using 'in' to select lines)

xfile = open('file1.txt')
for line in xfile:
    line = line.rstrip()
    if not 'Programming' in line:
        continue
    print(line)