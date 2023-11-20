print("Printing 1 to 9 using for Loop ...")
for i in range(1, 10):
    if i != 9 and i != 8 :
        print("%d," % i, end=" ")
    elif i == 8 :
        print("%d and" % i, end=" ")
    else:
        print("%d." % i)
print("End Program !!!")