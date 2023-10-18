from utils.dbconfig import dbconfig
from utils.new_user import new_user

import os
import tkinter
import hashlib
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import END, INSERT, PhotoImage, ttk, messagebox

#from Window_Maker import Window_Maker

Current_user = None
        

class Login_Window():
    def __init__(self):
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")
        # self.windowmaker = Window_maker()

    def Make_Win(self, Window, window_title, bgimg):

        Window.title(window_title)

        window_height = 360
        window_width = 640

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        global bg_img

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)


        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        self.widgetmaker(Window, bgimg)

        Window.mainloop()


    def widgetmaker(self, Window, bgimg):
        user_Entry = tk.CTkEntry(master = Window, fg_color = "#adffff", border_color = "#00ffff", text_color = "#000000")
        user_Entry.place(x = 163, y = 70, width = 320, height = 30)

        user_Entry.insert(0, "Username")

        def on_enter(e):
            user_Entry.delete(0, END)
        def on_leave(e):
            if user_Entry.get() == "":
                user_Entry.insert(0, "Username")

        user_Entry.bind("<FocusIn>", on_enter)
        user_Entry.bind("<FocusOut>", on_leave)

        pass_Entry = tk.CTkEntry(master = Window, fg_color = "#adffff", border_color = "#00ffff", text_color = "#000000", show = "*")
        pass_Entry.place(x = 163, y = 120, width = 320, height = 30)

        pass_Entry.insert(0, "Password")

        def on_enter(e):
            pass_Entry.delete(0, END)
        def on_leave(e):
            if pass_Entry.get() == "":
                pass_Entry.insert(0, "Password")

        pass_Entry.bind("<FocusIn>", on_enter)
        pass_Entry.bind("<FocusOut>", on_leave)

        def on_enter_press(e):
            sql_login()

        Window.bind("<Return>", on_enter_press)

        def sql_login():
            db = dbconfig()
            cursor = db.cursor()
            username = user_Entry.get()
            password = pass_Entry.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()


            query = '''use prodathon'''
            cursor.execute(query)
            query = "select * from  Prodathon.users where username = %s and masterkey_hash = %s"
            cursor.execute(query, [(username),(hashed_password)])
            data = cursor.fetchall()

            if data:
                deswin()
                messagebox.showinfo("","Login Success")
                db.close()
                
                with open ("temp1.txt", "w") as f:
                    f.write(username)

                
                
            else:
                messagebox.showerror("","Incorrect Username or Password")
                db.close()
                user_Entry.delete(0, END)
                pass_Entry.delete(0, END)


        def deswin():
            try:
                Window.destroy()
            except tkinter.TclError:
                pass

        def register():
            deswin()
            self.reg_window(bgimg)
            


        def logoff():
            try:
                Window.destroy()
            except tkinter.TclError:
                pass
            with open ("temp1.txt", "w") as f:
                f.write("None")
            messagebox.showinfo("","You have successfully logged out")


        #images
        img1 = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img1 = img1.resize((20,20), resample = 0)
        button_img = ImageTk.PhotoImage(img1)

        img2 = Image.open(os.path.join("imgs","back_button.png"))
        #img2.save(os.path.join("imgs","back_button.png"))
        img2 = img2.resize((17,25), resample = 0)
        logout_img = ImageTk.PhotoImage(img2)

        #buttons
        login_button = tk.CTkButton(master = Window, text = "Login", text_font = ("Cascadia Code SemiBold", 15), text_color = "#000000", fg_color = "#50bdcc", hover_color = "#63ecff", border_color = "#50bdcc", command = sql_login)
        login_button.place(x = 270, y = 170, width = 100, height = 50)

        reg_question = tk.CTkLabel(master = Window, text = "Dont have an account yet?",text_font = ("Calibri", 13),  fg_color = "#5c5c63")
