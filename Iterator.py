#Note : An Iterator is an object that contains a countable number of values .
#Consists of 2 methods (__iter__ and __next__())

list1 = [1,2,3,4,5,6]
lst = iter(list1)
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))

#Output
'''
1
2
3
4
'''
#Stop after 10 iteration
class Numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

obj1 = Numbers()
myiter = iter(obj1)

for x in myiter:
  print(x)

#Output
'''
1
2
3
4
1
2
3
4
5
6
7
8
9
10
'''