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

# Function to add fees status to the database
def add_fees_status():
    # Get input values from the entry fields
    student_id = student_id_entry.get()
    stu_name = stu_name_entry.get()
    course_id = course_id_entry.get()
    total_fees = total_fees_entry.get()
    paid_fees = paid_fees_entry.get()
    
    # Calculate balance fees
    try:
        total_fees = int(total_fees)
        paid_fees = int(paid_fees)
        balance_fees = total_fees - paid_fees
    except ValueError:
        messagebox.showerror("Error", "Invalid fees amount")
        return

    # SQL query to insert the fees status into the Fees_Status table
    sql = "INSERT INTO Fees_Status (student_id, stu_name, course_id, total_fees, paid_fees) VALUES (%s, %s, %s, %s, %s)"
    val = (student_id, stu_name, course_id, total_fees, paid_fees)

    try:
        # Execute the SQL query
        mycursor.execute(sql, val)
        # Commit changes to the database
        mydb.commit()
        messagebox.showinfo("Success", f"Fees status added successfully, Balance:{balance_fees,}")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Create the main window
window = tk.Tk()
window.title("Add Fees Status")
window.configure(bg='yellow')

# Labels
tk.Label(window, text="Student ID:", bg='yellow').grid(row=0, column=0)
tk.Label(window, text="Student Name:", bg='yellow').grid(row=1, column=0)
tk.Label(window, text="Course ID:", bg='yellow').grid(row=2, column=0)
tk.Label(window, text="Total Fees:", bg='yellow').grid(row=3, column=0)
tk.Label(window, text="Paid Fees:", bg='yellow').grid(row=4, column=0)

# Entry fields
student_id_entry = tk.Entry(window)
student_id_entry.grid(row=0, column=1)
stu_name_entry = tk.Entry(window)
stu_name_entry.grid(row=1, column=1)
course_id_entry = tk.Entry(window)
course_id_entry.grid(row=2, column=1)
total_fees_entry = tk.Entry(window)
total_fees_entry.grid(row=3, column=1)
paid_fees_entry = tk.Entry(window)
paid_fees_entry.grid(row=4, column=1)

# Button to add fees status
add_button = tk.Button(window, text="Add Fees Status", command=add_fees_status, bg='green',fg='white')
add_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
