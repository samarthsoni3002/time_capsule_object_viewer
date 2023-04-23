from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from backend_new import *
from random import *


def future_window():
    main = Toplevel()
    main.geometry("1000x800")
    
    
    heading = Label(main, text="\nLets go into the future", bg='#ADD8E6',font=("Helvetica", 24))
    heading.pack() 

    heading = Label(main, text="\nPlease enter the name of the object", bg='#ADD8E6',font=("Helvetica", 24))
    heading.pack()
    

    main.title("")
    main.geometry('900x700')
    main['bg'] = '#ADD8E6'

    def printValue():
        pname = player_name.get()
        Label(main, text=f'{pname}, Searching!', pady=20, bg='#ADD8E6').pack()
        futuristic_images(pname)
        
        no = randint(1,10)
        im = ImageTk.PhotoImage(Image.open(f"./{pname}_images/{pname}_{no}.jpg"))

        label1 = Label(main,image=im)
        label1.image = im
        label1.pack()

       



    player_name = Entry(main)
    player_name.pack(pady=30)

    Button(
        main,
        text="Lets go into the future", 
        padx=10, 
        pady=5,
        command=printValue
        ).pack()
   

def past_window():
    main = Toplevel()
    canvas = Canvas(main, height=800, width=1000)
    heading = Label(main, text="\nRelive the Past", bg='#ffbf00',font=("Helvetica", 24))
    heading.pack()  




    heading = Label(main, text="\nPlease enter the name of the object", bg='#ffbf00',font=("Helvetica", 24))
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

    canvas.pack()


root = Tk()
root.title("TIME CAPSULE OBJECT VIEWER")
root.geometry("1000x800")

bg = ImageTk.PhotoImage(Image.open("./TIME CAPSULE.jpg"))
bg2 = ImageTk.PhotoImage(Image.open("./time.png"))
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
                 text="RELIVE THE PAST",command = lambda:past_window())
button1_window = my_canvas.create_window(0, 370, anchor="nw", window=button1, height=0, width=500)

button3 = ttk.Button(master=my_canvas,
                 text="DIVE INTO THE FUTURE",command  = lambda:future_window())
button3_window = my_canvas.create_window(500, 370, anchor="nw", window=button3, width=500)

root.mainloop()