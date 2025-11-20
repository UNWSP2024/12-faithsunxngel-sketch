import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        mpg = miles / gallons
        messagebox.showinfo("MPG Result", f"MPG: {mpg:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("MPG Calculator")

tk.Label(root, text="Gallons of Gas:").grid(row=0, column=0, padx=10, pady=5)
gallons_entry = tk.Entry(root)
gallons_entry.grid(row=0, column=1)

tk.Label(root, text="Miles on Full Tank:").grid(row=1, column=0, padx=10, pady=5)
miles_entry = tk.Entry(root)
miles_entry.grid(row=1, column=1)

calc_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
