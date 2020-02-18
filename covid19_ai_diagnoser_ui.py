#Author: Jordan Bennett
#Note: Simple ui to use Ai based coronavirus2019/covid19 diagnosis tool

import covid19_ai_diagnoser

from tkinter import Frame, Tk, BOTH, Label, Menu, filedialog
from PIL import Image, ImageTk

import os
import codecs

screenWidth = "1200"
screenHeight = "800"
windowTitle = "Smart/Ai Coronavirus 2019 (Covid19) Diagnosis Tool"


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("covid19_ai_diagnoser_default__.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=(int(screenWidth)/2)-load.width/2, y=((int(screenHeight)/2))-load.height/2)


        
root = Tk()
app = Window(root)




############
#screen window size, window title
root.wm_title(windowTitle)
root.geometry(screenWidth + "x" + screenHeight)

############
#menu bar
menubar = Menu(root)

# Adding a cascade to the menu bar:
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Files", menu=filemenu)

# Defining function to trigger file browser
def loadImageFromDialog():
    currdir = os.getcwd()
    image_file = filedialog.askopenfile(mode ='r', parent=root, initialdir=currdir, title='Please select a CT Image of suspected coronavirus2019 case:')
    root.wm_title(windowTitle + " : " + image_file.name)
    loadImageFromName(image_file.name)

def loadImageFromName(filename):
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=(int(screenWidth)/2)-load.width/2, y=((int(screenHeight)/2))-load.height/2)
    print("######################\n") 
    print(filename+"\n") #Print active filename before prediction
    covid19_ai_diagnoser.doOnlineInference (filename)

# Adding a load image button to the cascade menu "File"
filemenu.add_command(label="Load an image", command=loadImageFromDialog)



############
#root cycle
root.config(menu=menubar)
root.mainloop()
