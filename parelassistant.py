import turtle as t
import webbrowser as web
from pprint import pprint
import os
import tkinter as tk
from tkinter import simpledialog as simpel
from openeentranslate import openen as op
from openlandcode import openen as landc

taal = landc

print(op("nl", "upcheck"))
os.system("curl https://raw.githubusercontent.com/Abelkrijgtalles/parel-assistant/master/versie.txt > config/versieonline.txt")

with open("config/versieonline.txt") as versieonlinenietint:
    versieonline = int(versieonlinenietint.read())
with open("config/versie.txt") as versienietint:
    versie = int(versienietint.read())

if versieonline > versie:
    updateinstall = input(op(taal, "updateinstall"), "J/N")
    updateinstall = updateinstall.upper()
    updateinstall = updateinstall.replace(" ", "")
    if updateinstall == "J":
        isgit = input(op(taal, "updateinstall"), "J/N")
        isgit = isgit.upper()
        isgit = isgit.replace(" ", "")
        if isgit == "J":
            os.system("git pull")
#Wat te doen
#4: Gui maken (MOEILIJK!!!!!!!!! en het moet wel mooi zijn)

naamgui = ""
root = tk.Tk()
root.withdraw()

while True:
        naamgui = simpel.askstring(title=op(taal, "hoi"), prompt=op(taal, "wat"))
        naamgui = (str.upper(naamgui))
        naamgui = naamgui.replace(" ", "")
        print(naamgui, op(taal, "open"))
        os.system('python commands/'+str(naamgui)+'.py')
    
                

#EINDE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
