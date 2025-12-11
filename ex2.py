import email
import tkinter as tk    
from tkinter import messagebox

def submit():
    name = entry_name.get()
    email + entry_email.get()
    phone = entry_phone.get()
    position = entry_position.get()

    if name == "" or email == "" or phone == "" or position == "":
        messagebox.showwarning("แจ้งเตือน", "กรุณากรอกข้อมูลให้ครบ!")
    else:
        messagebox.showinfo("ผลการสมัคร" ,
                            f"ชื่อ: {name}\nอีเมล: {email}\nเบอร์โทร: {phone}\nตำแหน่งที่สมัคร: {position}")

root = tk.Tk()
root.title("ฟอร์มสมัครงาน")
root.geometry("350x320")

# Title
label_title = tk.Label(root, text="ฟอร์มสมัครงาน", font=("TH Sarabun New" , 20))
label_title.pack(pady=10)

label_title = tk.Label(root, text="ข้อมูลส่วนตัว", font=("TH Sarabun New" , 18))
label_title.pack(pady=12)

# Frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Name
tk.Label(frame, text="ชื่อ-สกุล").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, width=4)
entry_name.grid(row=0, column=1 , pady=5)

# age
tk.Label(frame, text="อายุ").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame, width=20)
entry_email.grid(row=1, column=1, pady=5)

# DMY
tk.Label(frame, text="วันเดือนปีเกิด(DD/MM/YYYY)").grid(row=2, column=0, sticky="w")
entry_phone = tk.Entry(frame, width=30)
entry_phone.grid(row=2, column=1, pady=5)

# Position
tk.Label(frame, text="ตำแหน่งที่สมัคร").grid(row=3, column=0, sticky="w")
entry_position = tk.Entry(frame, width=30)
entry_position.grid(row=3, column=1, pady=5)

# Button
submit_btn = tk.Button(root, text="ส่งใบสมัคร", command=submit)
submit_btn.pack(pady=20)

root.mainloop()
