#Basics of class and object
#Class is the collection of object and Objects are instance of a class .
#self is used to represent the instance of the class. With this keyword,we can access the attributes and methods of the class in python. 
#__init__ is a constructer ,it can be called when an object is created from the class, and access is required to initialize the attributes of the class.

class Friends:
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
frnd1 = Friends("Aashna",9,"dance")
print(frnd1.name)

#Output (Aashna)
#Next program

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return 2*(self.length + self.width)
    def areaa(self,length,width):
        self.length = 6
        self.width = 8
        return self.length + self.width
a = Rectangle(2,3)
print(a.area())
print(a.areaa(2,3))

#Output 
'''10
14'''

