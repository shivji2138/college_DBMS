import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# Establishing the database connection
connection = mysql.connector.connect(host='localhost',
                                         database='collage',
                                         user='root',
                                         password='shivusql')

def add_course():
    course_id = course_id_entry.get()
    course_name = course_name_entry.get()
    course_fees = course_fees_entry.get()
    duration_yr = duration_yr_entry.get()

    try:
        cursor = connection.cursor()
        query = "INSERT INTO Courses (course_id, course_name, course_fees, duration_yr) VALUES (%s, %s, %s, %s)"
        data = (course_id, course_name, course_fees, duration_yr)
        cursor.execute(query, data)
        connection.commit()
        messagebox.showinfo("Success", "Course added successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")
    

# GUI
window = tk.Tk()
window.title("Add Course")
window.configure(background='yellow')

tk.Label(window, text="Course ID:", background='yellow').grid(row=0, column=0)
course_id_entry = tk.Entry(window)
course_id_entry.grid(row=0, column=1)

tk.Label(window, text="Course Name:", background='yellow').grid(row=1, column=0)
course_name_entry = tk.Entry(window)
course_name_entry.grid(row=1, column=1)

tk.Label(window, text="Course Fees:", background='yellow').grid(row=2, column=0)
course_fees_entry = tk.Entry(window)
course_fees_entry.grid(row=2, column=1)

tk.Label(window, text="Duration (years):", background='yellow').grid(row=3, column=0)
duration_yr_entry = tk.Entry(window)
duration_yr_entry.grid(row=3, column=1)

add_button = tk.Button(window, text="Add Course", command=add_course, background='green',fg='white')
add_button.grid(row=4, column=0, columnspan=2)

window.mainloop()

connection.close()

