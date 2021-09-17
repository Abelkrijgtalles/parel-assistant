import os
import time
from openeentranslate import open as op
#import random
#import time
#import turtle as t
#import webbrowser as web
#import string
#from pprint import pprint
#import os
#import tkinter as tk
#from tkinter import simpledialog as simpel
print(op("nl", "pakketinstall"))
print(op("nl", "macallert"))

os.system("python -m pip install -U pip")
os.system("pip install turtle")
os.system("pip install pygame")
os.system("pip install pgzero")

print(op("nl", "pakketinstallsuc"))
print(op("nl", "prostart"))
os.system("python parelassistant.py")