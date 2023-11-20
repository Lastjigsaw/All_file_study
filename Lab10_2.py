print("Using continue !!!")
s = "suranaree"

for n in range(1,20):
    if n % 3 == 0:
        print(n, end=" ")

print(" ")

for i in s:
    if i == 'a':
        continue
    else :
        print(i,end=' ')
