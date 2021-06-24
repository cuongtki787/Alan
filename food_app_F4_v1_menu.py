import getpass
import hashlib
import os
clear = lambda: os.system('cls')
from tkinter import*
from tkinter import ttk


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
      
        self.username_entry = ttk.Entry(self.login, width = 20)
        self.username_entry.grid(row = 2 , column = 1, columnspan = 2)

        self.password_entry = ttk.Entry(self.login, width = 20, show= '*')
        self.password_entry.grid(row = 3 , column = 1)

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
        
        
        self.phone_lable = Label(self.register,text="Contact Number",anchor=W, fg = "black", width = 30, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic"))
        self.phone_lable.grid(row = 4, column = 0,columnspan=2)

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

        
        self.password_entry = ttk.Entry(self.register, width = 40,show="*")
        self.password_entry.grid(row = 9 , column = 0,columnspan = 2)

        self.confirm_Label = Label(self.register, text = "Password Confirmation", anchor = W, fg = "black", width = 30, padx = 10, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.confirm_Label .grid (row=10,column = 0,columnspan = 2 )
        

        self.confirm_entry = ttk.Entry(self.register,width = 40,show="*")
        self.confirm_entry.grid(row = 11, column = 0,columnspan = 2)

        self.login_button = ttk.Button(self.register, text = "Register",width= 15 , command = self.register_function)
        self.login_button.grid( row =14, column = 1 )
        
        self.return_button = ttk.Button(self.register, text = "Return",width= 15 , command = self.return_menu)
        self.return_button.grid( row =14, column = 0 )

        self.warning_label = Label(self.register , text="" , anchor = W, fg = "red", width =20 , padx = 30 , pady = 10)
        self.warning_label.grid(row = 13, column = 1)


        #Menu Frame

        self.menu = Frame(parent)
        self.titlelabel = Label(self.menu, text = "Fast Food Botany Ordering Menu",
                             bg = "black", fg = "white", width = 30, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.titlelabel.grid(columnspan= 2)
        self.menu.grid_propagate(4)

        food_price_label = Label(self.menu,text = "Fast Food: $10",width = 12, padx = 30, pady = 10,
                             font = ("Time", "14", "bold italic"))
        food_price_label.grid(row = 1,column = 0)
        

        food_list = ["Fry Chicken", "Hamberger", "Meatball Subs", " Pizza"," Hotdog", "Onion Ring"]
        self.food_label=[]

        for i in range (len(food_list)):
            ColumnHeading = Label(self.menu, text = food_list[i], width = "20", height = "2" ,font = ("Vernada","12","bold") )
            self.food_label.append(ColumnHeading)
            ColumnHeading.grid(row = i+2 , column = 0)

        drink_price_label = Label(self.menu,text = "Drink: $3.00",width = 12, padx = 30, pady = 10,
                             font = ("Time", "14", "bold italic"))
        drink_price_label.grid(row = 1,column = 1)
        
        line_6 = Canvas(self.menu, width=700, height=0.1, bg="black", highlightthickness=0.1,)
        line_6.place(x=0, y=80)
    
        drink_list = ["Coca Cola","Pepsi","7 Ups"]
        self.drink_label = []

        for i in range (len(drink_list)):
            column_heading = Label(self.menu, text = food_list[i], width = "10", height = "2" ,font = ("Vernada","12","bold") )
            self.drink_label.append(column_heading)
            column_heading.grid(row = i+2 , column = 1 )

        #adding food button
        add_button_food  = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_food.place(x = 125, y =125)

        add_button_food1 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_food1.place(x = 125, y =169)

        add_button_food2 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_food2.place(x = 125, y =213)

        add_button_food3 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_food3.place(x = 125, y =257)

        add_button_food4 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_food4.place(x = 125, y =300)

        add_button_food5 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_food5.place(x = 125, y =344)

        # take off food button
        take_button_food  = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_food.place(x = 75, y =125)

        take_button_food1 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_food1.place(x = 75, y =169)

        take_button_food2 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_food2.place(x = 75, y =213)

        take_button_food3 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_food3.place(x = 75, y =257)

        take_button_food4 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_food4.place(x = 75, y =300)

        take_button_food5 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_food5.place(x = 75, y =344)

        #adding drink button
        add_button_drink  = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_drink.place(x = 340, y =125)

        add_button_drink1 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_drink1.place(x = 340, y =169)

        add_button_drink2 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_drink2.place(x = 340, y =213)

        add_button_drink3 = Button(self.menu,text="+",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        add_button_drink3.place(x = 340, y =257)

        #take off drink function
        take_button_drink  = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_drink.place(x = 290, y =125)

        take_button_drink1 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_drink1.place(x = 290, y =169)

        take_button_drink2 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_drink2.place(x = 290, y =213)

        take_button_drink3 = Button(self.menu,text="-",font = ("Vernada","9","bold"),command = self.add, height=1 ,width=1)
        take_button_drink3.place(x = 290, y =257)

        #finish order button
        finish_button = ttk.Button(self.menu,text= "Finish" )
        finish_button.grid(row = 13,column=1)
        
        #total_label = ttk.Label(self.menu)
        




        
              
        
        





    #def
    def show_login(self):

        self.welcome.grid_remove()
        self.login.grid()
    
    def show_Register(self):
        self.welcome.grid_remove()
        self.register.grid()
               
    
    def show_Menu(self):
        self.login.grid_remove()
        self.menu.grid()

    def register_function(self): 
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

            elif self.confirm_entry.get() != self.password_entry.get() :
                self.warning_label.configure(text = "Your password did not match")
                self.confirm_entry.delete(0, END)
                self.confirm_entry.focus() 
            else:
                self.warning_label.configure(text =" Account Created")
                name = self.name_entry.get()
                username = self.username_entry.get()
                password = self.password_entry.get()
                num = self.phone_entry.get()
                with open("account.txt", "a+") as data_file:
                    data_file.write(name + " ")
                    data_file.write(username + " ")
                    data_file.write(password + " ")
                    data_file.write(num)
                
        
        except ValueError: 
            self.warning_label.configure(text = "Please enter number only") 
            self.phone_entry.delete(0, END) 
            self.phone_entry.focus()

    def return_menu(self):
        self.register.grid_remove()
        self.welcome.grid()
    
    def add(self):
        self.register.grid_remove()
        self.welcome.grid()



    


if __name__ == "__main__":
    root = Tk()
    frames = FoodApp(root)
    root.title("App")
    root.mainloop()
