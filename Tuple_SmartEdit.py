#Add new items to Tuple(Notes: Tuples are immutable)

x = ('a','b','c','d')
y = list(x)
y.append('e')
x = tuple(y)
print(x)

#Output : ('a', 'b', 'c', 'd', 'e')

#Tuple Concatenation and delete

tp1 = ("1", "2" , "3")
tp2 = (1, 2, 3)

tp3 = tp1 + tp2
print(tp3)
del tp3
print(tp3)

#Output :('1', '2', '3', 1, 2, 3)
#NameError: name 'tp3' is not defined (As tp3 is deleted)