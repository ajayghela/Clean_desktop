import os
from datetime import datetime


def desktop_items():
    print(os.listdir("/Users/ajay/Desktop"))

def create_destination_folder():
    os.makedirs("/Users/ajay/Desktop/")

def current_datetime():
    dt = datetime.today()
    print(dt)
    

current_datetime()
