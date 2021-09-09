import random
import time
import turtle as t
import webbrowser as web
import string
from pprint import pprint
import os
import tkinter as tk
from tkinter import simpledialog as simpel

#Wat te doen
#4: Gui maken (MOEILIJK!!!!!!!!! en het moet wel mooi zijn)

naamgui = ""
root = tk.Tk()
root.withdraw()

while True:
        naamgui = simpel.askstring(title="Hoi", prompt="Wat kan ik voor je doen?")
        naamgui = (str.upper(naamgui))
        naamgui = naamgui.replace(" ", "")
        print(naamgui, "wordt geopend")
        os.system('python commands/'+str(naamgui)+'.py')
    
                

#EINDE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
