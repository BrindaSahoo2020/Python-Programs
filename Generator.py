#Print cube of 5 numbers using Generator
#example1

def cube():
    for i in range(1,11):
        yield (i*i*i)
value = cube()
for i in value:
    print(i)
#Output
'''
1
8
27
64
125
216
343
512
729
1000
'''
#example2

def generator():
    n = 1
    print("n displayed 1st time")
    yield n

    n = 2
    print("n displayed 2nd time")
    yield n

    n = 3
    print("n displayed 3rd time")
    yield n
for i in generator():
    print(i)

#Output 
'''
n displayed 1st time
1
n displayed 2nd time
2
n displayed 3rd time
3
'''

#example3

def fib(n): 
    a, b = 0, 1
    while a < n: 
        yield a 
        a, b = b, a + b 

for i in fib(10):  
    print(i) 

#Output
'''
0
1
1
2
3
5
8
'''