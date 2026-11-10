# Menu-Driven Student Information System

students = {}


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")

    students[roll] = {
        "Name": name,
        "Department": dept
    }

    print("Student added successfully.")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for roll, data in students.items():
        print("Roll No:", roll,
              "| Name:", data["Name"],
              "| Department:", data["Department"])


def search_student():
    roll = input("Enter Roll No to search: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter Roll No to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")