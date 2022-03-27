import shutil
import os

#set where the source of the files are
source = '/Users/Gabe/Desktop/Folder_A/'

#set the destination path to folder B
destination = '/Users/Gabe/Desktop/Folder_B'
files = os.listdir(source)

#for i in files:
    #shutil.move(source+i, destination)

for i in files:
    if i.endswith('.txt'):      #endswith checks for a string that ends with the value inserted into the function
        shutil.copy(source+i, destination)