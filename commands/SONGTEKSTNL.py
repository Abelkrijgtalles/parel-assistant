import webbrowser as web
import tkinter as tk
from tkinter import simpledialog as simpel

root = tk.Tk()
root.withdraw()

nummer = simpel.askstring(title="Songteksten", prompt="Waar wil je op zoeken?")
web.open('https://genius.com/search?q='+str(nummer))
print('De website', 'https://genius.com/search?q='+str(nummer), 'is geopend')