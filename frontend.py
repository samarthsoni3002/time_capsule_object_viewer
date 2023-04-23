from tkinter import *
from tkinter import ttk

root = Tk()
root.title("TIME CAPSULE OBJECT VIEWER")
root.geometry("1000x800")

bg = PhotoImage(file="./TIME CAPSULE.png")
bg2 = PhotoImage(file="./time.png")
my_canvas = Canvas(root)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas.create_image(0, 400, image=bg2, anchor="nw")

style = ttk.Style()

style.configure("TButton",
                font=("Georgia", 22),
                padding=10,
                relief="flat",
                background="#4ca7b3",
                foreground="#367077")

button1 = ttk.Button(master=my_canvas,
                 text="RELIVE THE PAST")
button1_window = my_canvas.create_window(0, 370, anchor="nw", window=button1, height=0, width=500)

button3 = ttk.Button(master=my_canvas,
                 text="DIVE INTO THE FUTURE")
button3_window = my_canvas.create_window(500, 370, anchor="nw", window=button3, width=500)

root.mainloop()
