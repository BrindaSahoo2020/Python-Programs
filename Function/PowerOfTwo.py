#Find Whether a Number is a Power of Two

def power_of_two(n):
    if n > 0:
        return n & (n - 1) == 0 
    else:
        return False
 
n = int(input('Enter a number: '))
if power_of_two(n):
    print(n,"is power of two")
else:
    print(n,"is not power of two")