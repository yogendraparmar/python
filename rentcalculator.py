#Total Rent of flat
#Totall Elictricty unit
#Total Amounr of food
# Toatal amount per unit of electricty
# Total candidate living in flat
print("============This is a rent calcualtor program=====================")
rent = int(input("Enter Flat rent :"))
elct = int(input("Enter total unit of electricty:"))
unit = int(input("Enter Rate of light unit:"))
food= int(input("Enter total amount of food:"))
candidate= int(input("Enter total candidate in flat:"))
light = elct*unit
Total= (rent+food+light)//candidate
print("This is your total Amount",rent+food+light)
print("This is rent per condidate:",Total)
