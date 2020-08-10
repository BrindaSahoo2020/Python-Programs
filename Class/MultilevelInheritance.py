#Python program to show Multilevel Inheritance

#Output (36,8,36)

class employee():
    def __init__(self,name,age,salary):  
        self.name = name
        self.age = age
        self.salary = salary

class employee1(employee):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
 
class employee2(employee1):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
emp1 = employee('Brinda',36,10000)
emp2 = employee1('Aashna',8,20000)
emp3 = employee2('Siba',36,30000)
 
print(emp1.age)
print(emp2.age)
print(emp3.age)