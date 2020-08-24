#Count the words occured in one dictionary

#Input (I am learning Python and Python is interesting)

file1 = dict()
line = input("Enter a line :")
words = line.split()
for word in words:
    file1[word] = file1.get(word,0)+1
print(file1)

#Output 
#{'I': 1, 'am': 1, 'learning': 1, 'Python': 2, 'and': 1, 'is': 1, 'interesting': 1}