sum = 0
print("Using while loop ...")
n = int(input("Enter a number (1-10): "))
while n < 1 or n > 10:
    n = int(input("Enter a number (1-10): "))

for i in range(n, 0, -1):
    if i%2 == 1:
        print(i, end=" ")
        sum = sum + i
print(" ")
print("Sum =",sum)
