def main():
    import os
    import openeentranslate
    import openlandcode
    import parelassistantding
    # import random
    # import time
    # import turtle as t
    # import webbrowser as web
    # import string
    # from pprint import pprint
    # import os
    # import tkinter as tk
    # from tkinter import simpledialog as simpel

    taal = openlandcode.openen()

    with open(os.path.join("config", "welketaal")) as f:
        welketaal = input(openeentranslate.openen(taal, "welketaal"))
        f.write(welketaal)

    print(openeentranslate.openen(taal, "prostart"))
    parelassistantding.main()
