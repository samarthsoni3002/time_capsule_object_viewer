from tkinter import *
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1000X1000")
app.title("Time Capsule Object Viewer")


def button_event():
    print("button pressed")

button1 = customtkinter.CTkButton(master=app,  
                                 width=400,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
                                 text="HOME",
                                 command=button_event) 
button1.grid(row=0, column=0, padx=10, pady=350)
button2 = customtkinter.CTkButton(master=app,  
                                 width=400,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
                                 text="RELIVE THE PAST",
                                 command=button_event) 

button2.grid(row=0, column=1, padx=20, pady=350)
button3 = customtkinter.CTkButton(master=app,  
                                 width=400,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
                                 text="DIVE INTO THE FUTURE",
                                 command=button_event) 

button3.grid(row=0, column=2, padx=20, pady=350)

app.mainloop()