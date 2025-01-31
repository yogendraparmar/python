year = int(input("Enter the year::"))
if (year%400==0)or(year % 4==0 and year % 100!=0):
    print(f"{year}:It is leap year")
else:
    print(f"{year}:it is not a leap year")
    
