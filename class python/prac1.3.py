#You are a cashier at a grocery store. Customers come to your counter with different items. 
#Each item has a specific price (float). You must add up all the prices (float) to get the total bill (float). 
#Write a Python program to calculate the total bill.

x="--------------------- Rama Mart ----------------------------\n\n"
y="\n----------------- Thanks! for visiting -----------------------"
total=0
print("Enter 1 in item to print total.")
while 1!=0:
    item=input("Enter the item name :")
    if item=="1":
        break
    else:
        price=int(input("Enter the item price :"))
        total=total+price
        x = x + f"{item:<20} {price:>10}\n"
print(x)
print(f"{'------':<20} {'------':>10}")
print(f"{'Total':<20} {total:>10}\n", y)
