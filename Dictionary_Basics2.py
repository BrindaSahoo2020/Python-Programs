#Exercises on Dictionary

count = dict()
names = ['Siba','Brinda','Aashna','Aashna']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)

#The 'get' method for Dictionaries
x = count.get('Brinda')
y = count.get('Aashna')
z = count.get('Siba')
print(x,y,z)

#counting with get()
count = dict()
names = ['Siba','Brinda','Aashna','Aashna']
for name in names:
    count[name] = count.get(name,0 ) + 1
print(count)

#Output
# {'Siba': 1, 'Brinda': 1, 'Aashna': 2}
#1 2 1
#{'Siba': 1, 'Brinda': 1, 'Aashna': 2}
