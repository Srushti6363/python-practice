
import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")

conn.commit()


# 1. Add student
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        cursor.execute("""
        INSERT INTO students (id, name, age, course, marks)
        VALUES (?, ?, ?, ?, ?)
        """, (student_id, name, age, course, marks))

        conn.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Error: Student ID already exists.")

    except ValueError:
        print("Error: Enter valid numeric values.")


# 2. View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("No student records found.")
    else:
        print("\n--- STUDENT RECORDS ---")
        for student in records:
            print(student)


# 3. Search student
def search_student():
    student_id = int(input("Enter Student ID to search: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("Student Found:", student)
    else:
        print("Student not found.")


# 4. Update student
def update_student():
    student_id = int(input("Enter Student ID to update: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = float(input("Enter New Marks: "))

        cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, course = ?, marks = ?
        WHERE id = ?
        """, (name, age, course, marks, student_id))

        conn.commit()
        print("Student updated successfully!")
    else:
        print("Student not found.")


# 5. Delete student
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Main menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Try again.")

    except ValueError:
        print("Please enter a valid number.")

conn.close()
