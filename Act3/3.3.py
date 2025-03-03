
# input
last = input("Enter Last Name: ")
first = input("Enter First Name: ")
age = input("Enter Age: ")
contact = input("Enter Contact Number: ")
course = input("Enter Course: ")

# information
student_info = f"{last}, {first} | Age: {age} | Contact: {contact} | Course: {course}"

# Opening the file
with open("students.txt", "a") as file:
    file.write(student_info)
print("Student information has been saved to 'students.txt'.")
