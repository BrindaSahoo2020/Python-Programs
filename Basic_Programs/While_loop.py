#Simple python programs on while loop
#Program1

lst= []
i = 1
while True:
    if i%0O7 == 0:
        break
    lst.append(i)
    i += 1
print(lst)

#Output : [1, 2, 3, 4, 5, 6]

#Program2

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)

#Output: 0 1 2 0

#Program3

x = "abcdef"
i = "a"
while i in x:
    print(i, end = " ")

#Output : infinite a will be printed

#Program4

x = "abcdef"
while i in x:
    print(i, end=" ")

#Output :Error,as i is not defined

