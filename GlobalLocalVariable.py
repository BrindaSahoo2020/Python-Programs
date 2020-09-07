#Exercises on Global and Local variable concepts

def f1():
    global x
    x+=1
    print(x)
x=12
print("x")

#Output (x)

def f1(x):
    x+=1
    print(x)
f1(15)
print("hello")

#Output 
'''
16
hello
'''

x=12
def f1(a,b=x):
    print(a,b)
x=15
f1(4)

#Output (4 12)

def f():
    global a
    print(a)
    a = "hello"
    print(a) 
a = "world" 
f()
print(a)

#Output (world hello hello)

x = 5 
def f1():
    global x
    x = 4
def f2(a,b):
    global x
    return a+b+x
f1()
total = f2(1,2)
print(total)

#Output 7

x=100
def f1():
    global x
    x=90
def f2():
    global x
    x=80
print(x)

#Output 100