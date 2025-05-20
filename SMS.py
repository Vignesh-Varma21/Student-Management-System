# Student Management System in Python

students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    if roll_no in students:
        print("Student already exists.")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    students[roll_no] = {'name': name, 'age': age, 'grade': grade}
    print("Student added successfully.")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\n--- All Students ---")
    for roll_no, details in students.items():
        print(f"Roll No: {roll_no}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}")

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    student = students.get(roll_no)
    if student:
        print(f"Found Student - Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    else:
        print("Student not found.")

def update_student():
    roll_no = input("Enter Roll Number to update: ")
    if roll_no in students:
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        grade = input("Enter New Grade: ")
        students[roll_no] = {'name': name, 'age': age, 'grade': grade}
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
menu()
