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
        self.register_button.grid(column = 1 , row =3 )

        self.close_button = ttk.Button(self.welcome, text = "Close",width = 15, command = self.close)
        self.close_button.grid(column = 1 , row =4 )



        #login frame
        self.login = Frame(parent)
        self.title_label = Label(self.login, text = "Login",
                             bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.title_label.grid(columnspan= 2)
        self.username_label = Label(self.login, text = "Username", anchor = W, fg = "black", width = 10, padx = 30, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.username_label.grid(row = 2, column = 0) 
        self.password_label = Label(self.login, text = "Password", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.password_label .grid (row=3, column = 0) 
      
        self.username_entry_log = ttk.Entry(self.login ,width = 20)
        self.username_entry_log.grid(row = 2 , column = 1, columnspan = 2)

        self.password_entry_log = ttk.Entry(self.login, width = 20,show= '*')
        self.password_entry_log.grid(row = 3 , column = 1)

        self.warning_label_log = Label(self.login,text = "",fg = "red", width =20 , padx = 30 , pady = 10)
        self.warning_label_log.grid(row = 4, column = 0)


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
              
        
        self.username_label = Label(self.register, text = "Username", anchor = W, fg = "black", width = 10, padx = 10, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.username_label.grid(row = 4, column = 0) 
        
        
        self.username_entry = ttk.Entry(self.register, width = 40)
        self.username_entry.grid(row = 5 , column = 0, columnspan = 2)

        
        self.password_label = Label(self.register, text = "Password", anchor = W, fg = "black", width = 10, padx = 10, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.password_label .grid (row=6, column = 0)

        
        self.password_entry = ttk.Entry(self.register, width = 40,show="*")
        self.password_entry.grid(row = 7 , column = 0,columnspan = 2)

        self.confirm_Label = Label(self.register, text = "Password Confirmation", anchor = W, fg = "black", width = 30, padx = 10, pady = 10, 
                                                            font = ("Time", '12', "bold italic")) 
        self.confirm_Label .grid (row=8,column = 0,columnspan = 2 )
        

        self.confirm_entry = ttk.Entry(self.register,width = 40,show="*")
        self.confirm_entry.grid(row = 9, column = 0,columnspan = 2)

        self.login_button = ttk.Button(self.register, text = "Register",width= 15 , command = self.register_function)
        self.login_button.grid( row =11, column = 1 )
        
        self.return_button = ttk.Button(self.register, text = "Return",width= 15 , command = self.return_menu)
        self.return_button.grid( row =11, column = 0 )

        self.warning_label = Label(self.register , text="" , anchor = W, fg = "red", width =20 , padx = 30 , pady = 10)
        self.warning_label.grid(row = 10, column = 1)


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
            ColumnHeading.grid(row = 2*i+2 , column = 0)

        drink_price_label = Label(self.menu,text = "Drink: $3.00",width = 12, padx = 30, pady = 10,
                             font = ("Time", "14", "bold italic"))
        drink_price_label.grid(row = 1,column = 1)
        
        line_1 = Canvas(self.menu, width=700, height=0.1, bg="black", highlightthickness=0.1,)
        line_1.place(x=0, y=80)

        line_2 = Canvas(self.menu, width=0.1, height=300, bg="black", highlightthickness=0.1,)
        line_2.place(x=210, y=45)
    
        drink_list = ["Coca Cola","Pepsi","7 Ups"]
        self.drink_label = []

        for i in range (len(drink_list)):
            column_heading = Label(self.menu, text = drink_list[i], width = "10", height = "2" ,font = ("Vernada","12","bold") )
            self.drink_label.append(column_heading)
            column_heading.grid(row = 2*i+2 , column = 1 )

        

        item_range = [0, 1, 2, 3, 4, 5]
        
        #food drop down
        self.food = IntVar()
        self.food.set(0)

        self.food1 = IntVar()
        self.food1.set(0)

        self.food2 = IntVar()
        self.food2.set(0)

        self.food3 = IntVar()
        self.food3.set(0)

        self.food4 = IntVar()
        self.food4.set(0)

        self.food5 = IntVar()
        self.food5.set(0)

        self.food6 = IntVar()
        self.food6.set(0)

        self.food_drop_down = OptionMenu(self.menu,self.food,*item_range)
        self.food_drop_down.grid(row =3,column=0)
        self.food_drop_down.config(width=10)
        

        self.food_1_drop_down = OptionMenu(self.menu,self.food1,*item_range)
        self.food_1_drop_down.grid(row =3,column=0)
        self.food_1_drop_down.config(width=10 )

        self.food_2_drop_down = OptionMenu(self.menu,self.food2,*item_range)
        self.food_2_drop_down.grid(row =5,column=0)
        self.food_2_drop_down.config(width=10 )

        self.food_3_drop_down = OptionMenu(self.menu,self.food3,*item_range)
        self.food_3_drop_down.grid(row =7,column=0)
        self.food_3_drop_down.config(width=10 )

        self.food_4_drop_down = OptionMenu(self.menu,self.food4,*item_range)
        self.food_4_drop_down.grid(row =9,column=0)
        self.food_4_drop_down.config(width=10 )

        self.food_5_drop_down = OptionMenu(self.menu,self.food5,*item_range)
        self.food_5_drop_down.grid(row =11,column=0)
        self.food_5_drop_down.config(width=10 )

        self.food_6_drop_down = OptionMenu(self.menu,self.food6,*item_range)
        self.food_6_drop_down.grid(row =13,column=0)
        self.food_6_drop_down.config(width=10 )

        #drink drop down
        self.drink = IntVar()
        self.drink.set(0)

        self.drink1 = IntVar()
        self.drink1.set(0)

        self.drink2 = IntVar()
        self.drink2.set(0)

        self.drink_1_drop_down = OptionMenu(self.menu,self.drink,*item_range)
        self.drink_1_drop_down.grid(row =3,column=1)
        self.drink_1_drop_down.config(width=10)

        self.drink_2_drop_down = OptionMenu(self.menu,self.drink1,*item_range)
        self.drink_2_drop_down.grid(row =5,column=1)
        self.drink_2_drop_down.config(width=10 )

        self.drink_3_drop_down = OptionMenu(self.menu,self.drink2,*item_range)
        self.drink_3_drop_down.grid(row =7,column=1)
        self.drink_3_drop_down.config(width=10 )

    
        self.warning_label_menu = Label(self.menu,text="",fg = "red", width =20 , padx = 30 , pady = 10)
        self.warning_label_menu.grid(row=12,column = 1)

         
        #finish order button
        finish_button = ttk.Button(self.menu,text= "Order",command=self.finish)
        finish_button.grid(row = 13,column=1)
        
        
        #total
        
        
        self.bill = Frame(parent)
        self.titlelabel = Label(self.bill, text = "Fast Food Botany Ordering ",
                             bg = "black", fg = "white", width = 30, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic")) 
        self.titlelabel.grid(columnspan= 2)

        self.total_label = Label(self.bill,text = "",width = 10, padx = 30, pady = 10,
                                                            font = ("Time", '12', "bold italic"))
        self.total_label.grid(row =2 , column =0)
        
        self.name_bill = Label(self.bill,text="Name",anchor = W, fg = "black", padx = 30, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.name_bill.grid(row = 3, column = 0)
        self.name_e_bill = ttk.Entry (self.bill,width=20)
        self.name_e_bill.grid(row = 3, column = 1) 



        self.phone_num = Label(self.bill,text="Contact Number",anchor = W, fg = "black",  padx = 30, pady = 10,
                                                            font = ("Time", '12', "bold italic")) 
        self.phone_num.grid(row = 4, column = 0)
        self.phone_entry = ttk.Entry (self.bill,width=20)
        self.phone_entry.grid(row = 4, column = 1) 


        
        self.address_label = Label(self.bill,text = "Address", fg = "black", padx = 30, pady = 10,
                                                            font = ("Time", '12', "bold italic"))
        self.address_label.grid(row = 5,column=0) 
        self.address_entry = ttk.Entry(self.bill,width=20)
        self.address_entry.grid(row =5,column = 1 )

        finish_button = ttk.Button(self.bill,text= "Finish",command=self.show_thank)
        finish_button.grid(row = 6,column=1)

        self.thanks = Label (self.bill,text="")
        self.thanks.grid(row = 7,columnspan=2)


        



        
              
        
        





    #function
    def close(self):
        self.welcome.grid_remove()
    def cancel_order(self):
        self.menu.grid_remove()
        self.welcome.grid()

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
            file1 = open(username_info,"r")
            verify = file1.read().splitlines()
            if password_info in verify:
                self.login.grid_remove()
                self.menu.grid()
            else:
                self.warning_label_log.configure(text = "Incorrect Password")
                self.password_entry_log.delete(0,END)
                self.password_entry_log.focus()
        else:
            self.warning_label_log.configure(text="Incorrect Username")
            self.username_entry_log.delete(0,END)
            self.password_entry_log.delete(0,END)
            self.username_entry_log.focus()

    def register_function(self): 
        try:
            if self.name_entry.get() == "": 
                self.warning_label.configure(text = "Please enter Name") 
                self.name_entry.focus() 

            elif self.name_entry.get().isalpha() == False: 
                self.warning_label.configure(text = "Pleasae enter text only") 
                self.name_entry.delete(0, END) 
                self.name_entry.focus()
            
            elif self.username_entry.get() == "": 
                self.warning_label.configure(text = "Please enter Username") 
                self.username_entry.focus() 

            elif self.username_entry.get().isalpha() == False: 
                self.warning_label.configure(text = "Pleasae enter text only") 
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
                file = open(username, "w")
                file.write(username + "\n")
                file.write(password + "\n")
                file.write(name + "")
                
                
        
        except ValueError: 
            self.warning_label.configure(text = "Please enter number only") 
            
    def return_menu(self):
        self.register.grid_remove()
        self.welcome.grid()

    def finish(self):
        a = self.food.get()
        b = self.food1.get()
        c = self.food2.get()
        d = self.food3.get()
        e = self.food4.get()
        f = self.food5.get()
        g = self.food6.get()
        x = self.drink.get()
        y = self.drink1.get()
        z = self.drink2.get()
        self.total =  (a+b+c+d+e+f+g)*10 +(x+y+z)*3
        if self.total == 0:
            self.warning_label_menu.configure(text = "You haven't order anything")
        else:        
            self.total_label.configure(text = "Total: $"+str(self.total)+".00")
            self.menu.grid_remove()
            self.bill.grid()
    
    def show_thank(self):
        try:
            if self.name_e_bill.get() == "": 
                self.thanks.configure(text = "Please enter Name",fg = "red", width =20 , padx = 30 , pady = 10) 
                self.name_e_bill.focus() 

            elif self.name_e_bill.get().isalpha() == False: 
                self.thanks.configure(text = "Pleasae enter text only",fg = "red", width =20 , padx = 30 , pady = 10) 
                self.name_e_bill.delete(0, END) 
                self.name_e_bill.focus()
            
            elif self.phone_entry.get() =="":
                self.thanks.config(text = "Please enter Phone Number",fg = "red", width =20 , padx = 30 , pady = 10)
                self.phone_entry.focus()
            
            elif self.phone_entry.get().isalpha() == True:
                self.thanks.configure(text = "Pleasae enter number only",fg = "red", width =20 , padx = 30 , pady = 10) 
                self.phone_entry.delete(0, END) 
                self.phone_entry.focus()


            elif self.address_entry.get()== "":
                self.thanks.configure(text = "Please enter Address",fg = "red", width =20 , padx = 30 , pady = 10) 
                self.name_e_bill.focus() 
            

            else:
                self.thanks.config(text="Thank You for choosing Fast Food Botany", width = 30, padx = 30, pady = 10,
                             font = ("Time", '14', "bold italic"))

                
        except ValueError: 
            self.warning_label.configure(text = "Please enter number only") 
        
        
if __name__ == "__main__":
    root = Tk()
    frames = FoodApp(root)
    root.title("App")
    root.mainloop()
