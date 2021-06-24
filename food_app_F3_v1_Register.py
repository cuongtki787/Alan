from tkinter import*
from tkinter import ttk
class FoodApp :
    def __init__(self,parent):
#welcome frame
        self.Welcome = Frame(parent)
        self.Welcome.grid(row = 10, column=10)

        self.TitleLabel = Label(self.Welcome,text = "Welcome to Fast Food Botany",
                                 bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                 font = ("Time", '14', "bold italic")) 
        self.TitleLabel.grid(columnspan = 3)

        self.LoginButton = ttk.Button(self.Welcome, text = "Login",width= 15 , command = self.show_Login)
        self.LoginButton.grid(column = 1 , row =2 )

        self.RegisterButton = ttk.Button(self.Welcome, text = "Register",width = 15, command = self.show_Register)
        self.RegisterButton.grid(column = 1 , row =4 )



        #login frame
        self.Login = Frame(parent)
        self.TitleLabel = Label(self.Login, text = "Login",
                             bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.TitleLabel.grid(columnspan= 2)
        self.UsernameLabel = Label(self.Login, text = "Username", anchor = W, fg = "black", width = 10, padx = 30, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.UsernameLabel.grid(row = 2, column = 0) 
        self.PasswordLabel = Label(self.Login, text = "Password", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.PasswordLabel .grid (row=3, column = 0) 
      
        self.UsernameEntry = ttk.Entry(self.Login, width = 20)
        self.UsernameEntry.grid(row = 2 , column = 1, columnspan = 2)

        self.PasswordEntry = ttk.Entry(self.Login, width = 20)
        self.PasswordEntry.grid(row = 3 , column = 1)

        self.LoginButton = ttk.Button(self.Login, text = "Login",width= 15 , command = self.show_Login)
        self.LoginButton.grid( row =4, column = 1 )

        #register frame
        self.Register = Frame(parent)
        self.TitleLabel = Label(self.Register, text = "Register",
                             bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.TitleLabel.grid(columnspan= 2)

        self.NameLabel = Label(self.Register, text = "Name", anchor = W, fg = "black", width = 10, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.NameLabel.grid(row=2,column=0)

        self.NameEntry = ttk.Entry(self.Register, width = 40)
        self.NameEntry.grid(row = 3 , column = 0, columnspan = 2)

        self.PhoneLable = Label(self.Register,text="Contact Number",anchor=W, fg = "black", width = 30, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic"))
        self.PhoneLable.grid(row = 4, column = 0,columnspan=2)

        self.PhoneEntry = ttk.Entry(self.Register, width = 40)
        self.PhoneEntry.grid(row = 5 , column = 0, columnspan = 2)

        self.UsernameLabel = Label(self.Register, text = "Username", anchor = W, fg = "black", width = 10, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.UsernameLabel.grid(row = 6, column = 0) 

        self.UsernameEntry = ttk.Entry(self.Register, width = 40)
        self.UsernameEntry.grid(row = 7 , column = 0, columnspan = 2)

        self.PasswordLabel = Label(self.Register, text = "Password", anchor = W, fg = "black", width = 10, padx = 10, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.PasswordLabel .grid (row=8, column = 0)
        
        self.PasswordEntry = ttk.Entry(self.Register, width = 40)
        self.PasswordEntry.grid(row = 9 , column = 0,columnspan = 2)

        self.ConfirmLabel = Label(self.Register, text = "Password Confirmation", anchor = W, fg = "black", width = 30, padx = 10, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.ConfirmLabel .grid (row=10,column = 0,columnspan = 2 )
        
        self.ConfirmEntry = ttk.Entry(self.Register,width = 40)
        self.ConfirmEntry.grid(row = 11, column = 0,columnspan = 2)

        self.LoginButton = ttk.Button(self.Register, text = "Register",width= 15 , command = self.show_Welcome)
        self.LoginButton.grid( row =12, column = 1 )





    #def
    def show_Welcome(self):
        self.Register.grid_remove()
        self.Welcome.grid()

    def show_Login(self):
        self.Welcome.grid_remove()
        self.Login.grid()
    
    def show_Register(self):
        self.Welcome.grid_remove()
        self.Register.grid()
    
    def show_Menu(self):
        self.Login.grid_remove()
        self.Menu.grid()


    


if __name__ == "__main__":
    root = Tk()
    frames = FoodApp(root)
    root.title("App")
    root.mainloop()
