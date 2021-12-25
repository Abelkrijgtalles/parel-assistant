import os
import json

os.system("cp -T" + os.__file__ + os.path.join("..", "os.py"))
os.system("cp -T" + json.__file__ + os.path.join("..", "json.py"))
os.system("pip install turtle")
import turtle
os.system("cp -T" + turtle.__file__ + os.path.join("..", "turtle.py"))
import random
os.system("cp -T" + random.__file__ + os.path.join("..", "random.py"))
import tkinter
os.system("cp -T" + tkinter.__file__ + os.path.join("..", "tkinter.py"))
import webbrowser
os.system("cp -T" + webbrowser.__file__ + os.path.join("..", "webbrowser.py"))
import pickle
os.system("cp -T" + pickle.__file__ + os.path.join("..", "pickle.py"))

os.system("cp -T" + pickle.__file__ + os.path.join("..", "commands", "pickle.py"))
os.system("cp -T" + os.__file__ + os.path.join("..", "commands", "os.py"))
os.system("cp -T" + json.__file__ + os.path.join("..", "commands", "json.py"))
os.system("cp -T" + turtle.__file__ + os.path.join("..", "commands", "turtle.py"))
os.system("cp -T" + random.__file__ + os.path.join("..", "commands", "random.py"))
os.system("cp -T" + tkinter.__file__ + os.path.join("..", "commands", "tkinter.py"))
os.system("cp -T" + webbrowser.__file__ + os.path.join("..", "commands", "webbrowser.py"))