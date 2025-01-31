even_no = int(input("Enter range of numbers"))
even_total=0
for i in range(1, even_no+1):
    if i%2==0:
        even_total= even_total+1
print("Even numbers is count;",even_total)
