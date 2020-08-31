#Program to access public and protected member from a class
#Program1
class Variable:
     def __init__(self):
         self.a = 1
         self.__b = 1
     def display(self):
         return self.__b
obj = Variable()
print(obj.a)
obj.a = 5
print(obj.a)

#Output ( 1 & 5)
#We can change the values of public class members using the object of the class.

#Program2
class Variable:
     def __init__(self):
         self.a = 1
         self._b = 4
     def display(self):
         return self._b
obj = Variable()
print(obj._b)

#Output (4)
