import os 
import csv
import tkinter
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import E, NO, RIGHT, W, Y, PhotoImage, ttk, messagebox, END
from Window_Maker import Window_Makers
from login import Login_Window
from utils.dbconfig import dbconfig
import login
import Window_Maker
import hashlib

class Windows():

    def __init__(self):
        self.First()

    def First(self):
        Window = tk.CTk()
        WM = Window_Makers()


        def open_win2():
            self.Second_Window()

        def info():
            pass
            # try:
            #     Window.destroy()
            # except tkinter.TclError:
            #     pass

        def login():
            self.login()

        def close():
            try:
                Window.destroy()
            except tkinter.TclError:
                pass


        WM.Make_Home(Window = Window, window_title = "Password Manager", bgimg = "1stbg", text1 = "Login/Logout", text2 = "About", text3 = "Exit", text4 = "Manage Passwords", fgcolor = "#535359", hcolor = "#82828c", command1 = login, command2 = info, command3 = close, command4 = open_win2)


    def Second_Window(self):
        PM_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def add():
            self.Add_Checker()

        def retrieve():
            self.Retrieve_Checker()

        def delete():
           self.Delete_Checker()

        def deswin():
            try:
                PM_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_pm(Window = PM_Window, window_title = "Password Manager", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Add password", text2 = "Retrieve password", text3 = "Delete password", text4 = "back", command1 = add, command2 = retrieve, command3 = delete, command4 = deswin)



    def Add_Checker(self):
        Add_Check_Window = tk.CTkToplevel()

        Add_Check_Window.title("Verify")
        
        window_height = 200
        window_width = 400

        screen_width = Add_Check_Window.winfo_screenwidth()
        screen_height = Add_Check_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Add_Check_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Add_Check_Window.resizable(False, False)


        Add_Check_Window['background'] = "#82828c"



        MP = tk.CTkEntry(master = Add_Check_Window)
        MP.place(x = 50, y = 50, width = 300, height = 30)

        MP.insert(0, "Master Password")

        def on_enter(e):
            MP.delete(0, END)
        def on_leave(e):
            if MP.get() == "":
                MP.insert(0, "Master Password")

        MP.bind("<FocusIn>", on_enter)
        MP.bind("<FocusOut>", on_leave)



        def sql_login():
            with open("temp.txt", "r") as f:
                username = f.read()

            db = dbconfig()
            cursor = db.cursor()
            password = MP.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()


            query = '''use prodathon'''
            cursor.execute(query)
            print(username)
            query = "select * from  Prodathon.users where username = %s and masterkey_hash = %s"
            cursor.execute(query, [(username),(hashed_password)])
            data = cursor.fetchall()

            if data:
                deswin()
                self.Add_Window()
                

            else:
                messagebox.showerror("","Wrong Master Password")

        def deswin():
            try:
                Add_Check_Window.destroy()
            except tkinter.TclError:
                pass




        Button1 = tk.CTkButton(master = Add_Check_Window, text = "verify", text_font = ("Times New Roman", 28), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = sql_login)
        Button1.place(x = 100, y = 110, width = 200, height = 50)



        Add_Check_Window.mainloop()



    def Add_Window(self):
        AddPW_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def add():
            deswin()


        def deswin():
            try:
                AddPW_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_add(Window = AddPW_Window, window_title = "Add password", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Generate password", text2 = "Back", command1 = add, command2 = deswin)


    def Retrieve_Checker(self):
        Retrieve_Check_Window = tk.CTkToplevel()

        Retrieve_Check_Window.title("Verify")
        
        window_height = 200
        window_width = 400

        screen_width = Retrieve_Check_Window.winfo_screenwidth()
        screen_height = Retrieve_Check_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Retrieve_Check_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Retrieve_Check_Window.resizable(False, False)


        Retrieve_Check_Window['background'] = "#82828c"



        MP = tk.CTkEntry(master = Retrieve_Check_Window)
        MP.place(x = 50, y = 50, width = 300, height = 30)

        MP.insert(0, "Master Password")

        def on_enter(e):
            MP.delete(0, END)
        def on_leave(e):
            if MP.get() == "":
                MP.insert(0, "Master Password")

        MP.bind("<FocusIn>", on_enter)
        MP.bind("<FocusOut>", on_leave)



        def sql_login():
            with open("temp.txt", "r") as f:
                username = f.read()

            db = dbconfig()
            cursor = db.cursor()
            password = MP.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()


            query = '''use prodathon'''
            cursor.execute(query)
            print(username)
            query = "select * from  Prodathon.users where username = %s and masterkey_hash = %s"
            cursor.execute(query, [(username),(hashed_password)])
            data = cursor.fetchall()

            if data:
                deswin()
                self.Retrieve_Window()
                

            else:
                messagebox.showerror("","Wrong Master Password")

        def deswin():
            try:
                Retrieve_Check_Window.destroy()
            except tkinter.TclError:
                pass




        Button1 = tk.CTkButton(master = Retrieve_Check_Window, text = "verify", text_font = ("Times New Roman", 28), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = sql_login)
        Button1.place(x = 100, y = 110, width = 200, height = 50)



        Retrieve_Check_Window.mainloop()



    def Retrieve_Window(self):
        RetPW_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def retrieve():
            deswin()


        def deswin():
            try:
                RetPW_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_ret(Window = RetPW_Window, window_title = "Add password", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Generate password", text2 = "Back", command1 = retrieve, command2 = deswin)


    def Delete_Checker(self):
        Delete_Check_Window = tk.CTkToplevel()

        Delete_Check_Window.title("Verify")
        
        window_height = 200
        window_width = 400

        screen_width = Delete_Check_Window.winfo_screenwidth()
        screen_height = Delete_Check_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Delete_Check_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Delete_Check_Window.resizable(False, False)


        Delete_Check_Window['background'] = "#82828c"



        MP = tk.CTkEntry(master = Delete_Check_Window)
        MP.place(x = 50, y = 50, width = 300, height = 30)

        MP.insert(0, "Master Password")

        def on_enter(e):
            MP.delete(0, END)
        def on_leave(e):
            if MP.get() == "":
                MP.insert(0, "Master Password")

        MP.bind("<FocusIn>", on_enter)
        MP.bind("<FocusOut>", on_leave)



        def sql_login():
            with open("temp.txt", "r") as f:
                username = f.read()

            db = dbconfig()
            cursor = db.cursor()
            password = MP.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()


            query = '''use prodathon'''
            cursor.execute(query)
            print(username)
            query = "select * from  Prodathon.users where username = %s and masterkey_hash = %s"
            cursor.execute(query, [(username),(hashed_password)])
            data = cursor.fetchall()

            if data:
                deswin()
                self.Delete_Window()
                

            else:
                messagebox.showerror("","Wrong Master Password")

        def deswin():
            try:
                Delete_Check_Window.destroy()
            except tkinter.TclError:
                pass




        Button1 = tk.CTkButton(master = Delete_Check_Window, text = "verify", text_font = ("Times New Roman", 28), fg_color = "#535359", hover_color = "#82828c", bg_color = "#535359" ,command = sql_login)
        Button1.place(x = 100, y = 110, width = 200, height = 50)



        Delete_Check_Window.mainloop()



    def Delete_Window(self):
        delPW_Window = tk.CTkToplevel()

        WM = Window_Makers()


        def dell():
            deswin()


        def deswin():
            try:
                delPW_Window.destroy()
            except tkinter.TclError:
                pass

            

        WM.Make_del(Window = delPW_Window, window_title = "Add password", bgimg = "1stbg", fgcolor = "#535359", hcolor = "#82828c", text1 = "Generate password", text2 = "Back", command1 = dell, command2 = deswin)







    def info_Window(self):
        pass

    def login(self):
        LWIN = tk.CTkToplevel()
        WM = Login_Window()
        WM.Make_Win(Window = LWIN, window_title = "Login", bgimg = "1stbg")




Window = Windows()