#You are building an e-commerce website, and you need to keep track of items in a user’s shopping cart. 
# Implement the following:
#·        Create an empty list called shopping_cart.
#·        Allow the user to add items (product names) to the cart.
#·        Display the current items in the cart.
#·        Allow the user to remove items from the cart.
#·        Calculate the total number of items in the cart.
item_list=[]
print("Welcome to the e-commerce website!")
while True:
    print("1.Add items\n2.Display the cart\n3.Remove item from cart\n4.Total item in the cart\n-1.Exit")
    choice=int(input("Enter your choice :"))
    match choice:
        case 1:
            item_name=""
            item_name=input("Enter the item name : ")
            item_list.append(item_name)
            print("Item added successfully ..")
        case 2:
            print("\nYour Cart :")
            print(item_list)   
        case 3:
            print("Your cart :",item_list)
            item_list.remove(input("Enter the name of item :"))
            print("Item removed successfully...")           
        case 4:
            print("Total item :", end="")
            print(len(item_list))
            
        case -1:
            break
        case _:
            print("--------------Enter the valid choice-----------")
            
