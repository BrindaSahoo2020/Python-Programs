#Simple practice in while loop

fruit = 'orange'
i = 0
l = len(fruit)
str1 = []

#step1 (print all the indivisual letters in a list)
while i < l :
    str1.append(fruit[i])
    i+=1
print(str1)

#step2 (print the index and letters)
#initiated i = 0 again as i became 5 in 1st step
i = 0
while i < l:
    letter = fruit[i]
    print (i,letter)
    i+=1

