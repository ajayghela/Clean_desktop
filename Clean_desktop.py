import os
import gspread
from google.oauth2.service_account import Credentials
from datetime import date


def path():
    directory = date.today().strftime('%Y-%m-%d')
    #print(directory)
    parent_dir = "/Users/ajay/Desktop/" # Change path for different computers
    path = os.path.join(parent_dir, directory)
    return path

def file_check():
    desktop_path = "/Users/ajay/Desktop/"
    files = os.listdir(desktop_path)
    #print(files)
    for item in files:
        if item.endswith('.png') or item.endswith('.mov'):
            return True
    return False

def create_destination_folder(path):
    #add if statement to the check if there actually dekstop items and for the folder
    if file_check() == True: 
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory '%s' created" %path)
        else:
            print("Directory '%s' already exists" %path)
    else:
        print("There are no files to move and so no folder has been created")

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

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("clean-desktop-creds.json", scopes=scopes)
client = gspread.authorize(creds)

def write_to_log():
    sheet_id = "1jRr3lYKCHalej1SdiVyPHWr583DgrJQ4BpYPe7iHrKI"
    sheet = client.open_by_key(sheet_id)
    values = sheet.sheet1.row_values(1)
    print(values)


    

#destination_path = path()
#file_check()
#create_destination_folder(destination_path)
#moving_items(destination_path)
write_to_log()