#Find the maximum occurring character in given String

#SampleInput
#str1 = "I am going to merge four programs here"
#Sample Output
'''
{'I': 1, 'a': 2, 'm': 3, 'g': 4, 'o': 4, 'i': 1, 'n': 1, 't': 1, 'e': 4, 'r': 5, 'f': 1, 'u': 1, 'p': 1, 's': 1, 'h': 1}
Maximum occurring frequency is : 5
The maximum occurring character is : r
'''

str1 = "I am going to merge four programs here"
#step1 (remove space from string)
for i in str1:
    if i == ' ':
	    str2 = str1.replace(' ',"")
print(str2)

#step2 (get a dictionary having characters and its occurrences)
freq ={}
for i in str2:
	if i in freq:
		freq[i]=freq[i]+1
	else:
		freq[i]=1
print ("Frequency of occurrence of characters :",freq)

#step3 (find the maximum occurring frequency )
lst1 = []
for x in freq:
    lst1.append(freq[x])
max1 = lst1[0]
for i in lst1:
    if (max1 < i):
        max1 = i
print("Maximum occurring frequency is :",max1)

#step4 (find maximum occurring character)
for x in freq:
    if (freq[x] == max1):
        print ("The maximum occurring character is :",x)
