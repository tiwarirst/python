# CGPA Calculator
print("----------------CGPA Calculator-------------------------------")

# Input: Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize totals
total_marks = 0
total_credits = 0

# Loop through subjects to collect grades and credits
for i in range(num_subjects):
    grade_value = float(input(f"Enter the grade value for subject {i + 1}: "))
    credit = float(input(f"Enter the credit for subject {i + 1}: "))
    
    # Accumulate total marks and total credits
    total_marks += grade_value * credit
    total_credits += credit

# Calculate and display CGPA
if total_credits == 0:
    print("Total credits cannot be zero. Check your inputs.")
else:
    cgpa = total_marks / total_credits
    print(f"Your CGPA is: {cgpa:.2f}")
