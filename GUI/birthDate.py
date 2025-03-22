import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    birth_date = entry.get()
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        messagebox.showinfo("Age", f"Your age is {age} years.")
    except ValueError:
        messagebox.showerror("Error", "Enter date in YYYY-MM-DD format.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x175")

tk.Label(root, text="Enter Birth Date (YYYY-MM-DD):").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=5)

root.mainloop()