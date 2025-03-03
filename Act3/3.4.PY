try:    
    with open("students.txt", "r") as file:
        content = file.read()
        
        # Check if the file is empty
        if content.strip():
            print("Student Information:\n", content)
        else:
            print("The file is empty.")
except FileNotFoundError:
    print("Error: students.txt file not found.")
