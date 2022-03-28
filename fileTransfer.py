





from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd    #lets you use files
 

class ParentWindow(Frame):

    #definitions==============================================================
    def close(self):
        self.master.destroy()   #closes window

    def getPath1(self):         #opens file manager and stores file path
        path1 = fd.askdirectory()
        self.vartxt1.delete(0,END)
        self.vartxt1.insert(0, path1)

    def __init__(self, master, *args, **kwargs):    #initalizes Frame
        Frame.__init__(self, master, *args, **kwargs)

    

        #defining master frame config
        self.master = master
        self.master.geometry('{}x{}'.format(450, 200))
        self.master.config(bg = 'lightgray')

        #Variables========================================================
        path1 = self.getPath1
        path2 = fd.askopenfilename

        #blank space
        self.blank = Label(self.master, text='', bg='lightgray')
        self.blank.grid(row=0, column=0)

        #Buttons==========================================================
        
        #browse button 1
        self.btn1 = Button(self.master, text='Browse', width=10, height=1, command=self.getPath1)
        self.btn1.grid(row=1, column=0, padx=10, pady=10, sticky=N+W)

        #browse button 2
        self.btn2 = Button(self.master, text='Browse', width=10, height=1, command=path2)
        self.btn2.grid(row=2, column=0, padx=10, pady=5, sticky=N+W)

        #Check for files==================================================

        #button
        self.btn3 = Button(self.master, text='Check for files', width=10, height=2)
        self.btn3.grid(row=3, column=0, padx=3, pady=10)


        #Close program====================================================

        self.btn4 = Button(self.master, text='Close', width=10, height=2, command = self.close)
        #self.close calls the close function to close the window
        self.btn4.grid(row=3, column=3)
        

        #Textboxes========================================================
        
        #textbox 1
        self.vartxt1 = self.getPath1
        self.txt1 = Entry(self.master, textvariable=self.vartxt1, width=50, bg='white')
        self.txt1.grid(row=1, column=1, padx=3, columnspan=3)


        #textbox 2
        self.vartxt2 = StringVar()
        self.txt2 = Entry(self.master, textvariable=self.vartxt2, width=50, bg='white')
        self.txt2.grid(row=2, column=1, padx=3, columnspan=3)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
