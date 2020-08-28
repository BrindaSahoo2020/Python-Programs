#Find out a number is Perfect or not

#Perfect number is a positive integer that is equal to the sum of its proper divisors(e.g 6(divisor =1,2,3),28(divisor = 1,2,4,7,14),496)

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1,n):
    if ((n%i) == 0) :
        sum1 = sum1 + i
if (sum1 == n):
    print(n," is a Perfect number ")
else:
    print(n," is not a Perfect number ")