from tkinter import *
import customtkinter
from PIL import Image, ImageTk


app = customtkinter.CTk()
app.geometry("805x1000")
app.resizable(0,0)
app.title("Time Capsule Object Viewer")
''' my_image = customtkinter.CTkImage(light_image=Image.open("<path to light mode image>"),
                                  dark_image=Image.open("<path to dark mode image>"),
                                  size=(30, 30))
button = customtkinter.CTkButton(app, image=my_image) 
image_label = customtkinter.CTkLabel(app, image=my_image)
image_label.grid(row=0, column=0, padx=10, pady=10) '''
frame = Frame(app, width=805, height=400)
frame.pack()
bg = ImageTk.PhotoImage(Image.open("./TIME CAPSULE.png"))
label = Label(app,image=bg)
label.place(x=0, y=0, anchor='nw')

'''
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
'''
app.mainloop()