print("Displays prime numbers from 1 to N.")
n = int(input("Please enter a value of n: "))
for i in range(1, n+1):
    if i == 2:
        print("They are %d" %i, end=' ')
    elif i > 2:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                print(i, end=' ')