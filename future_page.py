import tkinter as tk 
from tkinter import *

# Create the main window
main = tk.Tk()








# Create the heading
heading = tk.Label(main, text="\nLets go into the future", bg='#ADD8E6',font=("Helvetica", 24))
heading.pack() 

heading = tk.Label(main, text="\nPlease enter the name of the object", bg='#ADD8E6',font=("Helvetica", 24))
heading.pack()
 

main.title("")
main.geometry('900x700')
main['bg'] = '#ADD8E6'

def printValue():
    pname = player_name.get()
    Label(main, text=f'{pname}, Searching!', pady=20, bg='#ADD8E6').pack()


player_name = Entry(main)
player_name.pack(pady=30)

Button(
    main,
    text="Lets go into the future", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

# Run the GUI
main.mainloop()