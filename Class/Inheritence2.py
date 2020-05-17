#Python programs on Inheritence
#Sample output
'''
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Brinda)
(Initialized Teacher: Brinda)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)
Name:"Swaroop" Age:"25"
Marks: "75"
Name:"Mrs. Shrividya" Age:"40"
Salary: "30000"
Name:"Brinda" Age:"35"
Salary: "50000"
'''

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age))
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
t1=Teacher('Brinda',35,50000)
s = Student('Swaroop', 25, 75)
s.tell()
t.tell()
t1.tell()