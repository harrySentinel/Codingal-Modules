from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Image in Tkinter")
window.geometry("400x400")

img = Image.open("photo.jpg")
img = img.resize((300, 250))
photo = ImageTk.PhotoImage(img)

label = Label(window, image=photo)
label.pack(pady=20)

caption = Label(window, text="Aditya Srivastava - Codingal Instructor", fg="blue")
caption.pack()

window.mainloop()
