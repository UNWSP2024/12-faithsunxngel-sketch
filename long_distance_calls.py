import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    try:
        minutes = float(minutes_entry.get())
        rate = rate_var.get()

        if rate == 1:
            charge = minutes * 0.02   # Daytime
        elif rate == 2:
            charge = minutes * 0.12   # Evening
        else:
            charge = minutes * 0.05   # Off-peak

        messagebox.showinfo("Call Charge", f"Total Charge: ${charge:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")

root = tk.Tk()
root.title("Long-Distance call calculator")

rate_var = tk.IntVar()
rate_var.set(1)

tk.Label(root, text="Select Rate Category:").pack()

tk.Radiobutton(root, text="Daytime (0.02/min)", variable=rate_var, value=1).pack(anchor="w")
tk.Radiobutton(root, text="Evening (0.12/min)", variable=rate_var, value=2).pack(anchor="w")
tk.Radiobutton(root, text="Off-Peak (0.05/min)", variable=rate_var, value=3).pack(anchor="w")

tk.Label(root, text="Minutes:").pack(pady=5)
minutes_entry = tk.Entry(root)
minutes_entry.pack()

tk.Button(root, text="Calculate Charge", command=calculate_charge).pack(pady=10)

root.mainloop()
