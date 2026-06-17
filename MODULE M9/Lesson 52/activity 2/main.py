from tkinter import *

window = Tk()
window.title("Tkinter Grid Layout")
window.geometry("300x200")

Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
Entry(window).grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=10)
Entry(window).grid(row=1, column=1, padx=10, pady=10)

Button(window, text="Submit", bg="green", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
