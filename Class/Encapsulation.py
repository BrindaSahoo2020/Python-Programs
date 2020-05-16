#Program1
#Sample Output 
#Color is : Red
#Speed is : 100 km/h

class Car:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
i20 = Car(0,'Grey')
i20.speed = 100
i20.color = 'Red'
print("Color is :",i20.color)
print("Speed is :",i20.speed ,"km/h")

#Program2
#Sample Output :orange

class Fruit:
    def __init__(self):
        self.banana = 'banana'
        self.orange = 'orange'
    def display(self):
        print(self.orange)
obj1 = Fruit()
obj1.display()

#Program3
#Sample Output : 200
class Car:
    def __init__(self,price,speed):
        self.price = price
        self.speed = speed
    def set_speed(self,value):
        self.speed = value
    def get_speed(self):
        return self.speed
obj1 = Car(700000,100)
obj1.set_speed(200)
print(obj1.get_speed())

#Program4
#Sample Output :45

class Demo:
     def __init__(self):
         self.a = 1
         self.__b = 1
     def get(self):
         return self.__b
obj = Demo()
obj.a=45
print(obj.a)
