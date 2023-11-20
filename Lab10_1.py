s = "suranaree"
n = 0 
print("Using break !!!")
while n < 20:
    print(n, end=" ")
    n += 1
    if n == 7:
        print(n)
        break
    
    
for i in s:
    if i == 'n':
        print(i)
        break
    else :
        print(i,end=' ')