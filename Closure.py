#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier
mul1 = make_multiplier(3)
mul2 = make_multiplier(5)
mul3 = make_multiplier(4)

print(mul1(6))
print(mul2(3))
print(mul3(10))

#Output
'''
18
15
40
'''