import os
from openeentranslate import openen as op
from openlandcode import openen as landc
import commands

taal = landc()

print(op("nl", "upcheck"))
os.system("curl https://raw.githubusercontent.com/Abelkrijgtalles/parel-assistant/master/config/versie.txt > config/versieonline.txt")

with open(os.path.join("config", "versieonline.txt")) as versieonlinenietint:
    versieonline = int(versieonlinenietint.read())
with open(os.path.join("config", "versie.txt")) as versienietint:
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
# Wat te doen
# 4: Gui maken (MOEILIJK!!!!!!!!! en het moet wel mooi zijn)

naamgui = ""

while True:
    naamgui = input(op(taal, "wat"))
    naamgui = (str.upper(naamgui))
    naamgui = naamgui.replace(" ", "")
    print(naamgui, op(taal, "open"))
    if naamgui == "SONGTEKSTEN":
        commands.songteksten()
    elif naamgui == "DATA":
        commands.data()
    elif naamgui == "FEITEN":
        commands.feiten()
    elif naamgui == "GILLEN":
        commands.gillen()
    elif naamgui == "LANDEN":
        commands.landen()
    elif naamgui == "PAASDAG":
        commands.paasdag()
    elif naamgui == "TEKENCORONA":
        commands.tekencorona()
    elif naamgui == "WEER":
        commands.weer()
    elif naamgui == "WIEBENIK":
        commands.wiebenik
    elif naamgui == "STOP":
        break
    else:
        print(op(taal, "downgrade"))

# EINDE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
