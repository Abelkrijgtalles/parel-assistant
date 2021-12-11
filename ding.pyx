def main():
    import os
    from openeentranslate import openen as op
    from openlandcode import openen as landc
    from parelassistantding import main as startem
    # import random
    # import time
    # import turtle as t
    # import webbrowser as web
    # import string
    # from pprint import pprint
    # import os
    # import tkinter as tk
    # from tkinter import simpledialog as simpel

    taal = landc()

    with open(os.path.join("config", "welketaal")) as f:
        welketaal = input(op(taal, "welketaal"))
        f.write(welketaal)

    print(op(taal, "pakketinstall"))
    print(op(taal, "macallert"))

    os.system("python -m pip install -U pip")
    os.system("pip install turtle")
    os.system("pip install pygame")

    print(op(taal, "pakketinstallsuc"))
    print(op(taal, "prostart"))
    startem()
