a = int(input("a = "))
b = int(input("b = "))
sum = a + b
sumstr = str(sum)
print("%d + %d = %d, and it is %s digit(s)" % (a,b,sum,len(sumstr)))