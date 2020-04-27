#Python program to print even length words from a string

#Sample Input
'''s = "I am learning python" ''' 
#SampleOutput
'''Even words are : ['am', 'learning', 'python']'''

s = str(input("Enter a string : "))  
s1 = s.split(' ')
list1 = []
for word in s1:  
    if (len(word)%2) == 0:
        list1.append(word)
print("Even words are :",list1)