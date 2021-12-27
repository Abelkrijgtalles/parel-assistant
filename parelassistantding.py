import os
import openeentranslate
import openlandcode
import commands

taal = openlandcode.openen()

print(openeentranslate.openen("nl", "upcheck"))
os.system("curl https://raw.githubusercontent.com/Abelkrijgtalles/parel-assistant/master/config/versie.txt > config/versieonline.txt")

with open(os.path.join("config", "versieonline.txt")) as versieonlinenietint:
    versieonline = int(versieonlinenietint.read())
with open(os.path.join("config", "versie.txt")) as versienietint:
    versie = int(versienietint.read())

if versieonline > versie:
    print(openeentranslate.openen(taal, "updateinstall"), "J/N")
    updateinstall = input()
    updateinstall = updateinstall.upper()
    updateinstall = updateinstall.replace(" ", "")
    if updateinstall == "J":
        print(openeentranslate.openen(taal, "isgit"), "J/N")
        isgit = input()
        isgit = isgit.upper()
        isgit = isgit.replace(" ", "")
        if isgit == "J":
            os.system("git pull")
# Wat te doen
# 4: Gui maken (MOEILIJK!!!!!!!!! en het moet wel mooi zijn)

naamgui = ""

while True:
    print(openeentranslate.openen(taal, "wat"))
    naamgui = input()
    naamgui = (str.upper(naamgui))
    naamgui = naamgui.replace(" ", "")
    print(naamgui, openeentranslate.openen(taal, "open"))
    if naamgui == "SONGTEKSTEN":
        commands.songteksten.main()
    elif naamgui == "DATA":
        commands.data.main()
    elif naamgui == "FEITEN":
        commands.feiten.main()
    elif naamgui == "GILLEN":
        commands.gillen.main()
    elif naamgui == "LANDEN":
        commands.landen.main()
    elif naamgui == "PAASDAG":
        commands.paasdag.main()
    elif naamgui == "TEKENCORONA":
        commands.tekencorona.main()
    elif naamgui == "STOP":
        break
    else:
        print(openeentranslate.openen(taal, "downgrade"))

# EINDE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
