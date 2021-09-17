import os
import time
from openeentranslate import open as op
from openlandcode import open as landc
#import random
#import time
#import turtle as t
#import webbrowser as web
#import string
#from pprint import pprint
#import os
#import tkinter as tk
#from tkinter import simpledialog as simpel
welketaal = input("What is your two letter language code? If you don't know, then go to this website: http://www.abelr.tk/lc")

os.system("echo", welketaal, "> welketaal.txt")

taal = landc

print(op(taal, "pakketinstall"))
print(op(taal, "macallert"))

os.system("python -m pip install -U pip")
os.system("pip install turtle")
os.system("pip install pygame")
os.system("pip install pgzero")

print(op(taal, "pakketinstallsuc"))
print(op(taal, "prostart"))
os.system("python parelassistant.py")