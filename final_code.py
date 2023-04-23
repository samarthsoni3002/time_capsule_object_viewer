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

    im = ImageTk.PhotoImage(Image.open(""))

    label1 = Label(main,image=im)
    label1.image = im
    label1.pack()
 

    def back_to_home():
        main.destroy()
    

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
        text="Lets go into the future to save marty's kid from going to jail", 
        padx=10, 
        pady=5,
        command=printValue
        ).pack()
   
    Button(
        main,
        text="Go to the home page", 
        padx=15, 
        pady=5,
        command=back_to_home
        ).pack()
   

def past_window():
    main = Toplevel()
    main.geometry("1000x800")
    
    def back_to_home():
        main.destroy()
    
    heading = Label(main, text="\nRelive the past", bg='#ADD8E6',font=("Helvetica", 24))
    heading.pack() 

    heading = Label(main, text="\nPlease enter the name of the object", bg='#ADD8E6',font=("Helvetica", 24))
    heading.pack()
    

    main.title("")
    main.geometry('900x700')
    main['bg'] = '#ADD8E6'
 

    
    

    def printValue():
        pname = player_name.get()
        Label(main, text=f'{pname}, Searching!', pady=20, bg='#ADD8E6').pack()
        old_images(pname)

        no = randint(1,10)
        im = ImageTk.PhotoImage(Image.open(f"./{pname}_images/{pname}_{no}.jpg"))

        label1 = Label(main,image=im)
        label1.image = im
        label1.pack()

       


    player_name = Entry(main)
    player_name.pack(pady=30)

    Button(
        main,
        text="Let's time travel back in the past just like marty and doc ;)", 
        padx=10, 
        pady=5,
        command=printValue
        ).pack()

    Button(
        main,
        text="Go to the home page", 
        padx=15, 
        pady=5,
        command=back_to_home
        ).pack()
   

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



def exit_window():
    root.quit()


button1 = ttk.Button(master=my_canvas,
                 text="RELIVE THE PAST",command = lambda:past_window())
button1_window = my_canvas.create_window(0, 370, anchor="nw", window=button1, height=0, width=500)



button3 = ttk.Button(master=my_canvas,
                 text="DIVE INTO THE FUTURE",command  = lambda:future_window())
button3_window = my_canvas.create_window(500, 370, anchor="nw", window=button3, width=500)


button2 = ttk.Button(master=my_canvas,
                 text="Exit",command = lambda:exit_window())
button2_window = my_canvas.create_window(250, 740, anchor="nw", window=button2, height=0, width=500)

root.mainloop()