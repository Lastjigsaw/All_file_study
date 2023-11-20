print("Dec  Hex  Oct  Chr")
for n in range(65,91):
    print("%3d" %n,end='   ')
    print(hex(n)[2:4],end='  ')
    print(oct(n)[2:5],end='    ')
    print(chr(n))

