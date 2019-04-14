from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox
import mysql.connector
import mainWindow
import receiveDat

StoreMain=Tk()
StoreMain.geometry("1280x720")
StoreMain.focus_force()
StoreMain.resizable(0,0)
StoreMain.title("PharmaDB Store")

mainWindow.LoginScreen(StoreMain)

StoreMain.mainloop()