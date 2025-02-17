# Bookstore Inventory:  As a bookstore manager, you create a list of book titles and their corresponding 
# quantities in stock.
# •    Write a Python program that asks if the user is a manager or a normal user.
# •    Then allow the manager to create and update the list of books.
# •    Allow other users to search for a book title and check its availability.
# •    Prompt the user to enter a book title.
# •    If the book is in stock, display the quantity available; otherwise, show an appropriate message.
Book_store={}
while True:
    user=input("Enter the type of user (normal or manager or -1 to exit) : ")
    match user:
        case 'normal':
            search = input("Enter the book title: ").strip()
            if search in Book_store:
                if Book_store[search] == 0:
                    print("------Out of stock------")
                else:
                    print(f"Book is available: {search} - Quantity: {Book_store[search]}")
            else:
                print("------------Sorry! Book is not present in the store.---------")
        
        case "manager":
            password=input("Enter the password :")
            if password=="radmin":
                choice=int(input("Enter \n 1.To add new book \n 2.To update the quantity of book ."))
                match choice:
                    case 1:
                        while True:
                            title=input("Enter the book title (-1 to exit): ")
                            if title=='-1':
                                break
                            Quantity=int(input("Enter the quantity present : "))
                            Book_store[title]=Quantity
                    case 2:
                        print("Book in store : ",Book_store)
                        bname=input("Enter the book name want to update :")
                        if len(Book_store)==0:
                            print("-------Store is empty.----------") 
                            break
                        elif bname in Book_store:
                            uvalue=int(input("Enter the updated value :"))
                            Book_store[bname]=uvalue
                        else:
                            print("Book is not present in store.")
                    case _:
                        print("Invalid choice.")
            else:
                print("------------Incorrect password-------- \n ---------Try! Again----------")
        case "-1":
            break
        case _:
            print("----------------Enter the valid user.------------")