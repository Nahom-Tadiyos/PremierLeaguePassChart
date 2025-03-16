from customtkinter import *
import customtkinter as ct
from mplsoccer import *
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
from PIL import Image
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg


app = ct.CTk()
app.title("Soccer Pass Chart Generator")
app.geometry("700x500")
app.iconbitmap("logo.ico")
ct.set_appearance_mode("dark")

Arial = ct.CTkFont(family="Arial", size=10)
Heavitas = ct.CTkFont(family="heavitas", size=30)
HeavitasSmall = ct.CTkFont(family="heavitas", size=12)


filename = "No file uploaded"
insert = None
data = None

def openFile():
    global filename, data
    filename = filedialog.askopenfilename()
    if filename.endswith('.csv'):
        data = pd.read_csv(filename)
        filenameText.configure(text=filename if filename else "No file uploaded")
    else:
        filenameText.configure(text="Please upload a CSV file.")

def graph():
    global data, insert

    if data is None:
        filenameText.configure(text="Please upload a CSV file first.")
        return

    try:
        data.columns = data.columns.str.strip().str.lower()

        if 'x' not in data.columns or 'y' not in data.columns:
            filenameText.configure(text="CSV must contain 'x' and 'y' columns for plotting.")
            return

        fig, ax = plt.subplots(figsize=(13, 8.5))
        fig.set_facecolor('#22312b')
        ax.patch.set_facecolor('#22312b')

        pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
        pitch.draw(ax=ax)

        plt.gca().invert_yaxis()

        x = data['x']
        y = data['y']

        x_normalized = (x - x.min()) / (x.max() - x.min()) * 120
        y_normalized = (y - y.min()) / (y.max() - y.min()) * 80

        plt.scatter(x_normalized, y_normalized, s=100, c='#ea6969', alpha=.7)

        ax.set_xlim([0, 120])
        ax.set_ylim([0, 80])

        canvas = FigureCanvasAgg(fig)
        buf = BytesIO()
        canvas.print_png(buf)
        buf.seek(0)
        insert = Image.open(buf)

        plt.show()

    except Exception as e:
        filenameText.configure(text=f"Error generating graph: {e}")

def saveImage():
    global insert

    if insert is None:
        filenameText.configure(text="No graph to save. Generate a graph first.")
        return

    filename = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG file", "*.png")],
        title="Choose filename",
    )
    if filename:
        insert.save(filename)

title = ct.CTkLabel(app, text="Soccer Shot Chart Generator", font=Heavitas, fg_color="transparent")
title.pack(pady=(30, 10))

instructionsText = ct.CTkLabel(app, text="Click the button below to open a .csv file of your data", font=HeavitasSmall, fg_color="transparent")
instructionsText.pack(pady=(10, 10))

filenameText = ct.CTkLabel(app, text=filename, font=Arial, fg_color="transparent")
filenameText.pack(pady=(10, 10))

openFileBtn = ct.CTkButton(app, text="Open file", width=200, height=50, command=openFile, fg_color="#e47c7c", hover_color="#d96b6b")
openFileBtn.pack(pady=(10, 20))

graphBtn = ct.CTkButton(app, text="Graph", width=200, height=50, command=graph, fg_color="#e47c7c", hover_color="#d96b6b")
graphBtn.pack(pady=(10, 20))

saveImgBtn = ct.CTkButton(app, text="Save as PNG", width=200, height=50, command=saveImage, fg_color="#e47c7c", hover_color="#d96b6b")
saveImgBtn.pack(pady=(10,20))

app.mainloop()
