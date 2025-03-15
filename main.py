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

title = ct.CTkLabel(app, text="Soccer Pass Chart Generator", font=Heavitas, fg_color="transparent")
title.pack(pady=(30, 10))

instructionsText = ct.CTkLabel(app, text="Click the button below to open a .csv file of your data", font=HeavitasSmall, fg_color="transparent")
instructionsText.pack(pady=(10, 10))

openFileBtn = ct.CTkButton(app, text="Open file", width=200, height=50, command=openFile)
openFileBtn.pack(pady=(10, 10))

filenameText = ct.CTkLabel(app, text=filename, font=Arial, fg_color="transparent")
filenameText.pack(pady=(10, 20))

app.mainloop()
