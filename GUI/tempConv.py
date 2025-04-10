#to convert from Fahrenheit to Celsius and vice versa

import tkinter as tk
def fToC():
    try:
        fahrenheit = float(f_entry.get())
        celsius = (fahrenheit - 32) * 5/9 #conversion using teh formula
        c_entry.delete(0, tk.END)
        c_entry.insert(0, f"{celsius:.2f}")
    except ValueError:
        c_entry.delete(0, tk.END)
        c_entry.insert(0, "Invalid input") 

def cToF():
    try:
        celsius = float(c_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        f_entry.delete(0, tk.END)
        f_entry.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        f_entry.delete(0, tk.END)
        f_entry.insert(0, "Invalid input") #captures any inavlid input 

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x100")

tk.Label(root, text="Fahrenheit").grid(row=0, column=0)
tk.Label(root, text="Celsius").grid(row=0, column=1)

f_entry = tk.Entry(root)
f_entry.grid(row=1, column=0)
f_entry.insert(0, "32.0")

c_entry = tk.Entry(root)
c_entry.grid(row=1, column=1)
c_entry.insert(0, "0.0")

tk.Button(root, text=">>>>", command = fToC).grid(row = 2, column = 0)
tk.Button(root, text="<<<<", command = cToF).grid(row = 2, column = 1)

root.mainloop()