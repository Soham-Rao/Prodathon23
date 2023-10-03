import os 
import csv
import tkinter
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import E, NO, RIGHT, W, Y, PhotoImage, ttk, messagebox, END
from Window_Maker import Window_Maker



class Windows():

    def __init__(self):
        self.First()

    def First(self):
        Window = tk.CTk()

        First_Window = Window_Maker()

        First_Window.Make_Win(Window = Window, window_title = "Password Manager", bgimg = "1stbg", text1 = "Login/Logout", text2 = "Games", text3 = "Info", text4 = "Exit", fgcolor = "#9532a8", hcolor = "#b55bc7", command1 = None, command2 = None, command3 = None, command4 = None)


Window = Windows()