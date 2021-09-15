import random
import time
import turtle as t
import webbrowser as web
import string
from pprint import pprint
import os
import tkinter as tk
from tkinter import simpledialog as simpel

os.system("curl https://raw.githubusercontent.com/Abelkrijgtalles/parel-assistant/master/versie.txt > versieonline.txt")

versieonline = open("versieonline.txt", "r")
versie = open("versie.txt", "r")

if not versie == versieonline:
    updateinstall = input("Er is een nieuwe update, wil je hem installeren? J/N")
    updateinstall = updateinstall.upper()
    updateinstall = updateinstall.replace(" ", "")
    if updateinstall == "J":
        isgit = input("Is git geïnstalleerd? J/N")
        isgit = isgit.upper()
        isgit = isgit.replace(" ", "")
        if isgit == "J":
            os.system("git clone https://github.com/Abelkrijgtalles/parel-assistant ../parel-assistant")
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
