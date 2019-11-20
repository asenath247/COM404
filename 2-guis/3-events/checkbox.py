from tkinter import *
class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Passport Checker")
        
        # add components
        self.__add_firstheading_label()
        self.__add_face_yes_checkbutton()
        self.__add_face_no_checkbutton()
        self.__add_secondheading_label()
        self.__add_validty_yes_checkbutton()
        self.__add_validty_no_checkbutton()
        self.__add_thirdheading__label()
        self.__add_visa_yes_checkbutton()
        self.__add_visa_no_checkbutton()


    def __add_firstheading_label(self):
        # create
        self.firstheading_label = Label()
        self.firstheading_label.grid(row=0, column=0)

        # style
        self.firstheading_label.configure(font="Arial 12", 
        text="Passport Checker")

    def __add_face_yes_checkbutton(self):
        # create
        self.__add_face_yes_checkbutton = Checkbutton(text = "Yes")
        self.__add_face_yes_checkbutton.grid(row=1, column=0)

    # self.face_yes_checkbutton = CheckButton(text = "Yes")
    #grid
    
    def __add_face_no_checkbutton(self):
        # create
        self.__add_face_no_checkbutton = Checkbutton(text = "No")
        self.__add_face_no_checkbutton.grid(row=1, column=1)

    def __add_secondheading_label(self):
        # create
        self.secondheading_label = Label()
        self.secondheading_label.grid(row=2, column=0)

    def __add_validty_yes_checkbutton(self):
        # create 
        self.__add_validty_yes_checkbutton = Checkbutton(text = "Yes")
        self.__add_validty_yes_checkbutton.grid(row=3, column=0)

    def __add_validty_no_checkbutton(self):
        # create 
        self.__add_validty_no_checkbutton = Checkbutton(text = "No")
        self.__add_validty_no_checkbutton.grid(row=3, column=1)
        
    def __add_thirdheading__label(self):
        # create
        self.__add_thirdheading__label= Label()
        self.__add_thirdheading__label.grid(row=4, column=0)

    def __add_visa_yes_checkbutton(self):
        # create 
            self.__add_visa_yes_checkbutton = Checkbutton(text = "Yes")
            self.__add_visa_yes_checkbutton.grid(row=5, column=0)
    
    def __add_visa_no_checkbutton(self):
    # create
        self.__add_visa_no_checkbutton = Checkbutton(text = "No")
        self.__add_visa_no_checkbutton.grid(row=5, column=1)





        



         

       