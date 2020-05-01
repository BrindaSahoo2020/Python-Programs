#Python programs on different Set Methods

#Adding Items
set1 = {"apple", "banana", "cherry"}
set1.add("orange")
print(set1)
#Output
#{'orange', 'banana', 'cherry', 'apple'}

#Addig Multiple Items
set1 = {"apple", "banana", "cherry"}
set1.update(["orange", "mango", "grapes"])
print(set1)
#Output
#{'mango', 'orange', 'grapes', 'banana', 'apple', 'cherry'}

#Removing Items - Method1
set1 = {"apple", "banana", "cherry"}
set1.remove("apple")
print(set1)
#Output
#{'banana', 'cherry'}

#Removing Items - Metho2
set1 = {"apple", "banana", "cherry"}
set1.discard("apple")
print(set1)
#Output
#{'banana', 'cherry'}

#Removing Items - Method3
set1 = {"apple", "banana", "cherry"}
set1.pop()
print(set1)
#Output
#{'apple', 'banana'}
#Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

#Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Output
#{1, 2, 3, 'a', 'b', 'c'}