#Following program creates a GUI for adding two numbers
import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("Result", f"Sum: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")

root = tk.Tk()
root.title("Addition of Two Numbers")
root.geometry("300x100")

tk.Label(root, text="Enter First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add_numbers).grid(row=2, column=0, columnspan=2)

root.mainloop()