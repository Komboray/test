import time
import os

# print("Please run me in the script")
path = 'C:\\Users\\Raymond\\OneDrive\\Documents\\storepasscreation\\dumy.txt'


if os.path.exists(path):
    print("File exists")

with open(path, "r") as f:
    print(f.readlines())
    

