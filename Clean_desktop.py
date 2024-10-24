import os
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from datetime import date

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("clean-desktop-creds.json", scopes=scopes)
service = build('sheets', 'v4', credentials=creds)


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
    srce_lst = []
    dest_lst = []
    #print(files)
    for item in files: 
       if item[-4:] == '.png' or item[-4:] == '.mov':
           #print(item)
            source = os.path.join(desktop_path, item)
            srce_lst.append(source)
            destination = os.path.join(path, item)
            dest_lst.append(destination)
            os.rename(source, destination)
            print(f"Moved '{item}' to '{path}'")
    return srce_lst, dest_lst

def write_to_log(srce_lst, col):
    sheet_id = "1jRr3lYKCHalej1SdiVyPHWr583DgrJQ4BpYPe7iHrKI"
    sheet = client.open_by_key(sheet_id).sheet1
    #sheet.update(f"A1:{len(srce_lst)}", srce_lst)
    range = f'!{col}'
    body = {'majorDimension': 'ROWS', 'values': srce_lst}
    response = sheet.values().append(spreadsheetId=sheet_id,
                                     range=range,
                                     body=body,
                                     valueInputOption='USER_ENTERED',
                                     includeValuesInResponse=False).execute()
    print(values)

    
destination_path = path()
#lts = moving_items(destination_path)
file_check()
create_destination_folder(destination_path)
moving_items(destination_path)
#srce_lst, dest_lst = moving_items(destination_path)
#write_to_log(srce_lst, "B")
#write_to_log(dest_lst, "C")