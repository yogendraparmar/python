menu={
'Pizza':40,'Pasta':50, 'Burger':60,'Salad':70,'Coffee':90
     }
print("Welcome to my restorant")
print(" Pizza : Rs.40\n Pasta ; Rs.50\n Burger : Rs.60\n Salad :Rs.70\n Cofee:Rs.90")
order_total=0
 
item= input("Enter the name of item you wantto order=")
if item in menu:
    order_total += menu[item]
    print(f"Your item{item} has been added to your order")
else:
    print(f"Order item {item} is not available yet")
another_order = input("Do you want another order item?(Yes/No)")
if another_order =="Yes":
    item2= input("Enter the name of second item=")
    if item2 in menu:
         order_total +=menu[item2]
         print(f"Order item {item2} has added to order")
    else:
        print(f"Order iten {item2} is not avaialable")
print(f"The total amount of item is to pay=Rs.{order_total}")
    
    
