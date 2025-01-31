age= int(input("Enter Your age:"))
if age>100:
    print("Please enter correct age")
    exit()
if age<=13:
    print("You are child")
elif age>=13 and age<=19:
    print("You are teeage")
elif age>=20 and age<=59:
    print("You are adul")
else:
    print("You are senior")
    
