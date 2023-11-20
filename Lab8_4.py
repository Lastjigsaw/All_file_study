timein = float(input("Time in: "))
timeout = float(input("Time out: "))
timeuse = timeout - timein

if timeuse <= 0.3:
    print("You parked in for %s hour (s) and %s minute (s)" % (int(timeuse * 10) / 10, int(timeuse * 60) % 60))
    print("You will not be charged !!!.")
    print("You will pay 0 baht")

elif timeuse <= 2:
    print("You parked in for %s hour (s) and %s minute (s)" % (int(timeuse * 10) / 10, int(timeuse * 60) % 60))
    print("You will be cahrge for the first 2 hours.")
    print("You will pay 40 baht")

elif timeuse <= 6:
    print("You parked in for %s hour (s) and %s minute (s)" % (int(timeuse * 10) / 10, int(timeuse * 60) % 60))
    print("You will be charge for %s hour (s)" % (int(timeuse * 10) / 10))
    print("You will pay %s baht" % (int(timeuse * 10) / 10 * 20))

elif timeuse == 6:
    print("You parked in for %s hour (s) and %s minute (s)" % (int(timeuse * 10) / 10, int(timeuse * 60) % 60))
    print("You will be charge for 6 hours.")
    print("You will pay 500 baht")

else:
    print("You parked in for %s hour (s) and %s minute (s)" % (int(timeuse * 10) / 10, int(timeuse * 60) % 60))
    print("You will be charge for the maximum rate.")
    print("You will pay 2000 baht")
