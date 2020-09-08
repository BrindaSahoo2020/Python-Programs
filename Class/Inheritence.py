#Examples of Inhitence 

class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

#Output (0 1)

class A:
     def __init__(self):
         self.__i = 1
         self.j = 5
 
     def display(self):
         print(self.__i, self.j)
class B(A):
     def __init__(self):
         super().__init__()
         self.__i = 2
         self.j = 7  
c = B()
c.display()

#Output (1 7)

class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()

#Output (3 1)

class A:
    def test1(self):
        print("A is called ")
class B(A):
    def test(self):
        print("B is called ")
class C(A):
    def test(self):
        print("C is called ")
class D(B,C):
    def test2(self):
        print("D is called ")        
obj=D()
obj.test()

#Output (B is called)