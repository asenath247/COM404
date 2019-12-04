from tkinter import *

class Gui(Tk):
    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes   
        self.title("Gui")
        self.configure(bg="#eee", 
                        height=500,
                        width=500, padx = 10, pady = 10 )
#call functions
        self.add_heading_label()
        self.add_instructional_label()
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()



# create
    def add_heading_label(self):
        self.heading_label = Label ()
        self.heading_label.pack(fill=X)
        self.heading_label.configure(font="Arial 14", 
                                     text="RECIEVE OUR NEWSLETTER.", pady = 10)


# create
    def add_instructional_label(self):
        self.instructional_label = Label ()
        self.instructional_label.pack(fill=X)
        self.instructional_label.configure(text="Please enter your email below to receive our newsletter.", justify= LEFT, padx = 10, pady=10)

# create
    def add_email_label(self):
        self.email_label = Label ()
        self.email_label.pack()
        self.email_label.configure(text="Email", padx = 10)
        
# create 
    def add_email_entry(self):
        self.email_entry = Label ()
        self.email_entry.pack()
        self.email_entry.configure(width=30, bd=2, fg="#f00")

# create 
    def add_subscribe_button(self):
        self.subscribe_button = Button ()
        self.subscribe_button.pack(fill=X)
        self.subscribe_button.configure(text="Subscribe", bg="#fee")

# the object
if __name__ == "__main__":
    gui = Gui()    
    gui.mainloop() 