#       reg_question.place(x = 210, y = 280, width = 200, height = 20)

        register_button = tk.CTkButton(master = Window, text = "Register", text_font = ("Cascadia Code SemiBold", 15), text_color = "#000000", fg_color = "#50bdcc", hover_color = "#63ecff", border_color = "#50bdcc", command = register)
        register_button.place(x = 264, y = 240, width = 110, height = 50)

  
        logout_button = tk.CTkButton(master = Window, text = "Logout", text_color = "black", text_font = ("Cascadia Code SemiBold", 10), fg_color = "#50bdcc", hover_color = "#63ecff", border_color = "#50bdcc" ,command = logoff, image = logout_img, compound = "right")
        logout_button.place(x = 20, y = 8, width = 100, height = 30)


    def reg_window(self, bgimg):
        register_Window = tk.CTkToplevel()
        register_Window.title("Register")

        window_height = 360
        window_width = 640

        screen_width = register_Window.winfo_screenwidth()
        screen_height = register_Window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        register_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        register_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)


        background = tk.CTkLabel(master = register_Window, image = bg_img)
        background.place(x = 0, y = 0)




        ruser_Entry = tk.CTkEntry(master = register_Window, fg_color = "#adffff", border_color = "#00ffff", text_color = "#000000")
        ruser_Entry.place(x = 163, y = 50, width = 320, height = 30)

        ruser_Entry.insert(0, "Username")

        #binds
        def on_enter(e):
            ruser_Entry.delete(0, END)
        def on_leave(e):
            if ruser_Entry.get() == "":
                ruser_Entry.insert(0, "Username")

        ruser_Entry.bind("<FocusIn>", on_enter)
        ruser_Entry.bind("<FocusOut>", on_leave)


        rpass_Entry = tk.CTkEntry(master = register_Window, fg_color = "#adffff", border_color = "#00ffff", text_color = "#000000")
        rpass_Entry.place(x = 163, y = 100, width = 320, height = 30)

        rpass_Entry.insert(0, "MASTER Password")

        def on_enter(e):
            rpass_Entry.delete(0, END)
        def on_leave(e):
            if rpass_Entry.get() == "":
                rpass_Entry.insert(0, "MASTER Password")

        rpass_Entry.bind("<FocusIn>", on_enter)
        rpass_Entry.bind("<FocusOut>", on_leave)

        re_pass_Entry = tk.CTkEntry(master = register_Window, fg_color = "#adffff", border_color = "#00ffff", text_color = "#000000")
        re_pass_Entry.place(x = 163, y = 150, width = 320, height = 30)

        re_pass_Entry.insert(0, "Re-Enter Password")

        def on_enter(e):
            re_pass_Entry.delete(0, END)
        def on_leave(e):
            if re_pass_Entry.get() == "":
                re_pass_Entry.insert(0, "Re-Enter Password")

        re_pass_Entry.bind("<FocusIn>", on_enter)
        re_pass_Entry.bind("<FocusOut>", on_leave)

        def on_enter_press(e):
            sql_register()

        register_Window.bind("<Return>", on_enter_press)

        def destroy():
            register_Window.destroy()
  
        def sql_register():
            db = dbconfig()
            cursor = db.cursor()
            username = ruser_Entry.get()
            password = rpass_Entry.get()
            re_enter = re_pass_Entry.get()

            if password == re_enter and len(password) > 4:
                new_user(username, password)
                messagebox.showinfo("","Registered Successfully\nLogin with your details")
                ruser_Entry.delete(0, END)
                rpass_Entry.delete(0, END)
                re_pass_Entry.delete(0, END)
                deswin()
                
            else:
                messagebox.showerror("","Password doesn't match confirmation password or too small")
                deswin()
                



        def deswin():
            try:
                register_Window.destroy()
            except tkinter.TclError:
                pass

        #images
        img = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img = img.resize((20,20), resample = 0)
        button_img = ImageTk.PhotoImage(img)

        #buttons
        register_button_2 = tk.CTkButton(master = register_Window, text = "Register", text_font = ("Cascadia Code SemiBold", 15), text_color = "#000000", fg_color = "#50bdcc", hover_color = "#63ecff", border_color = "#50bdcc", command = sql_register)
        register_button_2.place(x = 270, y = 200, width = 110, height = 50)

        login_question = tk.CTkLabel(master = register_Window, text = "Already have an account?",text_font = ("Calibri", 13), fg_color = "#5c5c63")
#       login_question.place(x = 205, y = 270, width = 200, height = 20)

        login_button = tk.CTkButton(master = register_Window, text = "Login", text_font = ("Cascadia Code SemiBold", 15), text_color = "#000000", fg_color = "#50bdcc", hover_color = "#63ecff", border_color = "#50bdcc", command = lambda:destroy())
#       login_button.place(x = 243, y = 300, width = 100, height = 50)

 
        register_Window.mainloop()


