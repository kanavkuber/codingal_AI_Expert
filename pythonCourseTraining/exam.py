medical = input("Do you have a medical cause? (Yes/No): ").strip().upper()

if medical == 'Yes': 
    print("You are allowed")
else:
    attend = int(input("Enter the attendance of the student: "))
    if attend >= 75:
        print("You are allowed to take the Exam")
    else:
        print("You are not allowed to take the Exam")
