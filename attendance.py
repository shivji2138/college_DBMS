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

# Function to add attendance
def add_attendance():
    # Get input values from the entry fields
    student_id = student_id_entry.get()
    sem_1 = sem_1_entry.get()
    sem_2 = sem_2_entry.get()
    sem_3 = sem_3_entry.get()
    sem_4 = sem_4_entry.get()
    sem_5 = sem_5_entry.get()
    sem_6 = sem_6_entry.get()
    sem_7 = sem_7_entry.get()
    sem_8 = sem_8_entry.get()


    # SQL query to insert the attendance into the Attendance table
    sql = """UPDATE Attendance 
            SET sem_1 = %s, sem_2 = %s, sem_3 = %s, sem_4 = %s, 
            sem_5 = %s, sem_6 = %s, sem_7 = %s, sem_8 = %s
            WHERE student_id = %s"""
    val = (sem_1, sem_2, sem_3, sem_4, sem_5, sem_6, sem_7, sem_8, student_id)
    try:
        # Execute the SQL query
        mycursor.execute(sql, val)
        # Commit changes to the database
        mydb.commit()
        messagebox.showinfo("Success", "Attendance added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Create the main window
window = tk.Tk()
window.title("Add Attendance")
window.configure(bg='yellow')

# Labels
tk.Label(window, text="Student ID:", bg='yellow').grid(row=0, column=0)
tk.Label(window, text="Semester 1:", bg='yellow').grid(row=2, column=0)
tk.Label(window, text="Semester 2:", bg='yellow').grid(row=3, column=0)
tk.Label(window, text="Semester 3:", bg='yellow').grid(row=4, column=0)
tk.Label(window, text="Semester 4:", bg='yellow').grid(row=5, column=0)
tk.Label(window, text="Semester 5:", bg='yellow').grid(row=6, column=0)
tk.Label(window, text="Semester 6:", bg='yellow').grid(row=7, column=0)
tk.Label(window, text="Semester 7:", bg='yellow').grid(row=8, column=0)
tk.Label(window, text="Semester 8:", bg='yellow').grid(row=9, column=0)

# Entry fields
student_id_entry = tk.Entry(window)
student_id_entry.grid(row=0, column=1)
sem_1_entry = tk.Entry(window)
sem_1_entry.grid(row=2, column=1)
sem_2_entry = tk.Entry(window)
sem_2_entry.grid(row=3, column=1)
sem_3_entry = tk.Entry(window)
sem_3_entry.grid(row=4, column=1)
sem_4_entry = tk.Entry(window)
sem_4_entry.grid(row=5, column=1)
sem_5_entry = tk.Entry(window)
sem_5_entry.grid(row=6, column=1)
sem_6_entry = tk.Entry(window)
sem_6_entry.grid(row=7, column=1)
sem_7_entry = tk.Entry(window)
sem_7_entry.grid(row=8, column=1)
sem_8_entry = tk.Entry(window)
sem_8_entry.grid(row=9, column=1)

# Button to add attendance
add_button = tk.Button(window, text="Add Attendance", command=add_attendance, bg='green')
add_button.grid(row=10, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
