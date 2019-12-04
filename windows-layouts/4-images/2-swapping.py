from tkinter import *

class Gui(Tk):
    
def __init__(self):
        super().__init__()

        # load resources
        self.cactusleaves_image = PhotoImage(file="U:/Problem Solving/COM404/windows-layouts/4-images/cactusleaves.gif")
        self.palmtree_image = PhotoImage(file="U:/Problem Solving/COM404/windows-layouts/4-images/palmtree.gif")

        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_cactusleaves_image()
        self.__add_flip_button()
        
    def __add_heading_label(self):
     # create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        # style
        self.heading_label.configure(text="Cactus Leaves" , font="Arial 37")

    def __add_cactusleaves_image(self):
        # create
        self.cactusleaves_label = Label()
        self.cactusleaves_label.grid(row=1, column=0)
        self.cactusleaves_label.configure(image=self.cactusleaves_image, height=480, width=480)
        
    
    def __add_palmtree_image(self):
        # create 
        self.palmtree_label = Label()
        self.palmtree_label.grid(row=1, colmun=0)
        self.palmtree_label.configure(image=self.palmtree_image, height=360, width=360)


    def __add_flip_button(self):
        # create
        self.flip_button = Button()
        self.flip_button.grid(row=3, column=0)
        self.flip_button.configure(text="Flip.")
        self.flip_button.bind("<ButtonRelease-1>", self.__flip_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.__flip_button_clickedright)

    # events
    def __flip_button_clicked(self, event):
        self.cactusleaves_label.configure(image = self.palmtree_image)
    
    def __flip_button_clickedright(self, event):
        self.cactusleaves_label.configure(image = self.cactusleaves_image)

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()