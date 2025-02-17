
def calculate_compound_interest(principal, rate, time): 
    rate = rate / 100
    amount = principal * (1 + rate) ** time
    interest = amount - principal

    return interest, amount
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))
interest, total_amount = calculate_compound_interest(principal, rate, time)
print("\nResults:")
print(f"Compound Interest: {interest:.2f}")
print(f"Total Amount: {total_amount:.2f}")
