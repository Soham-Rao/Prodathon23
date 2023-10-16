import os
import tkinter 
from PIL import Image, ImageTk
from tkinter import PhotoImage, ttk, messagebox, END, INSERT

import customtkinter as tk


PW = None


class Window_Makers():

    def __init__(self):
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")



    def Make_Home(self, Window, window_title, bgimg, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4):


        def home_buttons(Window, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4):
            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 510, y = 170, width = 350, height = 70)

            Button2 = tk.CTkButton(master = Window, text = text2, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2)
            Button2.place(x = 510, y = 450, width = 350, height = 70)

            Button4 = tk.CTkButton(master = Window, text = text4, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor, command = command4)
            Button4.place(x = 510, y = 310, width = 350, height = 70)


            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button3 = tk.CTkButton(master = Window, text = text3, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command3, image = button_img, compound = "left")
            Button3.place(x = 10, y = 10, width = 121, height = 50)


        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        home_buttons(Window, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4)

        Window.mainloop()




    def Make_pm(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, text3, text4,  command1, command2, command3, command4):
        
        def pm_buttons(Window, fgcolor, hcolor, text1, text2, text3, text4,  command1, command2, command3, command4):
            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 510, y = 170, width = 350, height = 70)

            Button2 = tk.CTkButton(master = Window, text = text2, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2)
            Button2.place(x = 510, y = 310, width = 350, height = 70)

            Button3 = tk.CTkButton(master = Window, text = text3, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor, command = command3)
            Button3.place(x = 510, y = 450, width = 350, height = 70)

            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button4 = tk.CTkButton(master = Window, text = text4, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command4, image = button_img, compound = "left")
            Button4.place(x = 10, y = 10, width = 121, height = 50)



        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        pm_buttons(Window,fgcolor, hcolor, text1, text2, text3, text4, command1, command2, command3, command4)

        Window.mainloop()





    def Make_add(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, command1, command2):
        
        def add_widgets(Window, fgcolor, hcolor, text1, text2, command1, command2):

###            
            sitename_Entry = tk.CTkEntry(master = Window)
            sitename_Entry.place(x = 460, y = 100, width = 300, height = 30)

            sitename_Entry.insert(0, "Site name")

            def on_enter(e):
                sitename_Entry.delete(0, END)
            def on_leave(e):
                if sitename_Entry.get() == "":
                    sitename_Entry.insert(0, "Site name")

            sitename_Entry.bind("<FocusIn>", on_enter)
            sitename_Entry.bind("<FocusOut>", on_leave)

###
            siteurl_Entry = tk.CTkEntry(master = Window)
            siteurl_Entry.place(x = 460, y = 150, width = 300, height = 30)

            siteurl_Entry.insert(0, "Site URL")

            def on_enter(e):
                siteurl_Entry.delete(0, END)
            def on_leave(e):
                if siteurl_Entry.get() == "":
                    siteurl_Entry.insert(0, "Site URL")

            siteurl_Entry.bind("<FocusIn>", on_enter)
            siteurl_Entry.bind("<FocusOut>", on_leave)

###
            email_Entry = tk.CTkEntry(master = Window)
            email_Entry.place(x = 460, y = 200, width = 300, height = 30)

            email_Entry.insert(0, "Email")

            def on_enter(e):
                email_Entry.delete(0, END)
            def on_leave(e):
                if email_Entry.get() == "":
                    email_Entry.insert(0, "Email")

            email_Entry.bind("<FocusIn>", on_enter)
            email_Entry.bind("<FocusOut>", on_leave)

###
            siteusername_Entry = tk.CTkEntry(master = Window)
            siteusername_Entry.place(x = 460, y = 250, width = 300, height = 30)

            siteusername_Entry.insert(0, "Site Username")

            def on_enter(e):
                siteusername_Entry.delete(0, END)
            def on_leave(e):
                if siteusername_Entry.get() == "":
                    siteusername_Entry.insert(0, "Site Username")

            siteusername_Entry.bind("<FocusIn>", on_enter)
            siteusername_Entry.bind("<FocusOut>", on_leave)

###
            sitepassword_Entry = tk.CTkEntry(master = Window)
            sitepassword_Entry.place(x = 460, y = 300, width = 300, height = 30)

            sitepassword_Entry.insert(0, "Site Password")

            def on_enter(e):
                sitepassword_Entry.delete(0, END)
            def on_leave(e):
                if sitepassword_Entry.get() == "":
                    sitepassword_Entry.insert(0, "Site Password")

            sitepassword_Entry.bind("<FocusIn>", on_enter)
            sitepassword_Entry.bind("<FocusOut>", on_leave)

###

            Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
            Button1.place(x = 441, y = 420, width = 350, height = 70)

            img = Image.open(os.path.join("imgs","back_button.png"))
            img = img.resize((50,50), resample = 0)
            button_img = ImageTk.PhotoImage(img)       

            Button2 = tk.CTkButton(master = Window, text = text2, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2, image = button_img, compound = "left")
            Button2.place(x = 10, y = 10, width = 121, height = 50)


        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        add_widgets(Window,fgcolor, hcolor, text1, text2, command1, command2)

        Window.mainloop()




    def Make_ret(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, command1, command2):
        
        def ret_widgets(Window, fgcolor, hcolor, text1, text2, command1, command2):
            pass

        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        ret_widgets(Window,fgcolor, hcolor, text1, text2, command1, command2)

        Window.mainloop()



    def Make_del(self, Window, window_title, bgimg, fgcolor, hcolor, text1, text2, command1, command2):
        
        def del_widgets(Window, fgcolor, hcolor, text1, text2, command1, command2):
            pass

        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        del_widgets(Window,fgcolor, hcolor, text1, text2, command1, command2)

        Window.mainloop()
