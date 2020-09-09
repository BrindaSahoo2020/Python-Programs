#Example on Multiple inheritence

class A:
    def test(self):
        print("test of A called")
class B(A):
    def test(self):
        print("test of B called")
        super().test()  
class C(A):
    def test(self):
        print("test of C called")
        super().test()
class D(B,C):
    def test2(self):
        print("test of D called")      
obj=D()
obj.test()

#Output
'''
test of B called
test of C called
test of A called
'''