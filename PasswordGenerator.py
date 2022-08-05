from tkinter import *
from tkinter import messagebox
import string
import random
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())


root = Tk()
root.title("Password generator")
root.geometry("640x400")
root.iconbitmap(path + '\icon.ico')
root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)



#Creating frames
welcome_frame = Frame(root)
main_frame = Frame(root)

#==============Functions section==============
#Top menu implementation
def menu_top():
    """
        Function menu_top, creates menu on top of the program window.
    """
    
    def help_menu():
        messagebox.showinfo('Help', 'This program is made for creating randomly generated password with spcified properties. To create password u have to select desired collections, and specify length (default is 8). Than just click generate, and password will be automaticly generated. ')
    
    def author():
        messagebox.showinfo('Author info', 'Author => Krzysztof Służałek\nLinkedIn =>linkedin.com/in/krzysztof-sluzalek\nGitHub => github.com/Vercixxx')

    def version():
        messagebox.showinfo('Version', 'Version => 1.1')
    
    #Menu on top
    my_menu = Menu(root)
    root.config(menu=my_menu)


    #===============Menu items===============
    
    #label "File"
    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label= "Exit", command= root.quit)


    #label "More"
    more_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label= "More", menu=more_menu)
    more_menu.add_command(label= "Help", command= help_menu)
    more_menu.add_command(label= "Author", command= author)
    more_menu.add_command(label= "Version", command= version)
menu_top()

def pass_gen(small_letters, big_letters, digitss, symbolss, lenn):
    """Function pass_gen generates password on given instrucions, using random module.

    Args:
        small_letters (bool): If true adds small letters to password
        big_letters (bool): If true adds big letters to password
        digitss (bool): If true adds digits (0-9) to password
        symbolss (bool): If true adds symbols to password
        len (int): Length of password

    Returns:
        String: Randomly generated password
    """
    small_letters_list = list(string.ascii_lowercase)
    big_letters_list = list(string.ascii_uppercase)
    digitss_list = list(string.digits)
    symbolss_list = list(string.punctuation)

    list_of_characters = []
    
    if small_letters:
        list_of_characters = list_of_characters + small_letters_list
    
    if big_letters:
        list_of_characters = list_of_characters + big_letters_list
            
    if digitss:
        list_of_characters = list_of_characters + digitss_list
            
    if symbolss:
        list_of_characters = list_of_characters + symbolss_list
        

    
    random.shuffle(list_of_characters)
    
    output = random.choices(list_of_characters, k = lenn)
    output = "".join(output)
    return output


def generate_password():
    """
        Function generate_password, first check if user checked at least one option, and than invoke function pass_gen. Secondly this funcion create two canvas windows,
        first "canvas text" - label with text "Generated password:"
        second "canvas window" - label with generated password from pass_gen function
    """
    if small_letters_checkbox.get_state() == False and big_letters_checkbox.get_state() == False and digits_checkbox.get_state() == False and symbols_checkbox.get_state() == False:
        messagebox.showinfo('Error', 'Please select at least one option')
        
       
    else:
        password = pass_gen(small_letters_checkbox.get_state(),big_letters_checkbox.get_state(),digits_checkbox.get_state(),symbols_checkbox.get_state(),password_length.get())

        #Result text
        main_canvas.create_text(320,240, anchor=CENTER, text="Generated password:", font='Helvetica 18 bold', fill='white',)

        #Result password
        output_generated_password = StringVar(value=password)
        out_pas = Entry(main_frame, textvariable=output_generated_password, bd=0, justify=CENTER, font='Helvetica 13 bold', width=75, cursor='arrow', bg='grey', fg='white')
        main_canvas.create_window(320, 280, anchor=CENTER, window=out_pas)


def show_frame(frame):
    frame.tkraise()


for frame in (welcome_frame,main_frame):
    frame.grid(row= 0, column=0, sticky='nsew')
show_frame(welcome_frame)


#Adding background image
background_image = PhotoImage(file= path + "/background_image.png")

