#Examples on classes and objects usage

class Builtin():
	def __repr__(self):
		return '__repr__ built-in function called'
	def __str__(self):
		return '__str__ built-in function called'
obj1 = Builtin()
print(obj1)

#Output
#__str__ built-in function called  (__str__ is used for producing a string representation of an object’s value that Python can evaluate)

class student:
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = student(1, 'A')
stud1.age = 9
print(hasattr(stud1, 'age'))

#Output (True)

class student:
   'Base class for all students'
   def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade
   def display (self):
      print("Roll no : ", self.roll_no,  ", Grade: ", self.grade)
stud1 = student(1,'B')
print(stud1.__doc__)

#Output (Base class for all students)