#Count the number of letters in a string using for loop

#Program1(count total number of letters in the given string)
str1 = 'brinda sahoo'
count = 0
for i in str1:
    count = count + 1
print("Number of letters in the string is : ",count)

#Output (Number of letters in the string is :  12)

#Program2(count the number of letter 'o' )
str1 = 'brinda sahoo'
count = 0
for i in str1:
    if (i == 'o'):
        count = count + 1
print("'o' came ",count,"times in the string")

#Output ('o' came  2 times in the string)