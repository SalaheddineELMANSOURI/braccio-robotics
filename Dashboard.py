from tkinter import *
from PIL import ImageTk
from datetime import *
import time
import keyboard

class Dashboard2:
    def __init__(self, window):
        self.window = window
        self.increment = 0
        self.window.title("Robot Pick and Place")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        icon = PhotoImage(file='images\\pic-icon.png')
        self.window.iconphoto(True, icon)

        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=110, width=310, height=220)

        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=680, y=110, width=310, height=220)

        self.logoImage = ImageTk.PhotoImage(file='images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        self.brandName = Label(self.sidebar, text='My Robot', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=95, y=200)

        self.ExitImage = ImageTk.PhotoImage(file='images/exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        self.Exit.place(x=35, y=273)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=window.destroy)
        self.Exit_text.place(x=80, y=287)

        # self.total_people = Label(self.bodyFrame2, text='230', bg='#009aa5', font=("", 25, "bold"))
        # self.total_people.place(x=120, y=100)

        self.horloge = Label(self.bodyFrame2, bg='#009aa5')
        self.horloge.place(x=220, y=0)

        self.horloge_label = Label(self.bodyFrame2, text="Time", bg='#009aa5', font=("", 12, "bold"),
                                       fg='white')
        self.horloge_label.place(x=45, y=25)

        self.compteur = Label(self.bodyFrame3, text=f"{self.increment}" , bg='#e21f26', font=("", 25, "bold"))
        self.compteur.place(x=120, y=100)

        self.Left = Label(self.bodyFrame3,  bg='#e21f26')
        self.Left.place(x=220, y=0)

        self.peopleLeft_label = Label(self.bodyFrame3, text="Pick Counter", bg='#e21f26', font=("", 12, "bold"),
                                      fg='white')
        self.peopleLeft_label.place(x=45, y=25)

        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.bodyFrame2, image=self.clock_image, bg="#009aa5")
        self.date_time_image.place(x=15, y=25)

        self.date_time = Label(self.bodyFrame2, bg="#009aa5")
        self.date_time.place(x=120, y=100)
        self.show_time()
        self.check_key_press()

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)
        
    def check_key_press(self):
        if keyboard.is_pressed('p'):
            self.increment += 1
            self.compteur.config(text=f"{self.increment}")
        self.window.after(100, self.check_key_press)
    
def wind():
    window = Tk()
    Dashboard2(window)
    window.mainloop()
    
wind()