#Exercises to access private member in a class
#Method1
class Variable:
    def __init__(self):
        self.a = 1
        self.__b = 1
 
    def private(self):
        return self.__b
 
obj = Variable()
print(obj.__b)

#Output(AttributeError: 'Variable' object has no attribute '__b')

#Method2
class Variable:
    def __init__(self):
        self.a = 1
        self.__b = 1
 
    def private(self):
        return self.__b
 
obj = Variable()
print(obj.private())

#Output (1)