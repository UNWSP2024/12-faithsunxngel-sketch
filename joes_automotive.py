import tkinter as tk

def calculate_total():
    total = 0
    if oil_var.get(): total += 30
    if lube_var.get(): total += 20
    if rad_var.get(): total += 40
    if trans_var.get(): total += 100
    if insp_var.get(): total += 35
    if muff_var.get(): total += 200
    if tire_var.get(): total += 20

    total_label.config(text=f"Total: ${total:.2f}")

root = tk.Tk()
root.title("Joe's Automotive")

# BooleanVars for checkboxes
oil_var = tk.BooleanVar()
lube_var = tk.BooleanVar()
rad_var = tk.BooleanVar()
trans_var = tk.BooleanVar()
insp_var = tk.BooleanVar()
muff_var = tk.BooleanVar()
tire_var = tk.BooleanVar()

tk.Checkbutton(root, text="Oil Change - $30", variable=oil_var).pack(anchor="w")
tk.Checkbutton(root, text="Lube Job - $20", variable=lube_var).pack(anchor="w")
tk.Checkbutton(root, text="Radiator Flush - $40", variable=rad_var).pack(anchor="w")
tk.Checkbutton(root, text="Transmission Fluid - $100", variable=trans_var).pack(anchor="w")
tk.Checkbutton(root, text="Inspection - $35", variable=insp_var).pack(anchor="w")
tk.Checkbutton(root, text="Muffler Replacement - $200", variable=muff_var).pack(anchor="w")
tk.Checkbutton(root, text="Tire Rotation - $20", variable=tire_var).pack(anchor="w")

tk.Button(root, text="Calculate Total", command=calculate_total).pack(pady=10)

total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14))
total_label.pack()

root.mainloop()
