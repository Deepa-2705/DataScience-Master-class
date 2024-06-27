#Our task is to use this method in course_detail file
#task:Import everything from one module to another module

#**Package** is a directory or folder
#All the files inside a package folder is called **module**


import os,sys
from os.path import dirname,abspath,join                               #Write 3 lines 
sys.path.insert(0, abspath(join(dirname(__file__),'..')))    #This 3 lines will collapse all the folder

from courses import course_details

def paymentdet():
    print("This is my payment details")

course_details.coursedet()

#the output will not display in case of circular import