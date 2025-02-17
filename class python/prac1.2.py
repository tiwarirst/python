#Problem Statement: You are tasked with building an email automation system for a marketing campaign. 
#Your program must generate personalized email messages for customers based on their names and recent purchases.
# Develop a Python script that utilizes string operations to 
#construct dynamic email templates by inserting customer names and product details into predefined message formats.
def generate_email(name,item):
    print("""Dear {},\n\n
        Thank you for your recent purchase of {}. We hope you are enjoying it!\n
        As a valued customer, we would love to hear your feedback. Please feel free to reply to this email and let us know your thoughts.\n\n
        Best regards,\n
        The Marketing Team""".format(name,item))
name=input("Enter the customer name :")
items=input("Enter the purchased item :")
generate_email(name,items)