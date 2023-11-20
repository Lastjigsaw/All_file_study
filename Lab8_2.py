num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
if num2 == num1:
    num2 = input("Enter number 2:")
num3 = input("Enter number 3: ")
if num3 == num2 or num3 == num1:
    num3 = input("Enter number 3: ")

if num1 > num2:
    if num1 > num3:
        if num3 > num2:
            middle = num3
        else:
            middle = num2
    else :
        middle = num1

elif num1 > num3:
    middle = num1

else :
    if num2 > num3:
        if num2 > num1:
            middle = num1
        else:
            middle = num2
    else:
        if num3 > num1:
            middle = num1
        else:
            middle = num3

print("The middle number of %d, %d and %d is %d" % (num1,num2,num3,middle))