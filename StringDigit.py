#How do you check if a string contains only digits

str1 = str(input("Enter a string :"))
if str1.isdigit():
    print(str1," contains only digit")
else:
    print(str1," does not contain only digit")