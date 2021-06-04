import os
import shutil

source = input("Enter your source folder name : ")
destination = input("Enter your Destination : ")
source = source+'/'
destination = destination+'/'
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)
