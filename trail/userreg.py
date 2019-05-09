from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
#import tkMessageBox as tm
import os
import mysql.connector
#from tkinter import messagebox

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="project")
mycursor = mydb.cursor()



class LoginFrame(Frame):
    def __init__(self, master):
        #super().__init__(master)

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

        submenu6=Menu(menu)
        menu.add_cascade(label="Back",command =self.exit)

        def registration():
            name=entry_name.get()
            age=entry_age.get()
            phno=entry_phno.get()
            emailid=entry_emailid.get()
            fbid=entry_fbid.get()
            username=entry_username.get()
            password=entry_password.get()
            '''global selection
            selection=var.get()

            if selection == 1:
                    gender="Male"
            elif selection == 2:
                    gender="Female"
            else:
                    print("No such Parameter")'''
            
            add_user = ("INSERT INTO user "
                        "(username,password,name,age,phno,emailid,fbid)"
                        "values(%s,%s,%s,%s,%s,%s,%s)")
            user_data = (username,password,name,age,phno,emailid,fbid)
            mycursor.execute(add_user, user_data)   
            mydb.commit()
            r = Tk()
            r.title(' '+username)
            r.geometry('700x500')

            menu=Menu(r)
            r.config(menu=menu)
            submenu=Menu(menu)
            menu.add_cascade(label="Home",menu=submenu)
            submenu.add_command(label="User Details",command ="")
            submenu.add_separator()
            submenu.add_command(label=" ",command ="")

            newmenu=Menu(menu)
            menu.add_cascade(label="Logout",command =self.exit)              
            rlbl = Label(r, text='\n Welcome '+username)
            rlbl.pack()
            r.mainloop()
        
        #label_text.grid(row=0,sticky=E)
        label_name = Label(root, text="Name")
        label_name.grid(row=2,)
        entry_name = Entry(root)
        entry_name.grid(row=2,column=1)

        label_age = Label(root, text="Age")
        label_age.grid(row=3,)
        entry_age = Entry(root)
        entry_age.grid(row=3,column=1)

        label_phno = Label(root, text="PhoneNo")
        label_phno.grid(row=4,)
        entry_phno = Entry(root)
        entry_phno.grid(row=4,column=1)

        label_emailid = Label(root, text="EmailID")
        label_emailid.grid(row=5,)
        entry_emailid = Entry(root)
        entry_emailid.grid(row=5,column=1)

        label_fbid = Label(root, text="Facebook ID")
        label_fbid.grid(row=6,)
        entry_fbid = Entry(root)
        entry_fbid.grid(row=6,column=1)

        '''label_gender = Label(root, text="Gender")
        label_gender.grid(row=4,)
        var = IntVar()
        Radiobutton(root,text="Male",padx=5,variable=var,value="1").grid(row=4,column=1)
        Radiobutton(root,text="Female",padx=20,variable=var,
                    value="2").grid(row=4,column=2)'''

        label_username = Label(root, text="Username")
        label_username.grid(row=7, )
        entry_username = Entry(root)
        entry_username.grid(row=7, column=1)

        label_password = Label(root, text="Password")
        label_password.grid(row=8, )
        entry_password = Entry(root, show="*")
        entry_password.grid(row=8, column=1)

        logbtn_user = Button(root, text="Sign-In",command=registration) 
        logbtn_user.grid(row=10, columnspan=2,)

    def exit(self):
        os.system("main_login.py")
    def doNothing(self):
        print("ok")
            
root = tk.Tk()
root.geometry('700x300')
root.title("User Registration")
lf = LoginFrame(root)
root.mainloop()
