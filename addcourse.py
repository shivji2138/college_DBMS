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

# Function to add a course to the database
def add_course():
    # Get input values from the entry fields
    course_id = course_id_entry.get()
    course_name = course_name_entry.get()
    course_fees = course_fees_entry.get()
    duration_yr = duration_yr_entry.get()

    

    # SQL query to insert the course into the Courses table
    sql = "INSERT INTO Courses (course_id, course_name, course_fees, duration_yr) VALUES (%s, %s, %s, %s)"
    val = (course_id, course_name, course_fees, duration_yr)

    try:
        # Execute the SQL query
        mycursor.execute(sql, val)
        # Commit changes to the database
        mydb.commit()
        messagebox.showinfo("Success", "Course added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Create the main window
window = tk.Tk()
window.title("Add Course")
window.configure(bg='yellow')

# Labels
tk.Label(window, text="Course ID:", bg='yellow').grid(row=0, column=0)
tk.Label(window, text="Course Name:", bg='yellow').grid(row=1, column=0)
tk.Label(window, text="Course Fees:", bg='yellow').grid(row=2, column=0)
tk.Label(window, text="Duration (Years):", bg='yellow').grid(row=3, column=0)

# Entry fields
course_id_entry = tk.Entry(window)
course_id_entry.grid(row=0, column=1)
course_name_entry = tk.Entry(window)
course_name_entry.grid(row=1, column=1)
course_fees_entry = tk.Entry(window)
course_fees_entry.grid(row=2, column=1)
duration_yr_entry = tk.Entry(window)
duration_yr_entry.grid(row=3, column=1)

# Button to add course
add_button = tk.Button(window, text="Add Course", command=add_course, bg='green',fg='white')
add_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
