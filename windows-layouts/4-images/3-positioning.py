from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.map_image = PhotoImage(file="U:/Problem Solving/COM404/windows-layouts/4-images/map.gif")
        self.bus_image = PhotoImage(file="U:/Problem Solving/COM404/windows-layouts/4-images/bus.gif")
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_title_label()
        self.__add_map_image_frame()
        self.__add_map_label()
        self.__add_bus_label()

    def __add_title_label(self):
        # create
        self.title_label = Label()
        self.title_label.grid(row=0, column=0)
        self.title_label.configure(text="Bus Journey")

    def __add_bus_label(self):
        # create
        self.bus_label  = Label(self.map_frame)
        self.bus_label.place(y=10, x=10)
        self.bus_label.configure(image=self.bus_image)    
    

    def __add_map_image_frame(self):
        # create
        self.map_frame = Frame()
        self.map_frame.grid(row=0, column=0)
        self.map_frame.configure(height=500, width=500)

    def __add_map_label(self):
        # create
        self.map_label = Label(self.map_frame)
        self.map_label.place(x=0, y=0)
        self.map_label.configure(image=self.map_image)

    from Tkinter import *
    
    root = Tk()
    
    def callback(event):
    print "clicked at", event.x, event.y
    frame = Frame(root, width=100, height=100)
    frame.bind("<Button-1>", callback)
    frame.pack()

root.mainloop()
        
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()