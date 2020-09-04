#Usage of Keyward arguments(**kwargs)

def func(a=1,b=2,c=3):
  print("Last one is:" ,c)

func(a = 5 , b = 'brinda', c = 'sahoo')

def func(a=1,b=2,c=3,d=4):
  print(a,b,c,d)

func(b = 'brinda', c = 'sahoo')

#Output
'''
Last one is: sahoo
1 brinda sahoo 4
'''