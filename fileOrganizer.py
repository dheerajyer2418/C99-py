import os
import shutil
path = input("Enter the name of the directory to be sorted: ")
list_of_files = os.listdir(path)
#This will go through each and every file
for file in list_of_files: 
    name, ext = os.path.splitext(file)
    #this is going to store the extention type
    ext = ext[1:]
    #this forces the next iteration if it is the directory
    if ext == '':
        continue
    #this will move the file in the directory where the name 'ext' already exists
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    #this will create a new directory if the directory doesn't exist
    else: 
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
        