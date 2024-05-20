import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# Establishing the database connection
mydb = mysql.connector.connect(host='localhost',
                                         database='collage',
                                         user='root',
                                         password='shivusql')


def add_marks():
    roll_no = rollno_entry.get()
    student_id = student_id_entry.get()
    sem_1 = sem_1_entry.get()
    sem_2 = sem_2_entry.get()
    sem_3 = sem_3_entry.get()
    sem_4 = sem_4_entry.get()
    sem_5 = sem_5_entry.get()
    sem_6 = sem_6_entry.get()
    sem_7 = sem_7_entry.get()
    sem_8 = sem_8_entry.get()

    try:
        cursor = mydb.cursor()
        query = "INSERT INTO students_marks VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (student_id, sem_1, sem_2, sem_3, sem_4, sem_5, sem_6, sem_7, sem_8,roll_no)
        cursor.execute(query, data)
        mydb.commit()
        messagebox.showinfo("Success", "Data added successfully!")
    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")
    

# GUI
window = tk.Tk()
window.title("Add Data to Students Marks Table")
window.configure(bg='yellow')

tk.Label(window, text="Student ID:", bg='yellow').grid(row=0, column=0)
student_id_entry = tk.Entry(window)
student_id_entry.grid(row=0, column=1)

tk.Label(window, text="Semester 1:", bg='yellow').grid(row=1, column=0)
sem_1_entry = tk.Entry(window)
sem_1_entry.grid(row=1, column=1)

tk.Label(window, text="Semester 2:", bg='yellow').grid(row=2, column=0)
sem_2_entry = tk.Entry(window)
sem_2_entry.grid(row=2, column=1)

tk.Label(window, text="Semester 3:", bg='yellow').grid(row=3, column=0)
sem_3_entry = tk.Entry(window)
sem_3_entry.grid(row=3, column=1)

tk.Label(window, text="Semester 4:", bg='yellow').grid(row=4, column=0)
sem_4_entry = tk.Entry(window)
sem_4_entry.grid(row=4, column=1)

tk.Label(window, text="Semester 5:", bg='yellow').grid(row=5, column=0)
sem_5_entry = tk.Entry(window)
sem_5_entry.grid(row=5, column=1)

tk.Label(window, text="Semester 6:", bg='yellow').grid(row=6, column=0)
sem_6_entry = tk.Entry(window)
sem_6_entry.grid(row=6, column=1)

tk.Label(window, text="Semester 7:", bg='yellow').grid(row=7, column=0)
sem_7_entry = tk.Entry(window)
sem_7_entry.grid(row=7, column=1)

tk.Label(window, text="Semester 8:", bg='yellow').grid(row=8, column=0)
sem_8_entry = tk.Entry(window)
sem_8_entry.grid(row=8, column=1)

tk.Label(window, text='Roll_no:', bg='yellow').grid(row=9,column=0)
rollno_entry = tk.Entry(window)
rollno_entry.grid(row=9,column=1)

add_button = tk.Button(window, text="Add Data", command=add_marks, bg='green',fg='white')
add_button.grid(row=10, column=0, columnspan=2)

window.mainloop()

mydb.close()
    
