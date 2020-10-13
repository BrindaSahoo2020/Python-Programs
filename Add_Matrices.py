#Python program to add two Matrices ofsame size

#Sample Input
'''
x = [[1,2,3],[2,3,4],[3,4,5]]
y = [[2,3,0],[2,3,1],[4,3,2]]
'''
#Sample Output
'''
[3, 5, 3]
[4, 6, 5]
[7, 7, 7]
'''

x = [[1,2,3],[2,3,4],[3,4,5]]
y = [[2,3,0],[2,3,1],[4,3,2]]

z = [[0,0,0],[0,0,0],[0,0,0]] 

for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j] + y[i][j]
for k in z:
    print(k)

