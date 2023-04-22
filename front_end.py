from tkinter import *
import customtkinter

app = customtkinter.CTk()
app.geometry("2000x2000")
app.title("Time Capsule Object Viewer")

tabview = customtkinter.CTkTabview(app)
tabview.pack(padx=100, pady=100)

tabview.add("HOME")  
tabview.add("RELIVE THE PAST")  
tabview.add("DIVE INTO THE FUTURE") 
tabview.set("HOME")  




app.mainloop()