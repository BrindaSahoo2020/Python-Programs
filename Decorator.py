#Examples on Decorator usage

def decorator(func): 
    def inner1(x,y):   
        print("before Execution")   
        # getting the returned value 
        returned_value = func(x,y) 
        print("after Execution")   
        # returning the value to the original frame 
        return returned_value      
    return inner1 

@decorator
def addition(a, b): 
    return a + b 

a, b = 1, 2  
# getting the value through return of the function 
print("Sum =", addition(a, b)) 

#Output
'''
before Execution
after Execution
Sum = 3
'''