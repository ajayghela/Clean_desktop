import os
from datetime import date


def desktop_items():
    print(os.listdir("/Users/ajay/Desktop"))

def create_destination_folder():
    directory_name = date.today().strftime('%Y-%m-%d')
    #print(directory_name)
    directory = directory_name
    parent_dir = "/Users/ajay/Desktop/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '%s' created" %directory)
    
create_destination_folder()