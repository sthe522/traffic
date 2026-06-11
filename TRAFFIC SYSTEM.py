import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Traffic System")


cars_db = [] 

def update_geometry():
    app.update_idletasks()
    w, h = 380, 520
    x = (app.winfo_screenwidth() - w) // 2
    y = (app.winfo_screenheight() - h) // 2
    app.geometry(f"{w}x{h}+{x}+{y}")
    app.resizable(False, False)


header = tk.Frame(app, bg="steelblue", height=50)
header.pack(fill="x", side="top")
header.pack_propagate(False)
tk.Label(header, text="TRAFFIC SYSTEM", bg="steelblue", fg="white",
         font=("Arial", 16, "bold")).pack(pady=12)

form = tk.Frame(app, padx=15, pady=10)
form.pack(fill="both", expand=True)


tk.Label(form, text="Car Registration:").grid(row=0, column=0, sticky="w", pady=3)
car = tk.Entry(form, width=30)
car.grid(row=0, column=1, pady=3)

tk.Label(form, text="Owner Name:").grid(row=1, column=0, sticky="w", pady=3)
owner = tk.Entry(form, width=30)
owner.grid(row=1, column=1, pady=3)


tk.Label(form, text="Phone Number:").grid(row=2, column=0, sticky="w", pady=3)
phone = tk.Entry(form, width=30)
phone.grid(row=2, column=1, pady=3)


tk.Label(form, text="License No:").grid(row=3, column=0, sticky="w", pady=3)
license_no = tk.Entry(form, width=30)
license_no.grid(row=3, column=1, pady=3)


tk.Label(form, text="Disk Expiry Date:").grid(row=4, column=0, sticky="w", pady=3)
expiry = tk.Entry(form, width=30)
expiry.insert(0, "YYYY-MM-DD")
expiry.grid(row=4, column=1, pady=3)


tk.Label(form, text="Vehicle Type:").grid(row=5, column=0, sticky="w", pady=3)
vehicle_type = tk.StringVar(value="Car")
tk.OptionMenu(form, vehicle_type, "Car", "Taxi", "Truck", "Bus", "Motorcycle").grid(row=5, column=1, sticky="w", pady=3)


status = tk.Label(app, text="Status: Waiting...", fg="blue", font=("Arial", 10, "bold"))
status.pack(pady=5)


list_frame = tk.Frame(app)
list_frame.pack(fill="both", expand=True, padx=15, pady=5)

tk.Label(list_frame, text="Registered Cars:", font=("Arial", 11, "bold")).pack(anchor="w")
listbox = tk.Listbox(list_frame, height=6)
listbox.pack(fill="both", expand=True)

def register():
    if car.get() == "" or owner.get() == "" or phone.get() == "":
        status.config(text="Status: Fill all required fields ", fg="red")
        return

    car_data = {
        "reg": car.get(),
        "owner": owner.get(),
        "phone": phone.get(),
        "license": license_no.get(),
        "expiry": expiry.get(),
        "type": vehicle_type.get()
    }
    cars_db.append(car_data)

    display = f"{car_data['reg']} | {car_data['owner']} | {car_data['type']}"
    listbox.insert(tk.END, display)

    status.config(text="Status: Car Registered ", fg="green")
    messagebox.showinfo("Success", f"Car {car.get()} registered successfully!")

def renew_disk():
    if car.get() == "":
        status.config(text="Status: Enter car reg ", fg="red")
    else:
        status.config(text=f"Status: Disk for {car.get()} Renewed ", fg="green")

def renew_plate():
    if car.get() == "":
        status.config(text="Status: Enter car reg ", fg="red")
    else:
        status.config(text=f"Status: Plate for {car.get()} Renewed ", fg="green")

def clear():
    car.delete(0, tk.END)
    owner.delete(0, tk.END)
    phone.delete(0, tk.END)
    license_no.delete(0, tk.END)
    expiry.delete(0, tk.END)
    expiry.insert(0, "YYYY-MM-DD")
    status.config(text="Status: Cleared", fg="blue")

def delete_car():
    sel = listbox.curselection()
    if sel:
        listbox.delete(sel[0])
        cars_db.pop(sel[0])
        status.config(text="Status: Car Deleted", fg="orange")


btn_frame = tk.Frame(app, pady=10)
btn_frame.pack()

tk.Button(btn_frame, text="Register Car", command=register,
          bg="green", fg="white", width=12).grid(row=0, column=0, padx=3)
tk.Button(btn_frame, text="Renew Disk", command=renew_disk,
          bg="blue", fg="white", width=12).grid(row=0, column=1, padx=3)
tk.Button(btn_frame, text="Renew Plate", command=renew_plate,
          bg="purple", fg="white", width=12).grid(row=1, column=0, padx=3, pady=3)
tk.Button(btn_frame, text="Delete", command=delete_car,
          bg="orange", fg="white", width=12).grid(row=1, column=1, padx=3, pady=3)
tk.Button(btn_frame, text="Clear", command=clear,
          bg="red", fg="white", width=12).grid(row=0, column=2, padx=3, rowspan=2)


update_geometry()
app.mainloop()

