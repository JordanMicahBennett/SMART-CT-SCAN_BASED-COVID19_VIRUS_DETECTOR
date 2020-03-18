#Author: Jordan Bennett
#Note: Simple ui to use Ai based coronavirus2019/covid19 diagnosis tool

import covid19_ai_diagnoser

from tkinter import Frame, Tk, BOTH, Label, Menu, filedialog, messagebox
from PIL import Image, ImageTk

import os
import codecs

screenWidth = "1560"
screenHeight = "840"
windowTitle = "Smart/Ai Coronavirus 2019 (Covid19) Diagnosis Tool"

import cv2

class Window(Frame):
    _PRIOR_IMAGE = None
    #establish variable to keep track of images added to Frame, for purpose of preventing stacking @ new image additions
    #by using destroy() on each old image instance @ addition
	#Added by Jordan Bennett, based on suggestion by Andrei Marinescu, who suggested that xray images should not stack as new ones are loaded. (https://www.facebook.com/mvandrei)
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("covid19_ai_diagnoser_default__.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=(int(screenWidth)/2)-load.width/2, y=((int(screenHeight)/2))-load.height/2)
        self._PRIOR_IMAGE = img #setup prior image instance


        
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
def loadRegularPneumoniaImageFromDialog():
    currdir = os.getcwd()
    image_file = filedialog.askopenfile(mode ='r', parent=root, initialdir=currdir, title='Please select an Xray Image of suspected regular pneumonia case:')
    root.wm_title(windowTitle + " : " + image_file.name)
    loadRegularPneumoniaImageFromName(image_file.name)

def loadRegularPneumoniaImageFromName(filename):
    app._PRIOR_IMAGE.destroy() #destroy old image
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=(int(screenWidth)/2)-load.width/2, y=((int(screenHeight)/2))-load.height/2)
    outputContent = "#############################################\n" + filename+"\n\n"
    outputContent += covid19_ai_diagnoser.doOnlineInference_regularPneumonia (filename)
    print(outputContent)
    app._PRIOR_IMAGE = img #set latest instance of old image
    messagebox.showinfo(title=windowTitle + " : Result ", message=outputContent)


def loadCovid19ImageFromDialog():
    currdir = os.getcwd()
    image_file = filedialog.askopenfile(mode ='r', parent=root, initialdir=currdir, title='Please select an Xray Image of suspected coronavirus2019 case:')
    root.wm_title(windowTitle + " : " + image_file.name)
    loadCovid19ImageFromName(image_file.name)

def loadCovid19ImageFromName(filename):
    app._PRIOR_IMAGE.destroy() #destroy old image
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=(int(screenWidth)/2)-load.width/2, y=((int(screenHeight)/2))-load.height/2)
    outputContent = "#############################################\n" + filename+"\n\n"
    outputContent += covid19_ai_diagnoser.doOnlineInference_covid19Pneumonia (filename)
    print(outputContent)
    app._PRIOR_IMAGE = img #set latest instance of old image
    messagebox.showinfo(title=windowTitle + " : Result ", message=outputContent)
    

# Adding a load image button to the cascade menu "File"
filemenu.add_command(label="Load Regular Pnuemonia image", command=loadRegularPneumoniaImageFromDialog)
filemenu.add_command(label="Load Covid19 Pneumonia image", command=loadCovid19ImageFromDialog)

############
#root cycle
root.config(menu=menubar)
root.mainloop()
