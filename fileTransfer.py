





from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd    #lets you use files
import os
import shutil
 

class ParentWindow(Frame):

    #definitions==============================================================
    def close(self):
        self.master.destroy()   #closes window

    def getPath1(self):         #opens file manager and stores file path
        path1 = fd.askdirectory()
        self.txt1.delete('0','end')
        self.txt1.insert(0, path1)
        print(path1)

    def getPath2(self):         #opens file manager and stores file path
        path2 = fd.askdirectory()
        self.txt2.delete('0','end')
        self.txt2.insert(0, path2)

    def copyFiles(self):
        path1 = self.txt1.get()
        path2 = self.txt2.get()
        os.listdir(path1)
        for i in path1:
            shutil.copy(path1+i, path2)

    def __init__(self, master, *args, **kwargs):    #initalizes Frame
        Frame.__init__(self, master, *args, **kwargs)

    

        #defining master frame config
        self.master = master
        self.master.geometry('{}x{}'.format(450, 200))
        self.master.config(bg = 'lightgray')

        #blank space
        self.blank = Label(self.master, text='', bg='lightgray')
        self.blank.grid(row=0, column=0)

        #Buttons==========================================================
        
        #browse button 1
        self.btn1 = Button(self.master, text='Browse', width=10, height=1, command=self.getPath1)
        self.btn1.grid(row=1, column=0, padx=10, pady=10, sticky=N+W)

        #browse button 2
        self.btn2 = Button(self.master, text='Browse', width=10, height=1, command=self.getPath2)
        self.btn2.grid(row=2, column=0, padx=10, pady=5, sticky=N+W)

        #Copy Files=======================================================

        #button
        self.btn3 = Button(self.master, text='Copy Files', width=10, height=2, command=self.copyFiles)
        self.btn3.grid(row=3, column=0, padx=3, pady=10)


        #Close program====================================================

        self.btn4 = Button(self.master, text='Close', width=10, height=2, command = self.close)
        #self.close calls the close function to close the window
        self.btn4.grid(row=3, column=3)
        

        #Textboxes========================================================
        
        #textbox 1
        self.txt1 = Entry(self.master, width=50, bg='white')
        self.txt1.grid(row=1, column=1, padx=3, columnspan=3)


        #textbox 2
        self.txt2 = Entry(self.master, width=50, bg='white')
        self.txt2.grid(row=2, column=1, padx=3, columnspan=3)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
