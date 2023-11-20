location = "1234567890"
name = input(("NAME: "))
sex = input(("SEX (M/F): "))
num = int(input(("NUMBER (100 - 199): ")))
gpa = float(input(("GPA: "))) 
print(location*4)
print("%-15s%-9s%-13s%3s" % ("NAME","SEX","NUMBER","GPA"))
print("%-16s%-9s%5d%10.3f" % (name,sex,num,gpa))