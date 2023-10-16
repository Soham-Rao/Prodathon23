import os 
import csv
import tkinter
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import E, NO, RIGHT, W, Y, PhotoImage, ttk, messagebox, END
from Window_Maker import Window_Maker
from login import Login_Window


class Windows():

    def __init__(self):
        self.First()

    def First(self):
        Window = tk.CTk()
        First_Window = Window_Maker()


        def open_win2():
            pass
            # try:
            #     Window.destroy()
            # except tkinter.TclError:
            #     pass

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


        First_Window.Make_Home(Window = Window, window_title = "Password Manager", bgimg = "1stbg", text1 = "Login/Logout", text2 = "About", text3 = "Exit", text4 = "Manage Passwords", fgcolor = "#535359", hcolor = "#82828c", command1 = login, command2 = open_win2, command3 = close, command4 = open_win2)


    def Second_Window(self):
        pass

    def info_Window(self):
        pass

    def login(self):
        LWIN = tk.CTkToplevel()
        Fifth_Window = Login_Window()
        Fifth_Window.Make_Win(Window = LWIN, window_title = "Login", bgimg = "1stbg")




Window = Windows()