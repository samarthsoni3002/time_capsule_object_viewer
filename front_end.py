from tkinter import *
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1000X1000")
app.title("Time Capsule Object Viewer")

tabview = customtkinter.CTkTabview(app)
tabview.pack(padx=100, pady=100)

tabview.add("HOME")  
tabview.add("RELIVE THE PAST")  
tabview.add("DIVE INTO THE FUTURE") 
tabview.set("HOME")  



app.resizable(False,False)

img = Image.open('./bgimage3.jpg')
im = img.resize((1000,1000))


bg_image = ImageTk.PhotoImage(im)
bg = Canvas(app, width=1000, height=1000)
bg.pack(fill=BOTH, expand=YES)
bg.create_image(0,0,image=bg_image,anchor=NW)

app.mainloop()