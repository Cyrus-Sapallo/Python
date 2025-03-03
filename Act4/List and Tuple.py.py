import os

# List to store student records
student_records = []

def open_file():
    filename = input("Enter filename to open: ")

    if not os.path.exists(filename):
        print("File not found.")
        return

    with open(filename, "r") as file:
        student_records.clear()  # Clear current list before loading
        for line in file:
            data = line.strip().split(",")
            if len(data) == 5:
                student_id, first_name, last_name, class_standing, major_exam = data
                student_records.append((student_id, (first_name, last_name), float(class_standing), float(major_exam)))

    print(f"Records loaded from '{filename}'.")

def save_file():
    if not student_records:
        print("No records to save.")
        return

    with open("student_records.txt", "w") as file:
        for record in student_records:
            file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")

    print("Records saved to 'student_records.txt'.")

def save_as_file():
    if not student_records:
        print("No records to save.")
        return

    filename = input("Save as (enter filename): ")
    
    if not filename.endswith(".txt"):
        filename += ".txt"

    with open(filename, "w") as file:
        for record in student_records:
            file.write(f"{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n")

    print(f"Records saved to '{filename}'.")

def show_all():
    if student_records:
        while True:
            print("\nChoose sorting option:")
            print("1: Order by Last Name")
            print("2: Order by Grade")
            print("3: Return to Menu")
            
            sort_choice = input("Enter your choice: ")

            if sort_choice == "1":
                order_by_last_name()
            elif sort_choice == "2":
                order_by_grade()
            elif sort_choice == "3":
                return
            else:
                print("Invalid choice. Please try again.")

    else:
        print("No student records found.")

def order_by_last_name():
    if student_records:
        sorted_records = sorted(student_records, key=lambda x: x[1][1].lower())  # Sort by last name (case-insensitive)
        print("\nRecords Ordered by Last Name:")
        for record in sorted_records:
            print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Class Standing: {record[2]}, Major Exam: {record[3]}")
    else:
        print("No student records found.")

def order_by_grade():
    if student_records:
        sorted_records = sorted(student_records, key=lambda x: (x[2] * 0.6) + (x[3] * 0.4), reverse=True)
        print("\nRecords Ordered by Grade:")
        for record in sorted_records:
            final_grade = (record[2] * 0.6) + (record[3] * 0.4)
            print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Class Standing: {record[2]}, Major Exam: {record[3]}, Final Grade: {final_grade:.2f}")
    else:
        print("No student records found.")

def show():
    student_id = input("Enter Student ID to search: ")
    for record in student_records:
        if record[0] == student_id:
            print("\nRecord found:")
            print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Class Standing: {record[2]}, Major Exam: {record[3]}")
            return
    print("Record not found.")

def add():
    while True:
        student_id = input("Enter Student ID (6 digits): ")
        if len(student_id) == 6 and student_id.isdigit():
            break
        print("Invalid Student ID. It must be a 6-digit number.")

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    
    while True:
        try:
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            break
        except ValueError:
            print("Invalid input. Please enter numerical values for grades.")

    record = (student_id, (first_name, last_name), class_standing, major_exam)  # Store as a tuple
    student_records.append(record)  # Add to list
    print("Record added successfully.")

def edit():
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(student_records):
        if record[0] == student_id:
            first_name = input("Enter new First Name: ")
            last_name = input("Enter new Last Name: ")
            while True:
                try:
                    class_standing = float(input("Enter new Class Standing Grade: "))
                    major_exam = float(input("Enter new Major Exam Grade: "))
                    break
                except ValueError:
                    print("Invalid input. Grades must be numerical.")

            student_records[i] = (student_id, (first_name, last_name), class_standing, major_exam)  # Replace tuple
            print("Record updated successfully.")
            return
    print("Record not found.")

def delete():
    student_id = input("Enter Student ID to delete: ")
    for record in student_records:
        if record[0] == student_id:
            confirm = input(f"Are you sure you want to delete {record[1][0]} {record[1][1]}? (yes/no): ").strip().lower()
            if confirm == "yes":
                student_records.remove(record)
                print("Record deleted successfully.")
            else:
                print("Deletion canceled.")
            return
    print("Record not found.")

# Menu options stored in a dictionary
menu = {
    "1": open_file,
    "2": save_file,
    "3": save_as_file,
    "4": show_all,
    "5": show,
    "6": add,
    "7": edit,
    "8": delete,
}

while True:
    print("\nMenu:")
    print("1: Open file         6: Add Record")
    print("2: Save file         7: Edit Record")
    print("3: Save as file      8: Delete Record")
    print("4: Show all records  0: Exit")
    print("5: Search by Student ID")  # Fixed label

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting program...")
        break
    elif choice in menu:
        menu[choice]()  # Calls the corresponding function
    else:
        print("Invalid choice. Please try again.")
