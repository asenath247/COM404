from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.ambulance_image = PhotoImage(file="U:/Problem Solving/COM404\windows-layouts/4-images/ambulance.gif")
        self.bike_image = PhotoImage(file="U:/Problem Solving/COM404/windows-layouts/4-images/bike.gif")
        self.plane_image = PhotoImage(file="U:/Problem Solving/COM404\windows-layouts/4-images/plane.gif")


        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()
        
    def __add_ambulance_image_label(self):
     # create
        self.ambulance_label = Label()
        self.ambulance_label.grid(row=0, column=0)
        self.ambulance_label.configure(image=self.ambulance_image, height=50, width=50)

    def __add_bike_image_label(self):
    # create
        self.bike_label = Label()
        self.bike_label.grid(row=0, column=1)
        self.bike_label.configure(image=self.bike_image, height=50, width=50)
 
    def __add_plane_image_label(self):
     # create
        self.plane_label = Label()
        self.plane_label.grid(row=0, column=2)
        self.plane_label.configure(image=self.plane_image, height=50, width=50)

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	
