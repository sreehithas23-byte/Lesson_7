medical_cause=(input("Enter the medical cause? (Y/N): "))
if medical_cause == 'Y':
    print("You are eligible to write exams.")
else:
    attendance=int(input("Enter your attendance percentage: "))
    if attendance >= 75:
        print("You are eligible to write exams.")
    else:
        print("You are not eligible to write exams.")