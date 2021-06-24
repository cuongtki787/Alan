from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class FoodApp :
    def __init__(self,parent):

        self.Welcome = Frame(parent)
        self.Welcome.pack()

        self.TitleLabel = Label(self.Welcome,text = "Welcome to Fast Food Botany",
                                 bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                 font = ("Time", '14', "bold italic")) 
        self.TitleLabel.pack(fill= X)
        my_img = ImageTk.PhotoImage(Image.open("C:\Foodpic\chicken.png"))
        self.myLabel = Label (self.Welcome, image= my_img)
        self.myLabel.pack()
        self.myLabel.place(height = 100,width=100,x= 200, y =200 )


        
        
if __name__ == "__main__":
    root = Tk()
    frames = FoodApp(root)
    root.title("App")
    root.mainloop()
