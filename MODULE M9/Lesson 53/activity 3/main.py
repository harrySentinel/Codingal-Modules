from tkinter import *

window = Tk()
window.title("Main Window")
window.geometry("300x200")

def open_top():
    top = Toplevel()
    top.title("Top Window")
    top.geometry("250x150")
    Label(top, text="Welcome to the Top Window!", pady=20).pack()
    Button(top, text="Close", command=top.destroy).pack()

label = Label(window, text="Click to open a new window", pady=40)
label.pack()

btn = Button(window, text="Open Window", command=open_top, bg="blue", fg="white")
btn.pack()

window.mainloop()
