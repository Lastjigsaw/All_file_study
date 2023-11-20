w = int(input("Width (7-10): "))
while w < 7 or w > 10:
    print("Invalid Number!")
    w = int(input("Width (7-10): "))
    

b = int(input("Border (1-3): "))
while b < 1 or b > 3:
    print("Invalid Number!")
    b = int(input("Border (1-3): "))

for i in range(1, w+1):
    if i == 1 or i == w or i == b or i == w-b+1:
        print("*" * w)

    else:
        print("*"*b + " " * (w-4) + "*"*b)



