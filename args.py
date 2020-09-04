#Example on usage of *arg

def func(*argv):
    for i in argv:
        print(i)

func('I','am','new','to','python')

def mathematics(*arg):
    for x in arg:
        print(x)

mathematics(1,2,3,4,5)

def func1(arg1,*arg):
    print("First argument is :",arg1)
    for i in arg:
        print(i)  

func1('ab','cd','ef','gh')

def add(*num):
    sum1 = 0 
    for i in num:
        sum1 = sum1 + i
    print("Sum:",sum1)

add(3,5)
add(4,5,6,7,9,0)

#Output
'''
I
am
new
to
python
1
2
3
4
5
First argument is : ab
cd
ef
gh
Sum: 8
Sum: 31
'''