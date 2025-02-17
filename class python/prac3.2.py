# You are building a student management system. Implement the following:
# ·        Create a dictionary called student_records where each key is a student ID (e.g., roll number) and the
#  student’s name, age, and grade value.
# ·        Allow the user to add new student records.
# ·        Display the details of a specific student given their ID.

print("------------Welcome to student management system----------")
student_records={}
while True:
    print("1.Add new student\n 2. Display specific student \n 3.Dispaly all the student \n4.exit")
    choice=int(input("Enter your choice:"))
    match choice:
        case 1:
            roll_no=input("Enter the roll no :")
            name=input("Enter the name of student:")
            age=float(input("Enter the age of student :"))
            grade=input("Enter the grade of student :")
            student_records[roll_no]={}
            student_records[roll_no]["Name"]=name
            student_records[roll_no]["Age"]=age
            student_records[roll_no]["Grade"]=grade
        case 2:
            id=input("Enter the roll no :")
            print("Details :-")
            for i in student_records.keys():
                if(id==i):
                    print(student_records[id])
                else:
                    print("---not found ---")
        case 3:
            print("Student Records :-")
            print(student_records)
        case 4:
            break
        case _:
            print("Enter the valid choice .....")
