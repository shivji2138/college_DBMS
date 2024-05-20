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

# Function to pay fees
def pay_fees():
    # Get input values from the entry fields
    student_id = student_id_entry.get()
    amount_paid = amount_paid_entry.get()



    # SQL query to update the paid fees and balance fees in the Fees_Status table
    try:
        # Retrieve current paid fees and total fees for the student and course
        sql_select = "SELECT total_fees, paid_fees FROM Fees_Status WHERE student_id = %s"
        mycursor.execute(sql_select, (student_id,))
        result = mycursor.fetchone()
        
        if not result:
            messagebox.showerror("Error", "No such record found")
            return

        total_fees, paid_fees = result
        total_fees = int(total_fees)
        paid_fees = int(paid_fees)
        
        # Calculate updated paid fees and balance fees
        amount_paid = int(amount_paid)
        new_paid_fees = paid_fees + amount_paid
        balance_fees = total_fees - new_paid_fees

        # Update the Fees_Status table
        sql_update = "UPDATE Fees_Status SET paid_fees = %s WHERE student_id = %s"
        val = (new_paid_fees, student_id)
        mycursor.execute(sql_update, val)
        mydb.commit()

        messagebox.showinfo("Success", f"Fees paid successfully. Balance:{balance_fees}")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Create the main window
window = tk.Tk()
window.title("Pay Fees")
window.configure(bg='yellow')

# Labels
tk.Label(window, text="Student ID:", bg='yellow').grid(row=0, column=0)
tk.Label(window, text="Amount Paid:", bg='yellow').grid(row=1, column=0)

# Entry fields
student_id_entry = tk.Entry(window)
student_id_entry.grid(row=0, column=1)
amount_paid_entry = tk.Entry(window)
amount_paid_entry.grid(row=1, column=1)

# Button to pay fees
pay_button = tk.Button(window, text="Pay Fees", command=pay_fees, bg='green',fg='white')
pay_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
