##import Tkinter
##import tkFileDialog
##import os
##
##root = Tkinter.Tk()
##root.withdraw() #use to hide tkinter window
##
##currdir = os.getcwd()
##tempdir = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
##if len(tempdir) > 0:
##    print "You chose %s" % tempdir


import tkinter
import tkFileDialog
import os
import time

root = Tkinter.Tk()
root.withdraw() 
currdir = os.getcwd()
##var = open("india.txt","w")
##var.write(
tempdir = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
if len(tempdir) > 0:
    print("You chose %s" % tempdir)
filepath = tempdir +  "_" + "logg.txt"
print(filepath)
var = open(filepath,"w")
print("here")
var.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
var.close()
