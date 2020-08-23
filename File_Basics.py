#File Basics in python
#Program1(print the contents in a file)

xfile = open('file1.txt')
for i in xfile:
    print(i)

#Program2 (Count lines in file,here the count is 3)
yfile = open('file2.txt')
count = 0
for i in yfile:
    count = count + 1
print(count)

#Program3(calculate the length of file and print letters till position 10)
xfile = open('file1.txt')
xy = xfile.read()
l = len(xy)
print(l)
print(xy[:10])

#Program4(Search through lines)
xfile = open('file1.txt')
for i in xfile:
    if i.startswith('Pr'):
        print(i)