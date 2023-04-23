import tkinter as tk 
from tkinter import *

# Create the main window
main = tk.Tk()
main.title("Relive the Past")

# Create the heading
heading = tk.Label(main, text="\nRelive the Past", bg='#ffbf00',font=("Helvetica", 24))
heading.pack()  




heading = tk.Label(main, text="\nPlease enter the name of the object", bg='#ffbf00',font=("Helvetica", 24))
heading.pack()
 

main.title("")
main.geometry('900x700')
main['bg'] = '#ffbf00'

def printValue():
    pname = player_name.get()
    Label(main, text=f'{pname}, Searching!', pady=20, bg='#ffbf00').pack()


player_name = Entry(main)
player_name.pack(pady=30)

Button(
    main,
    text="Relive The Past", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

# Run the GUI
main.mainloop()