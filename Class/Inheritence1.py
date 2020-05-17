#Python programs on Inheritence
#Sample output
'''
Derived_Demo's __new__() invoked
Demo's __init__() invoked
Demo's __new__() invoked
'''
class Demo:
    def __new__(self):
        self.__init__(self)
        print("Demo's __new__() invoked")
    def __init__(self):
        print("Demo's __init__() invoked")
class Derived_Demo(Demo):
    def __init__(self):
        print("Derived_Demo's __init__() invoked")
    def __new__(self):
        print("Derived_Demo's __new__() invoked")
def main():
    obj1 = Derived_Demo()
    obj2 = Demo()
main()
