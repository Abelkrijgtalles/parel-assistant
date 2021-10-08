import os
from openeentranslate import openen as op
from openlandcode import openen as landc
# import random
# import time
# import turtle as t
# import webbrowser as web
# import string
# from pprint import pprint
# import os
# import tkinter as tk
# from tkinter import simpledialog as simpel



welketaal = input("What is your two letter language code? If you don't know, then go to this website: https://abelr.tk/lc : ")

with open("config/welketaal.txt") as f:
    f.write(welketaal)

taal = landc

print(op(taal, "pakketinstall"))
print(op(taal, "macallert"))

os.system("python -m pip install -U pip")
os.system("pip install turtle")
os.system("pip install pygame")

print(op(taal, "pakketinstallsuc"))
print(op(taal, "prostart"))
os.system("python parelassistant.py")
