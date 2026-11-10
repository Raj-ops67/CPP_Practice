# Student Record Management with List, Tuple, Dictionary and CSV

import csv

students = [
    {"RollNo": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
    {"RollNo": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
    {"RollNo": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78}
]

# Tuple example: fixed course details
course = ("Python", 4)
print("Course Tuple:", course)

# Write text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

# Write CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read CSV file
print("\n--- Records from CSV ---")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            row["RollNo"],
            row["Name"],
            row["Department"],
            row["Mark"]
        )