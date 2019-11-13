from tkinter import *

class Gui(Tk):
    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes   
        self.title("Gui")
        self.configure(bg="#eee",
                        height=500,
                        width=500)
#call functions
        self.add_heading_label()
        self.add_middleheading_label()
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()



    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font="Arial 29", 
                                     text="RECIEVE OUR NEWSLETTER.")

        

    def add_middleheading_label(self):
        # create
        self.middleheading_label = Label()
        self.middleheading_label.pack()
        self.middleheading_label.configure(font="Arial 18", 
                                     text="Please enter your email below to recieve our newsletter.")

        # ...assigning any event handlers to the component
    
    

    
    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()

    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure(font="Arial 18",
                                        text="Email:")

    def add_email_entry(self):
        self.email_entry = Entry (self.email_frame)
        self.email_entry.pack(side=RIGHT)
        
 

 