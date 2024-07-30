import os
from datetime import date


def path():
    directory = date.today().strftime('%Y-%m-%d')
    #print(directory)
    parent_dir = "/Users/ajay/Desktop/" # Change path for different computers
    path = os.path.join(parent_dir, directory)
    return path

def create_destination_folder(path):
    #add if statement to the check if there actually dekstop items and for the folder
    desktop_path = "/Users/ajay/Desktop/"
    files = os.listdir(desktop_path)
    #print(files)
    files_present = 0
    for item in files:
        if item.endswith('.png') or item.endswith('.mov'):
            return True
    while True: 
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory '%s' created" %path)
            break
        else:
            print("Directory '%s' already exists" %path)
            break
            

   # for item in files: 
    #    if item.endswith('.png') or item.endswith('.mov') and not os.path.exists(path):
     #           os.mkdir(path)
      #          print("Directory '%s' created" %path)
       # elif item[-4:] == '.png' or item[-4:] == '.mov':
        #    print("Directory '%s' already exists" %path)
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
#n_files = file_count(destination_path)
#print(n_files)
create_destination_folder(destination_path)
#moving_items(destination_path)