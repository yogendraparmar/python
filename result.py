print("===============This program is a for result chake================")
e= int(input("Enter english marks:"))
m= int(input("Enter maths marks:"))
p= int(input("Enter physics marks:"))
c= int(input("Enter chemistry marks:"))
o= int(input("Enter optional marks:"))
t= e+m+p+c+o
print("Total marks:",t)
p=(t)//5
print("This si your parcentage:",p)
if e>=33 and m>=33 and p>=33 and c>=33 and o>=33 :
    print("Your pass")
else:
    print("You are fail")

if p > 90:
    print("You got Grade 'A'" )
elif p>=80:
     print("You gotGrade 'B'")
elif p>=70:
    print("You got Grade 'C'")
elif p>=60:
    print("You got Grade 'D'")
else:
    print("You got Grade 'E'")
    
          

