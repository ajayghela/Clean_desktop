import os
from datetime import date


def desktop_items():
    files = os.listdir("/Users/ajay/Desktop")
    correct_files = [item for item in files if item[-4:] == '.png' or item[-4:] == '.mov']
    #print(files)
    #for item in files:
       # if item[-4:] == '.png':
        #    correct_files.append(item)
        #elif item[-4:] == '.mov':
        #    correct_files.append(item)
    print(correct_files)
    

def create_destination_folder():
    directory_name = date.today().strftime('%Y-%m-%d')
    #print(directory_name)
    directory = directory_name
    parent_dir = "/Users/ajay/Desktop/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '%s' created" %directory)
    
desktop_items()