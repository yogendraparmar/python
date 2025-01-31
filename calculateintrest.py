print("===========Intrest calculator=============")

p = int(input("Enter principal amount:"))
i = int(input("Enter interst rate:"))
t = int(input("Enter time dureation years:"))
total = (p*i*t)//100
print("This is your intrest:",total)
print("This is your total Amount:",p+total)
