from tkinter import *
import random as rd
import string
from ttkbootstrap import Style


#Class
class App():
    def __init__(self, window):
        #Main window
        #self.style = Style(theme="morph")
        self.window = window
        self.window.title('Password generator')
        self.window.geometry('600x500')
        self.window.minsize(350, 450)
        self.window.config(bg='#4A90E2')
        #Control Variables
        self.length_var = DoubleVar()
        self.uppercase_var = BooleanVar()
        self.lowercase_var = BooleanVar()
        self.numbers_var = BooleanVar()
        self.symbols_var = BooleanVar()
        #Method that creates widgets
        self.create_widgets()


    def create_widgets(self):
        '''Create all the components of the app'''
        ###FRAME: Header
        self.header_frame = Frame(self.window, pady=40, bg='#4A90E2')
        self.header_frame.pack()
        #Title
        self.header = Label(self.header_frame, text="Password Generator", font=('Poppins', 20, 'bold'),
                            bg='#4A90E2', fg='#FFFFFF')
        self.header.pack()
        #Subtitle
        self.subheader = Label(self.header_frame, text='Generate a strong password in few seconds', font=('Poppins', 12),
                               bg='#4A90E2', fg='#FFFFFF')
        self.subheader.pack()
        ###FRAME: Password box
        self.password_frame = LabelFrame(self.window, text="Your password", width=100, height=50, relief="flat", bg='#4A90E2', fg='#FFFFFF')
        #White border config
        self.password_frame.config(highlightbackground='white', highlightcolor='white', highlightthickness=2,
                                   font=('Poppins',12))
        self.password_frame.pack(padx=0)
        #Final password
        self.final_password = Label(self.password_frame, text="", width=37, bg='#4A90E2')
        self.final_password.pack(side="left", anchor="w")
        self.copy_button = Button(self.password_frame, text='Copy', command=self.copy_password,
                                  bg="#50E3C2", activebackground='#4A90E2', activeforeground='#FFFFFF',
                                  relief="flat", font=('Poppins',12))
        self.copy_button.pack(side="right", pady=10, anchor="e", padx=0)
        ###FRAME: Customize box
        self.customize_frame = Frame(self.window, width=70, padx=40, pady=20, bg='#4A90E2')
        #White border config
        self.customize_frame.config(highlightbackground='white', highlightthickness=2, highlightcolor='white')
        self.customize_frame.pack(pady=20)
        #Title
        self.customize_title = Label(self.customize_frame, text='Customize your password', font=('Poppins', 12),
                                     bg='#4A90E2', fg='#FFFFFF')
        self.customize_title.config(pady=5)
        self.customize_title.pack()
        #Length selector
        self.length_frame = Frame(self.customize_frame, bg='#4A90E2', pady=20)
        self.length_frame.pack(side='left', padx=20)
        self.length_label = Label(self.length_frame, text="Password Length", bg='#4A90E2', fg='#FFFFFF', font=('Poppins',10))
        self.length_label.pack(anchor="w")
        self.length_control = Scale(self.length_frame, variable=self.length_var, from_=8, to=24, resolution=1,
                                    troughcolor='#FFFFFF', orient=HORIZONTAL, bg='#4A90E2', highlightthickness=0,
                                    relief="flat", sliderrelief="flat", activebackground='#50E3C2')
        self.length_control.pack(anchor="w")
        #Character selector
        #FRAME: Radiobuttons
        self.check_buttons_frame = Frame(self.customize_frame, relief="flat", bg='#4A90E2')
        self.check_buttons_frame.pack(padx=20)
        self.uppercase = Checkbutton(self.customize_frame, text='Uppercase',
                                     variable=self.uppercase_var,
                                     highlightthickness=0,
                                     relief="flat",
                                     bg='#4A90E2', fg='#FFFFFF',
                                     activebackground='#50E3C2',
                                     font=('Poppins',12), selectcolor='#50E3C2')
        self.uppercase.pack(anchor="w")
        self.lowercase = Checkbutton(self.customize_frame, text='Lowercase',
                                     variable=self.lowercase_var,
                                     highlightthickness=0,
                                     relief="flat",
                                     bg='#4A90E2', fg='#FFFFFF',
                                     activebackground='#50E3C2',
                                     font=('Poppins',12), selectcolor='#50E3C2')
        self.lowercase.pack(anchor="w")
        self.numbers = Checkbutton(self.customize_frame, text='Numbers',
                                   variable=self.numbers_var,
                                   highlightthickness=0, 
                                   relief="flat",
                                   bg='#4A90E2', fg='#FFFFFF',
                                   activebackground='#50E3C2',
                                   font=('Poppins',12), selectcolor='#50E3C2')
        self.numbers.pack(anchor="w")
        self.symbols = Checkbutton(self.customize_frame, text='Symbols',
                                   variable=self.symbols_var,
                                   highlightthickness=0, relief="flat",
                                   bg='#4A90E2', fg='#FFFFFF',
                                   activebackground='#50E3C2',
                                   font=('Poppins',12), selectcolor='#50E3C2')
        self.symbols.pack(anchor="w")
        ###WINDOW
        #Generate button
        self.generate_button = Button(self.window, text='Generate', command=self.check_selector,
                                      bg="#50E3C2", activebackground='#4A90E2', activeforeground='#FFFFFF',
                                      relief="flat", font=('Poppins',12))
        self.generate_button.pack()
        

    def check_selector(self):
        """Check the check buttons wich are selected"""
        #Extract the values
        self.final_length = int(self.length_var.get())
        self.uppercase_value = self.uppercase_var.get()
        self.lowercase_value = self.lowercase_var.get()
        self.numbers_value = self.numbers_var.get()
        self.symbols_value = self.symbols_var.get()
        #Save the values
        self.selector_values = {
            'uppercase': self.uppercase_value,
            'lowercase': self.lowercase_value,
            'numbers': self.numbers_value,
            'symbols': self.symbols_value
        }
        #Create vars for saving diferent characters
        self.upper_char = string.ascii_uppercase
        self.lower_char = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = string.punctuation
        self.characters = ''
        #Check the selectors
        for key, value in self.selector_values.items():
            #Add uppercase char
            if (key == 'uppercase') and (self.selector_values[key] == True):
                self.characters += self.upper_char
            #Add lowercase char
            elif (key == 'lowercase') and (self.selector_values[key] == True):
                self.characters += self.lower_char
            #Add numbers
            elif (key == 'numbers') and (self.selector_values[key] == True):
                self.characters += self.digits
            #Add special char
            elif (key == 'symbols') and (self.selector_values[key] == True):
                self.characters += self.symbols
        #Call the function that generates the password
        self.generate_password()


    def generate_password(self):
        """Generates the new pasword"""
        self.new_password = ''
        for i in range(0, self.final_length):
            self.char = rd.choice(self.characters)
            self.new_password += self.char
        self.show_password()
        

    def show_password(self):
        self.final_password.config(text=self.new_password, fg='#FFFFFF', padx=0, anchor="w", font=('Poppins',10))


    def copy_password(self):
        password = self.new_password
        app.window.clipboard_append(password)
        app.window.update()


app = App(Tk())
app.window.mainloop() #Esto sería root en programación funcional.