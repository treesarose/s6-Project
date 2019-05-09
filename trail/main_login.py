from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import pymysql
import os
from tkinter import messagebox
#from PIL import Image, ImageTk

mydb = pymysql.connect(host="localhost", user="root", passwd="", database="project")
mycursor = mydb.cursor()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        menu=Menu(root)
        root.config(menu=menu)
        submenu1=Menu(menu)
        menu.add_cascade(label="Route",menu=submenu1)
        submenu1.add_command(label="User Login",command = self.doNothing)

        submenu2=Menu(menu)
        menu.add_cascade(label="Accomadation",menu=submenu2)
        submenu2.add_command(label="Hotels",command = self.doNothing)
        submenu2.add_command(label="Resorts",command = self.doNothing)
        submenu2.add_command(label="Home Stays",command = self.doNothing)

        submenu3=Menu(menu)
        menu.add_cascade(label="Resturants",menu=submenu3)
        submenu3.add_command(label="Vegitarian",command = self.doNothing)
        submenu3.add_command(label="Non-Vegitarian",command = self.doNothing)
        submenu3.add_command(label="Multi-Cusine",command = self.doNothing)
        submenu3.add_command(label="Others",command = self.doNothing)

        submenu4=Menu(menu)
        menu.add_cascade(label="Activities",menu=submenu4)
        submenu4.add_command(label="Adventure",command = self.doNothing)
        submenu4.add_command(label="Trekking",command = self.doNothing)
        submenu4.add_command(label="Water-Sports",command = self.doNothing)

        submenu5=Menu(menu)
        menu.add_cascade(label="Travel Dairy",command = self.doNothing)


        self.label_text = Label(self, text=" ")
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_text.grid(row=0,sticky=E)
        self.label_username.grid(row=2, )
        self.label_password.grid(row=3, )
        self.entry_username.grid(row=2, column=1)
        self.entry_password.grid(row=3, column=1)

        self.logbtn_user = Button(self, text="Sign In", command=self.user_home) 
        self.logbtn_user.grid(row=7, columnspan=2,sticky=E)

        self.regbtn_user = Button(self, text="Sign Up", command=self.register_btn_clicked)
        self.regbtn_user.grid(row=7, columnspan=2)

        self.pack()

    def _login_btn_clicked(window):

        r = Tk() # Opens new window
            #r.title(admin_name+ 'Administrator')
        r.geometry('1050x650')

        menu=Menu(r)
        r.config(menu=menu)
        submenu=Menu(menu)
        menu.add_cascade(label="Home",menu=submenu)
        submenu.add_command(label="User Details",command ="")
        submenu.add_separator()
        submenu.add_command(label=" ",command ="")

        newmenu=Menu(menu)
        menu.add_cascade(label="Profile",menu=newmenu)
        newmenu.add_command(label="Logout",command ="self.adminLogin")
        
        rlbl = Label(r, text='\n Welcome Administrator') 
        rlbl.pack()
        r.mainloop()
        '''else:
            tm.showerror("Login error", "Incorrect username")'''


    def register_btn_clicked(self):
        os.system("userreg.py")

    def user_home(self):
        #os.system("userhome.py")

        username = self.entry_username.get()
        password = self.entry_password.get()
        # print(username, password)
        sql3 = "SELECT * FROM user WHERE username = %s and password=%s"
        #p1 = Page1(self)
        login = (username,password,)
        mycursor.execute(sql3, login)
        myresult = mycursor.fetchall()
        validate=len(myresult)
        if validate==1:
            for x in myresult:
                user_id=x[0]
                user_name=x[1]
            r = Tk() # Opens new window
            r.title('Welcome '+user_name)
            r.geometry('1050x650') # Makes the window a certain size

            menu=Menu(r)
            r.config(menu=menu)
            submenu=Menu(menu)
            menu.add_cascade(label="User Details",command =self.doNothing)
            submenu.add_separator()
            submenu.add_command(label=" ",command ="")

            newmenu=Menu(menu)
            menu.add_cascade(label="Logout",command =self.login)             
            rlbl = Label(r, text='\n Welcome '+username)
            rlbl.pack()
            r.mainloop()
        else:
            tm.showerror("Login error", "Incorrect username")


    def doNothing(self):
        print("ok")

    def adminLogin(self):

        window = tk.Tk()
        window.geometry('500x450')
        window.title("Admin Login")
        
        menu=Menu(window)
        window.config(menu=menu)
        submenu=Menu(menu)
        menu.add_cascade(label="Home",menu=submenu)
        submenu.add_command(label="",command = "")
        submenu.add_separator()
        submenu.add_command(label="Exit",command ="")

        window.labelt = Label(window, text="Admin Login")
        window.labelu = Label(window, text="Username")
        window.labelp = Label(window, text="Password")

        window.entryu = Entry(window)
        window.entryp = Entry(window, show="*")
        
        window.labelt.grid(row=0,sticky=E)
        window.labelu.grid(row=2, )
        window.labelp.grid(row=3, )
        window.entryu.grid(row=2, column=1)
        window.entryp.grid(row=3, column=1)

        

        window.checkbox = Checkbutton(window, text="Keep me logged in")
        window.checkbox.grid(row=5, columnspan=2)

        

        window.logbtn_admin = Button(window, text="Admin Login",
                                     command=self._login_btn_clicked)
        window.logbtn_admin.grid(row=7)


root = tk.Tk()
root.geometry('700x500')
root.title("Login")
lf = LoginFrame(root)
root.mainloop()
