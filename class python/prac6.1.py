#Online Shopping Cart: Imagine you’re developing an online shopping platform. Create a Python program that simulates a user’s shopping cart.
# •    Allow the user to add product names and prices to their cart.
# •    Display the current items in the cart.
# •    Allow the user to remove items from the cart.
# •    Calculate the total price and display the total number of items in the cart.
items={}
total=0
bill=""
cart=""
print("Welcome to the myntra!")
while True:
    print("1.Add items\n2.Display the cart\n3.Remove item from cart\n4.Total item in the cart\n-1.Exit")
    choice=int(input("Enter your choice :"))
    match choice:
        case 1:
            item_name=""
            item_name=input("Enter the item name : ")
            item_price=int(input("Enter the item Price :"))
            items[item_name]=item_price
            total+=item_price
            print("Item added successfully ..")
        case 2:
            print("*"*30)
            print("Your cart".center(30))
            print("*"*30)
            for key,value in items.items():
                 cart = cart+ f"{key:<20} {value:>10}"+"\n"
            print(cart) 
            print("*"*30)
            cart='' 
        case 3:
            print("*"*30)
            print("Your cart".center(30))
            print("*"*30)
            for key,value in items.items():
                 cart = cart+ f"{key:<20} {value:>10}"+"\n"
            print(cart) 
            print("*"*30)
            x=input("Enter the name of item :")
            total-=items[x]
            del items[x]
            print("Item removed successfully...") 
            cart=''          
        case 4:
            print("*"*30)
            print("BILL".center(30))
            print("*"*30)
            for key,value in items.items():
                 bill = bill+ f"{key:<20} {value:>10}"+"\n"
            print(bill)
            print(f"{'----------':<20} {'-----------':>10}")
            print(f"{'Total item':<20} {'Total price':>10}")
            print(f"{'----------':<20} {'-----------':>10}")
            print(f"{len(items):<20}{total:>10}")
            print("*"*30)
            print("Thanks for visiting".center(30))
            print("*"*30)
            bill=""

        case -1:
            break
        case _:
            print("--------------Enter the valid choice-----------")
            
