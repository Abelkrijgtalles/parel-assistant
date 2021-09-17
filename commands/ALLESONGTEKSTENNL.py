import webbrowser as web
import tkinter as tk
from tkinter import simpledialog as simpel
from openeentranslate import open as op
from openlandcode import open as landc

taal = landc

root = tk.Tk()
root.withdraw()

nummer = simpel.askstring(title=op(taal, "pakketinstallsuc"), prompt=op(taal, "pakketinstallsuc"))
web.open('https://genius.com/search?q='+str(nummer))
print(op(taal, "website"), 'https://genius.com/search?q='+str(nummer), op(taal, "open"))