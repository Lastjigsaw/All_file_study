n = int(input("Fibonacci sequence (2-10): "))
while n < 2 or n > 10:
    print("Invalid Number!")
    n = int(input("Fibonacci sequence (2-10): "))
if n == 2:
    print("Fibonacci sequence up to %d : 0 1 1" %n, end=' ')
elif n == 3:
    print("Fibonacci sequence up to %d : 0 1 1 2" %n, end=' ')
else:
    print("Fibonacci sequence up to %d : 0 1 1 2", end=' ')
    a = 1
    b = 2
    for i in range(4, n+1):
        c = a + b
        a = b
        b = c
        print(c, end=' ')