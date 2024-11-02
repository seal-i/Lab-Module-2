# Author: Ian Seal
# File Name: student_qualifications.py
# Description: This app accepts a student's name and GPA, then checks if the student qualifies for the Dean's List or Honor Roll.
# The app will continue to process student records until 'ZZZ' is entered as the last name.

# Initialize lists to store students names and GPAs
student_names = []
student_gpas = []

# Collect student data
while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()
    if last_name.upper() == 'ZZZ':
        break
    
    first_name = input("Enter the student's first name: ").strip()
    
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Please enter a valid numeric GPA.")
        continue

    # Add student information to lists
    student_names.append((first_name, last_name))
    student_gpas.append(gpa)

# Process and print qualifications
for (first_name, last_name), gpa in zip(student_names, student_gpas):
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for any academic recognition.")
