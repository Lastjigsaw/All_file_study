customer = int(input("How many customer?: "))
per = int(input("How much per head?: "))
toh = customer // 4 
total = (customer * per)- (toh * per) 
print("Total payment for %d customers is %d bath." % (customer,total)) #เหลือ add , 
