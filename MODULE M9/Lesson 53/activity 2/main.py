from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus Alert")
window.geometry("300x200")

def show_alert():
    messagebox.showwarning("Alert!", "Virus Detected on your system!")

label = Label(window, text="Security Check", font=("Arial", 14))
label.pack(pady=40)

btn = Button(window, text="Scan Now", command=show_alert, bg="red", fg="white")
btn.pack()

window.mainloop()
