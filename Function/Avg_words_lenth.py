#Calculate average words length in a string.

#Sample Input
#"Hi, my name is Brinda Sahoo.I am a Python beginner."
#"Now I know Python a bit.Let me explore more!"
#Sample Output
'''4
 3 '''
 
def mysolution(str1):
    for p in "!?',;.-":
        str1 = str1.replace(p, ' ')
    words = str1.split()
    #print (len(words))
    sum1 = 0
    for word in words:
        sum1 = sum1 + len(word)
    average = sum1/len(words)
    avg = round(average)
    print (avg)
    return avg

str1 = "Hi, my name is Brinda Sahoo.I am a Python beginner."
str2 = "Now I know Python a bit.Let me explore more!"
mysolution(str1)
mysolution(str2)