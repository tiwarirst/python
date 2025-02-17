#Problem statement:  You are working in a
#loan approval section of a bank; you need to create a Python script for 
#"printing loan approval or not" from the following criteria. (AGE SHOULD BE GREATER THAN 18,
#SALARY SHOULD BE NO LESS THAN 4 LAKHS, AND CREDIT SCORE SHOULD BE NO LESS THAN 600).
i=float(input("Enter your age:"))
j=float(input("Enter your salary :"))
k=float(input("Enter the credit score :"))
if i>18 and j>400000 and k>=600:
    {
        print("Congratulation !You are eligible for loan.")
    }
else:
    {
        print("Sorry ! You are not eligible for loan")
    }