#==============Welcome frame section==============
welcome_canvas = Canvas(welcome_frame,highlightthickness=0)
welcome_canvas.pack(fill='both', expand=True)

#Setting background image
welcome_canvas.create_image(0,0, image=background_image, anchor='nw')

#Creating text
welcome_canvas.create_text(320,40, text="Welcome!", font='Helvetica 35 bold', fill='white', anchor='center')

welcome_canvas.create_text(320,100, text="To start press button below", font='Helvetica 20 bold', fill='white', anchor='center')


#Start button
start_button = Button(welcome_frame, text="S t a r t", command=lambda:show_frame(main_frame),relief=RAISED, justify=CENTER, font= 'Helvetica 20 bold', width=10, bg='#222222',fg='white' , borderwidth=4, cursor='hand2')
welcome_canvas.create_window(320, 250, anchor='center', window=start_button)

#version info
welcome_canvas.create_text(320,360, text="Version: 1.1", font='Helvetica 12', fill='white', anchor='center')






#==============Main frame section==============
main_canvas = Canvas(main_frame, highlightthickness=0)
main_canvas.pack(fill='both', expand=True)

#Setting background image
main_canvas.create_image(0,0, image=background_image, anchor='nw')

#Creating text
main_canvas.create_text(320,20, text="Select options", font='Helvetica 20 bold', fill='white', anchor='center')

#version info
main_canvas.create_text(320,360, text="Version: 1.1", font='Helvetica 12', fill='white', anchor='center')

#Checkbox class declaration
class my_checkbox():
    def __init__(self,display_text ,output_variable, placement_width):
        self.display_text = display_text
        self.output_variable = output_variable
        self.W = placement_width
        self.H = 70
        self.create_checkbox()
        
        
    def create_checkbox(self):
        self.output_variable = BooleanVar()
        self.checkbut = Checkbutton(main_frame, variable=self.output_variable, onvalue=True, offvalue=False, text=self.display_text, font='Helvetica 15 bold', indicatoron=0, width=10, height=1, bg='white',fg='black', selectcolor='#888888', relief=GROOVE, borderwidth=3, justify=CENTER, cursor='hand2')
        main_canvas.create_window(self.W, self.H, anchor=CENTER, window=self.checkbut )
        
    
    def get_state(self):
        """ 
        Returns state of checkbox

        Returns:
            Bool: True if checked, otherwhise False
        """
        return self.output_variable.get() 
        
        
    def __str__(self):
        return "my_checkbox class"
        
    def __repr__(self):
        return "my_checkbox class"





#Creating checbox instances
small_letters_checkbox = my_checkbox('Small letters', 'var1', 100)
big_letters_checkbox = my_checkbox('Big letters', 'var2', 250)
digits_checkbox = my_checkbox('Digits', 'var3', 400)
symbols_checkbox = my_checkbox('Symbols', 'var4', 550)



#Scale label
main_canvas.create_text(165,120, text="Choose length:", font='Helvetica 15 bold', fill='white', anchor='center')

scale_indicator = main_canvas.create_text(250,120, text='8', fill='white', font='Helvetica 15 bold', anchor='center')

def change_scale_indicator(value):
    """This Funcion shows actual value of scale

    Args:
        value: current value of scale
    """
    main_canvas.itemconfig(scale_indicator, text=str(value))


password_length= IntVar()
len_scale = Scale(main_frame, from_=8, to=50, orient=HORIZONTAL, variable=password_length, cursor='sb_h_double_arrow', bd=-1, troughcolor='grey', length=250, width=20, resolution=1, highlightthickness=0, showvalue=0, command=change_scale_indicator)
main_canvas.create_window(50, 150, anchor=W, window=len_scale)


#Result area
button_generate = Button(main_frame, text= "Generate", relief=RAISED, justify=CENTER, font= 'Helvetica 15 bold', width=14, bg='#222222',fg='white' , borderwidth=4, cursor='hand2', command=generate_password)
main_canvas.create_window(560,150, anchor=E, window=button_generate)


root.mainloop()