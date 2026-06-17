from tkinter import *

window = Tk()
window.title("Aditya's First Window")
window.geometry("300x300")

label = Label(window, text="Hello! I am Aditya Srivastava", fg="black", bg="white")
button = Button(window, text="Click Me", bg="black", fg="white")
entry = Entry(window, fg="yellow", bg="blue", width=30)

label.pack()
button.pack()
entry.pack()

window.mainloop()
