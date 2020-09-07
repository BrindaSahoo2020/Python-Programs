#Remove the repeated character from a string and reprint the string

str1 = "PYPTHOOOONN"
str2 = ""
for i in str1:
    if i not in str2:
        str2 = str2 + i
print(str2)

#Output(PYTHON)
