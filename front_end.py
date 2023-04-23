from tkinter import *
import customtkinter
from PIL import ImageTk, Image



app = customtkinter.CTk()
app.geometry("1000X1000")
app.title("Time Capsule Object Viewer")



frame = Frame(app,width=600,height=400)
frame.pack()
frame.place(anchor='center',relx=0.5,rely=0.5)

bg = ImageTk.PhotoImage(Image.open("./TIME CAPSULE.jpg"))
label = Label(frame,image=bg)
label.pack()

app.mainloop()