#Python programs on Global and local variable

def func(a,b,c):
    global d
    a = 2
    b = 4
    c = 6
    d = 8
    print(a,b,c,d)
a,b,c,d = 1,2,3,4
func(5,10,15)

#Output : 2 4 6 8

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

#Output : 7

z = 10
def func1():
    global z
    z = 3
def func2(x,y):
    global z
    z = -100
    z = z+1
    z = z-1
    return x+y+z
func1()
total = func2(4,5)
print(total)

#Output :  -91