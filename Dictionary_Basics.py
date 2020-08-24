#Exercises on Dictionary

fruit = dict()
fruit['orange'] = 10
fruit['banana'] = 6
fruit['apple'] = 15
print(fruit)
fruit['cherry'] = fruit['banana'] + 2
print(fruit)
print(fruit['apple'])
fruit['orange'] = 12
print(fruit)

#Output
'''{'orange': 10, 'banana': 6, 'apple': 15}
{'orange': 10, 'banana': 6, 'apple': 15, 'cherry': 8}
15
{'orange': 12, 'banana': 6, 'apple': 15, 'cherry': 8}
'''