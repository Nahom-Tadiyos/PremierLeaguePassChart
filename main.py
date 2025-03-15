from customtkinter import *
import customtkinter as ct
import mplsoccer as mp
import pandas as pd
from tkinter import filedialog

app = ct.CTk()
app.title("Soccer Pass Chart Generator")
app.geometry("700x500")
ct.set_appearance_mode("dark")

Arial = ct.CTkFont(family="Arial", size=10)
Heavitas = ct.CTkFont(family="heavitas", size=30)
HeavitasSmall = ct.CTkFont(family="heavitas", size=12)

filename = "No file uploaded"

def openFile():
    global filename
    filename = filedialog.askopenfilename()
    filenameText.configure(text=filename if filename else "No file uploaded")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

title = ct.CTkLabel(app, text="Soccer Pass Chart Generator", width=50, height=50, fg_color="transparent", font=Heavitas)
title.pack()

instructionsText = ct.CTkLabel(app, text="Click the button below to open a .csv file of your data", fg_color="transparent", font=HeavitasSmall)
instructionsText.pack()

openFileBtn = ct.CTkButton(app, text="Open file", width=80, height=50, command=openFile)
openFileBtn.pack()

filenameText = ct.CTkLabel(app, text=filename, font=Arial, fg_color="transparent")
filenameText.pack()

app.mainloop()
