# Find First Non Repeated Character in a String 

#Sample Input :("learnpythontoday")

#Sample Output :(First non-repeating character is: l)

str1 = "learnpythontoday"
while (str1 != ""):
    l = len(str1)
    ch = str1[0]
    str1 = str1.replace(ch, "")
    l1 = len(str1)
    if (l1 == l-1):
        print ("First non-repeating character is:",ch)
        break
else:
    print ("No Unique Character Found!")

 

