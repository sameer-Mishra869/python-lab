from student import Student
import csv

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")

def view_students():
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                s = Student(row[0], row[1], row[2])
                s.display()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")

