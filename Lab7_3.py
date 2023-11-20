# bi = str(input("Enter a 8-Bit binary number: ")) #ใช้หลักการเหมือน add


binary_input = input("Enter a 8-bit binary number: ")
binarytostr = str(binary_input)
binary1 = binarytostr[-1:-4:-1]
binary2 = binarytostr[-4:-7:-1]
binary3 = binarytostr[-7:-9:-1]
print(binary_input, "=",binary3,binary2,binary1)

