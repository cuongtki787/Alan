from tkinter import*
from tkinter import ttk
import os

class FoodApp :
    def __init__(self,parent):
#welcome frame
        self.welcome = Frame(parent)
        self.welcome.grid(row = 10, column=10)

        self.title_label = Label(self.welcome,text = "Welcome to Fast Food Botany",
                                 bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                 font = ("Time", '14', "bold italic")) 
        self.title_label.grid(columnspan = 3)

        self.login_button = ttk.Button(self.welcome, text = "Login",width= 15 , command = self.show_login)
        self.login_button.grid(column = 1 , row =2 )

        self.register_button = ttk.Button(self.welcome, text = "Register",width = 15, command = self.show_Register)
        self.register_button.grid(column = 1 , row =4 )



        #login frame
        self.login = Frame(parent)
        self.title_label = Label(self.login, text = "login",
                             bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.title_label.grid(columnspan= 2)
        self.username_label = Label(self.login, text = "Username", anchor = W, fg = "black", width = 10, padx = 30, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.username_label.grid(row = 2, column = 0) 
        self.password_label = Label(self.login, text = "Password", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.password_label .grid (row=3, column = 0) 
      
        self.username_entry_log = ttk.Entry(self.login, width = 20)
        self.username_entry_log.grid(row = 2 , column = 1, columnspan = 2)

        self.password_entry_log = ttk.Entry(self.login, width = 20, show= '*')
        self.password_entry_log.grid(row = 3 , column = 1)

        self.login_button = ttk.Button(self.login, text = "Login",width= 15 , command = self.show_Menu)
        self.login_button.grid( row =4, column = 1 )

        #register frame
        self.register = Frame(parent)
        self.title_label = Label(self.register, text = "Register",
                             bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.title_label.grid(columnspan= 2)

        self.name_label = Label(self.register, text = "Name", anchor = W, fg = "black", width = 10, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.name_label.grid(row=2,column=0)
        
    
        self.name_entry = ttk.Entry(self.register, width = 40)
        self.name_entry.grid(row = 3 , column = 0, columnspan = 2)
        
        self.phone_entry
        self.phone_lable = Label(self.register,text="Contact Number",anchor=W, fg = "black", width = 30, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic"))
        self.phone_lable.grid(row = 4, column = 0,columnspan=2)

        self.phone_num = IntVar

        self.phone_entry = ttk.Entry(self.register, width = 40)
        self.phone_entry.grid(row = 5 , column = 0, columnspan = 2)
        
        
        self.username_label = Label(self.register, text = "Username", anchor = W, fg = "black", width = 10, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.username_label.grid(row = 6, column = 0) 
        
        
        self.username_entry = ttk.Entry(self.register, width = 40)
        self.username_entry.grid(row = 7 , column = 0, columnspan = 2)

        
        self.password_label = Label(self.register, text = "Password", anchor = W, fg = "black", width = 10, padx = 10, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.password_label .grid (row=8, column = 0)

        
        self.password_entry = ttk.Entry(self.register, width = 40)
        self.password_entry.grid(row = 9 , column = 0,columnspan = 2)

        self.confirm_Label = Label(self.register, text = "Password Confirmation", anchor = W, fg = "black", width = 30, padx = 10, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.confirm_Label .grid (row=10,column = 0,columnspan = 2 )
        

        self.confirm_entry = ttk.Entry(self.register,width = 40)
        self.confirm_entry.grid(row = 11, column = 0,columnspan = 2)

        self.login_button = ttk.Button(self.register, text = "Register",width= 15 , command = self.return_menu_)
        self.login_button.grid( row =13, column = 1 )

        self.warning_label = Label(self.register , text="" , anchor = W, fg = "red", width =20 , padx = 30 , pady = 10)
        self.warning_label.grid(row = 14, column = 1)


        #Menu Frame

        self.Menu = Frame(parent)
        self.titlelabel = Label(self.Menu, text = "Menu",
                             bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.titlelabel.grid(columnspan= 2)
        
               #photoimage = photo.subsample(3, 3)

        #self.FoodButton = ttk.Button(self.Menu,image= PhotoImage, compound=TOP)
        #self.FoodButton.grid(row =2,column =0)
        
        





    #def
    def show_login(self):
        self.welcome.grid_remove()
        self.login.grid()
    
    def show_Register(self):
        self.welcome.grid_remove()
        self.register.grid()
               
    
    def show_Menu(self):
        username_info = self.username_entry_log.get()
        password_info = self.password_entry_log.get()
        list_of_files = os.listdir()
        if username_info in list_of_files:
            file1 = open(username_info)
        self.login.grid_remove()
        self.Menu.grid()

    def return_menu(self): 
        try:
            if self.name_entry.get() == "": 
                self.warning_label.configure(text = "Please enter Name") 
                self.name_entry.focus() 

            elif self.name_entry.get().isalpha() == False: 
                self.warning_label.configure(text = "Pleasae enter text only") 
                self.name_entry.delete(0, END) 
                self.name_entry.focus()

            elif self.phone_entry.get() == "": 
                self.warning_label.configure(text = "Please enter Phone Number") 
                self.phone_entry.focus()
            
            elif self.username_entry.get() == "": 
                self.warning_label.configure(text = "Please enter Username") 
                self.username_entry.focus() 

            elif self.username_entry.get().isalpha() == False: 
                self.warning_label.configure(text = "Pleasae enter text") 
                self.username_entry.delete(0, END) 
                self.username_entry.focus()

            elif self.password_entry.get()== "":
                self.warning_label.configure(text = "Please enter password")
                self.password_entry.focus()
            
            elif self.confirm_entry.get()=="":
                self.warning_label.configure(text = "Please enter the password again")
                self.confirm_entry.focus()

            elif self.confirm_entry.get() == self.password_entry.get() == False:
                self.warning_label.configure(text = "Incorrect passwaord")          
            
        
        except ValueError: 
            self.warning_label.configure(text = "Please enter number only") 
            self.phone_entry.delete(0, END) 
            self.phone_entry.focus()

    


if __name__ == "__main__":
    root = Tk()
    frames = FoodApp(root)
    root.title("App")
    root.mainloop()
