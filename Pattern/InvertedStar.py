#Print an Inverted Star Pattern

#Sample Output
'''
******
 *****
  ****
   ***
    **
     *
'''
n = 6
for i in range (n, 0, -1): 
    print((n-i) * ' ' + i * '*') 