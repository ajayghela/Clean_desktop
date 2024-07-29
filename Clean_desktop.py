import os
from datetime import date



def path():
    directory = date.today().strftime('%Y-%m-%d')
    #print(directory)
    parent_dir = "/Users/ajay/Desktop/" # Change path for different computers
    path = os.path.join(parent_dir, directory)
    return path

def file_count(path):
    parent_dir = "/Users/ajay/Desktop/" # Change path for different computers
    files = os.listdir(parent_dir)
    file_count = len(files)
    return file_count

def create_destination_folder(path):
    #add if statement to the check if there actually dekstop items and for the folder
    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory '%s' created" %path)
    else: 
        print("Directory '%s' already exists" %path)
    #error if folder has already been created

def moving_items(path):
    desktop_path = "/Users/ajay/Desktop/"
    files = os.listdir(desktop_path)
    #print(files)
    for item in files: 
       if item[-4:] == '.png' or item[-4:] == '.mov':
           #print(item)
            source = os.path.join(desktop_path, item)
            destination = os.path.join(path, item)
            os.rename(source, destination)
            print(f"Moved '{item}' to '{path}'")
    

destination_path = path()
n_files = file_count(destination_path)
print(n_files)
if n_files > 2:
    create_destination_folder(destination_path)
    moving_items(destination_path)