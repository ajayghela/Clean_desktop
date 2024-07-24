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
    print("Directory '%s' created" %directory)

    #error if folder has already been created

def moving_items(path):
    files = os.listdir("/Users/ajay/Desktop")
    print(files)
    for item in files: 
       if item[-4:] == '.png' or item[-4:] == '.mov':
           #print(item)
            os.path.join(path, item)
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

path = path()
create_destination_folder()
moving_items()