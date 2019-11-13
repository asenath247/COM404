from tkinter import *

class Gui(Tk):

  # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
        height=500, 
        width=500)

        self.add_heading_label()
        self.add_middleheading_label()
        #self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()


    def add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        # style
        self.heading_label.configure(font="Arial 24",
        text="RECIEVE OUR NEWSLETTER.")


    def add_middleheading_label(self):
        self.middleheading_label = Label()
        self.middleheading_label.grid(row=1, column=0, columnspan=2)
        self.middleheading_label.configure(font="Arial 18", 
        text="Please enter your email below to recieve our newsletter.")

    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.grid(row=2, column=1, columnspan=1)


    def add_email_label(self):
        self.email_label = Label()
        self.email_label.grid(row=2, column=0, columnspan=1)
        self.email_label.configure(font="Arial 18",
        text="Email:")


    def add_email_entry(self):
        self.email_entry = Entry ()
        self.email_entry.grid(row=2, column=1, columnspan=1)
 