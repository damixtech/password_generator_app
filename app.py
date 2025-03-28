from tkinter import *
from ttkbootstrap import Style
import random
import string


#Class
class App():
    def __init__(self, window):
        #self.style = Style(theme='morph')
        self.window = window
        self.window.title('Password generator')
        self.window.geometry('600x500')
        self.window.minsize(350, 450)
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
        self.header_frame = Frame(self.window, pady=40)
        self.header_frame.pack()
        #Title
        self.header = Label(self.header_frame, text="Password Generator", font=('Poppins', 20, 'bold'))
        self.header.pack()
        #Subtitle
        self.subheader = Label(self.header_frame, text='Generate a strong password in seconds', font=('Poppins', 12))
        self.subheader.pack()
        ###FRAME: Password box
        self.password_frame = LabelFrame(self.window, text="Your password", relief="flat")
        self.password_frame.config(highlightbackground='white', highlightcolor='white', highlightthickness=2)
        self.password_frame.pack()
        #Final password
        self.final_pasword = Label(self.password_frame, text="", width=29)
        self.final_pasword.pack(side="left")
        self.copy_button = Button(self.password_frame, text='Copy')
        self.copy_button.pack(side="right", pady=10)
        ###FRAME: Customize box
        self.customize_frame = Frame(self.window, width=50, padx=20, pady=20)
        self.customize_frame.config(highlightbackground='white', highlightthickness=2, highlightcolor='white')
        self.customize_frame.pack(pady=20)
        #Title
        self.customize_title = Label(self.customize_frame, text='Customize your password', font=('Poppins', 12))
        self.customize_title.config(pady=10)
        self.customize_title.pack()
        #Length selector
        self.length_frame = Frame(self.customize_frame)
        self.length_frame.pack(side='left', padx=20)
        self.length_label = Label(self.length_frame, text="Password Length")
        self.length_label.pack(anchor="w")
        self.length_control = Scale(self.length_frame, variable=self.length_var, from_=8, to=24, resolution=1, orient=HORIZONTAL)
        self.length_control.pack(anchor="w")
        #Character selector
        #FRAME: Radiobuttons
        self.check_buttons_frame = Frame(self.customize_frame, relief="flat")
        self.check_buttons_frame.pack(padx=20)
        self.uppercase = Checkbutton(self.customize_frame, text='Uppercase', variable=self.uppercase_var, relief="flat")
        self.uppercase.pack(anchor="w")
        self.lowercase = Checkbutton(self.customize_frame, text='Lowercase', variable=self.lowercase_var, relief="flat")
        self.lowercase.pack(anchor="w")
        self.numbers = Checkbutton(self.customize_frame, text='Numbers', variable=self.numbers_var, relief="flat")
        self.numbers.pack(anchor="w")
        self.symbols = Checkbutton(self.customize_frame, text='Symbols', variable=self.symbols_var, relief="flat")
        self.symbols.pack(anchor="w")
        ###WINDOW
        #Generate button
        self.generate_button = Button(self.window, text='Generate', command=self.check_selector)
        self.generate_button.pack()
        

    def check_selector(self):
        """Check the check buttons wich are selected"""
        self.final_length = self.length_var.get()
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
        #Call the function that generates the password
        self.generate_password()


    def generate_password(self):
        """Generates the new pasword"""
        self.upper_char = string.ascii_uppercase
        self.lower_char = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = string.punctuation
        self.characters = ''

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

    
    def copy_password(self):
        pass


app = App(Tk())
app.window.mainloop()