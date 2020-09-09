#Example on Over riding 

class Bird:
	species="bird"
	def __init__(self):
		print("bird is ready")
	def whoisthis(self):
		print("i am a bird")
	def swim(self):
		print("bird can swim")
class Penguin(Bird):
	def __init__(self):
		Bird.__init__(self)
		print("penguin is ready")
	def whoisthis(self):
		print("i am a penguin")
	def run(self):
		print("penguin can run")
class Eagle(Bird):
	def __init__(self):
		Bird.__init__(self)	
		print("eagle is ready")
	def fly(self):
		print("i can fly")
	def whoisthis(self):
		print("i am an egale")
obj1=Penguin()
print(obj1.species)
obj1.whoisthis()
obj1.swim()
obj1.run()
obj2=Eagle()
obj2.whoisthis()
obj2.fly()
obj2.swim()

#Output

'''
bird is ready
penguin is ready
bird
i am a penguin
bird can swim
penguin can run
bird is ready
eagle is ready
i am an egale
i can fly
bird can swim
'''
