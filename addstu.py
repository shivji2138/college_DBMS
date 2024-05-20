import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shivusql",
  database="collage"  # Make sure to use the correct database name
)

# Create a cursor object
mycursor = mydb.cursor()

# Function to add a student to the database
def add_student():
    # Get input values from the entry fields
    stuid = stuid_entry.get()
    name = name_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    department = department_entry.get()
    academic_year = academic_year_entry.get()
    courseid = courseid_entry.get()
    
    # SQL query to insert the student into the Students table
    sql = "INSERT INTO Students (student_id, stu_name, date_of_birth, phone_number, address, email, department, academic_year,course_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (stuid, name, dob, phone, address, email, department, academic_year,courseid)
    
    try:
        # Execute the SQL query
        mycursor.execute(sql, val)
        # Commit changes to the database
        mydb.commit()
        messagebox.showinfo("Success", "Student added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def add_attendance():
    stuid = stuid_entry.get()
    try:
        mycursor.execute('INSERT INTO attendance (student_id) VALUES (%s)',(stuid,))
        mydb.commit()
        messagebox.showinfo("Success", "Student added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def add_marks():
    stuid = stuid_entry.get()
    try:
        mycursor.execute('INSERT INTO students_marks (student_id) VALUES (%s)',(stuid,))
        mydb.commit()
        messagebox.showinfo("Success", "Student added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        
# Create the main window
window = tk.Tk()
window.title("Add Student")
window.configure(bg='yellow')

# Labels
tk.Label(window, text="Student ID:", bg='yellow').grid(row=0, column=0)
tk.Label(window, text="Name:", bg='yellow').grid(row=1, column=0)
tk.Label(window, text="Date of Birth:", bg='yellow').grid(row=2, column=0)
tk.Label(window, text="Phone Number:", bg='yellow').grid(row=3, column=0)
tk.Label(window, text="Address:", bg='yellow').grid(row=4, column=0)
tk.Label(window, text="Email:", bg='yellow').grid(row=5, column=0)
tk.Label(window, text="Department:", bg='yellow').grid(row=6, column=0)
tk.Label(window, text="Academic Year:", bg='yellow').grid(row=7, column=0)
tk.Label(window, text='Couse ID:', bg='yellow').grid(row=8, column=0)

# Entry fields
stuid_entry = tk.Entry(window)
stuid_entry.grid(row=0, column=1)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1)
dob_entry = tk.Entry(window)
dob_entry.grid(row=2, column=1)
phone_entry = tk.Entry(window)
phone_entry.grid(row=3, column=1)
address_entry = tk.Entry(window)
address_entry.grid(row=4, column=1)
email_entry = tk.Entry(window)
email_entry.grid(row=5, column=1)
department_entry = tk.Entry(window)
department_entry.grid(row=6, column=1)
academic_year_entry = tk.Entry(window)
academic_year_entry.grid(row=7, column=1)
courseid_entry = tk.Entry(window)
courseid_entry.grid(row=8,column=1)

# Button to add student
add_button = tk.Button(window, text="Add Student", command=add_student, bg='green',fg='white')
add_button.grid(row=9, column=0, columnspan=2, pady=10)

attendance_button = tk.Button(window, text='Create Attendance', command=add_attendance, bg='blue',fg='white')
attendance_button.grid(row=10, column=0, columnspan=2, pady=10)

marks_button = tk.Button(window, text='Create Marks', command=add_marks, bg='skyblue', fg='white')
marks_button.grid(row=11, column=0,columnspan=2, pady=10)

# Run the application
window.mainloop()
