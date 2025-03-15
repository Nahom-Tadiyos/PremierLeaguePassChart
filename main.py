from customtkinter import *
import customtkinter as ct
import mplsoccer as mp
import pandas as pd



app = ct.CTk()
app.title("Soccer Pass Chart Generator")
app.geometry("700x500")
ct.set_appearance_mode("dark")

Arial = ct.CTkFont(family="Arial", size=30)
Heavitas = ct.CTkFont(family="heavitas", size=30)
HeavitasSmall = ct.CTkFont(family="heavitas", size=15)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

title = ct.CTkLabel(app, text="Soccer Pass Chart Generator",width=50, height=50, fg_color="transparent", font=Heavitas)
title.pack()

instructionsText = ct.CTkLabel(app, text="Click the button below to open a .csv file of your data", fg_color="transparent", font=HeavitasSmall)
instructionsText.pack()

app.mainloop()