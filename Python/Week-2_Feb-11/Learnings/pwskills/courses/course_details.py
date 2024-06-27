#Our task is to use this method in payment_detail file
#task:Import everything from one module to another module

#**Package** is a directory or folder
#All the files inside a package folder is called **module**



#This error is coming because the payment_detail python file inside multiple folder 
# the system is unable to find the particular file 
#we can solve this error by collapsing all the file path so that the system can find the file


import os,sys
from os.path import dirname,abspath,join                               #Write 3 lines 
sys.path.insert(0, abspath(join(dirname(__file__),'..')))    #This 3 lines will collapse all the folder

from payment import payment_details

def coursedet():
    print("This is my course file")

payment_details.paymentdet()    #No module name payment error is coming .But Why?

#the output will not display in case of circular import
