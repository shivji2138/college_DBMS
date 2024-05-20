import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

def search_student():
    student_id = int(student_id_entry.get())
    student_info = get_student_info(student_id)
    if student_info != "Student not found.":
        display_student_info(student_info)
    else:
        messagebox.showinfo("Student Not Found", "Student with the provided ID not found.")

def get_student_info(student_id):
    try:
        # Establishing the database connection
        mydb = mysql.connector.connect(host='localhost',
                                        database='collage',
                                        user='root',
                                        password='shivusql')

        if mydb.is_connected():
            # Creating a cursor object
            cursor = mydb.cursor()

            # Query to retrieve student information by joining tables
            query = """
            SELECT s.student_id, s.stu_name, s.date_of_birth, s.phone_number, s.address, s.email, 
                   s.department, s.academic_year, fs.total_fees, fs.paid_fees, fs.balance_fees, 
                   a.sem_1, a.sem_2, a.sem_3, a.sem_4, a.sem_5, a.sem_6, a.sem_7, a.sem_8, 
                   m.sem_1 AS marks_sem_1, m.sem_2 AS marks_sem_2, m.sem_3 AS marks_sem_3, 
                   m.sem_4 AS marks_sem_4, m.sem_5 AS marks_sem_5, m.sem_6 AS marks_sem_6, 
                   m.sem_7 AS marks_sem_7, m.sem_8 AS marks_sem_8
            FROM Students s
            LEFT JOIN Fees_Status fs ON s.student_id = fs.student_id
            LEFT JOIN Attendance a ON s.student_id = a.student_id
            LEFT JOIN Students_Marks m ON s.student_id = m.student_id
            WHERE s.student_id = %s
            """
            # Executing the query
            cursor.execute(query, (student_id,))

            # Fetching the results
            student_data = cursor.fetchone()

            if student_data:
                return student_data
            else:
                return "Student not found."

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # Closing database connection
        if mydb and mydb.is_connected():
            cursor.close()
            mydb.close()

def display_student_info(student_info):
    student_window = tk.Toplevel(window)
    student_window.title("Student Information")
    student_window.configure(bg='yellow')

    labels = ["Student ID", "Name", "Date of Birth", "Phone Number", "Address", "Email", "Department", "Academic Year",
              "Total Fees", "Paid Fees", "Balance Fees", "Semester 1", "Semester 2", "Semester 3", "Semester 4",
              "Semester 5", "Semester 6", "Semester 7", "Semester 8", "Marks Semester 1", "Marks Semester 2",
              "Marks Semester 3", "Marks Semester 4", "Marks Semester 5", "Marks Semester 6", "Marks Semester 7",
              "Marks Semester 8"]

    for i in range(len(labels)):
        label = tk.Label(student_window, text=labels[i] + ": " + str(student_info[i]), bg='yellow')
        label.pack()

# GUI
window = tk.Tk()
window.title("Search Student")
window.configure(bg='yellow')

tk.Label(window, text="Enter Student ID:", bg='yellow').pack()
student_id_entry = tk.Entry(window)
student_id_entry.pack()

search_button = tk.Button(window, text="Search", command=search_student, bg='blue', fg='white')
search_button.pack()

window.mainloop()
