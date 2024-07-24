import os
from datetime import date

def path():
    directory = date.today().strftime('%Y-%m-%d')
    #print(directory)
    parent_dir = "/Users/ajay/Desktop/"
    path = os.path.join(parent_dir, directory)
    return path

def create_destination_folder(path):
    #add if statement to the check if there actually dekstop items and for the folder
    os.mkdir(path)
    print("Directory '%s' created" %path)
    #error if folder has already been created

def moving_items(path):
    desktop_path = "/Users/ajay/Desktop/"
    files = os.listdir(desktop_path)
    print(files)
    for item in files: 
       if item[-4:] == '.png' or item[-4:] == '.mov':
           #print(item)
            source = os.path.join(desktop_path, item)
            destination = os.path.join(path, item)
            os.rename(source, destination)
            print(f"Moved '{item}' to '{path}'")
    #correct_files = [item for item in files if item[-4:] == '.png' or item[-4:] == '.mov']
    #file_full_path = [os.path.join(desktop_path, item) for item in correct_files] 
    #return file_full_path
    #correct_files = [item for item in files if os.path.splitext(item)[1] in ['.png', '.mov']]
    #print(files)
    #for item in files:
       # if item[-4:] == '.png':
        #    correct_files.append(item)
        #elif item[-4:] == '.mov':
        #    correct_files.append(item)

destination_path = path()
create_destination_folder(destination_path)
moving_items(destination_path)