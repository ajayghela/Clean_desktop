import os
from datetime import datetime


def desktop_items():
    print(os.listdir("/Users/ajay/Desktop"))

def create_destination_folder():
    directory_name = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    #print(directory_name)

    directory = directory_name
    parent_dir = "/Users/ajay/Desktop/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '%s' created" %directory)



#def rename_destination_folder()

    

create_destination_folder()