# This script creates a project standard project structure according to the Real Python article
# https://realpython.com/python-application-layouts/

import pathlib
import os

# TODO get the folder path from the user

PATH = "C://code/testfolder/"
stringlist = PATH.split("/")
SCRIPT_NAME = stringlist[-2]
# print(stringlist[-2])

#Create path for the main script
SRC_PATH = PATH + SCRIPT_NAME + "/"
os.makedirs(SRC_PATH)
src = open(SRC_PATH + "testfolder.py", "w")
src.write("#Write the source code in file.This is the script that you’re distributing")
src.write("#As far as naming the main script file goes,I recommend that you go with the name of your project") 
src.write("which is the same as the name of the top-level directory")
src.close()


#create helper.py
helper = open(SRC_PATH+"helpers.py", "w")
helper.write("#this file is for all the helper methods")
helper.close()

 #create _init_.py
init = open(SRC_PATH + "_init_.py", "w")

#Create path for the docs
DOC_PATH = PATH + "docs"
os.mkdir(DOC_PATH)

#Create path for tests
TEST_PATH = PATH + "tests/"
os.mkdir(TEST_PATH)
tests = open(TEST_PATH + "/tests.py", "w")


# Create requirements.txt and write a comment
req = open(PATH + "requirements.txt", "w")
req.write(
    "# This file defines outside Python dependencies and their versions for your application."
)
req.close()

