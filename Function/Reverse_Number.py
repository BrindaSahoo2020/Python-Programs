#Reverse a number using function

def reverse(x):
    str1 = str(x)
    if str1[0] == '-':
        print(int('-'+str1[:0:-1]))
    else:
        print(int(str1[::-1]))
    
reverse(-768)
reverse(3780)
reverse(120000)

#Output(-867 ,873,21)