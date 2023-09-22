import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk()
root.iconbitmap("warning_small.ico")
root.title('Commercial Alert')

riot_imf                    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\riotup.png")) 

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=570, width=230,)
canvas.grid(column=0, row=0, sticky=W)
canvas.create_image((0, 0), image=riot_imf, anchor=NW)

# Enter event loop
root.mainloop()