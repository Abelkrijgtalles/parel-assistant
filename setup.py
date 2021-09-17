import os
import time
#import random
#import time
#import turtle as t
#import webbrowser as web
#import string
#from pprint import pprint
#import os
#import tkinter as tk
#from tkinter import simpledialog as simpel
with open("teksten/nl/macallert.txt") as macallert:
    macallert = str(macallert.read())
with open("teksten/nl/pakketinstall.txt") as pakketinstall:
    pakketinstall = str(pakketinstall.read())
with open("teksten/nl/pakketinstallsuc.txt") as pakketinstallsuc:
    pakketinstallsuc = str(pakketinstallsuc.read())
with open("teksten/nl/prostart.txt") as prostart:
    prostart = str(prostart.read())

print(pakketinstall)
print(macallert)

os.system("python -m pip install -U pip")
os.system("pip install turtle")
os.system("pip install pygame")
os.system("pip install pgzero")

print(pakketinstallsuc)
print(prostart)
os.system("python parelassistant.py")